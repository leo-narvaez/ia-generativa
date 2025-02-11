from dotenv import load_dotenv
import os
import json
from datetime import datetime, timedelta, date, timezone
from dateutil.parser import parse as is_date

# Import namespaces
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.conversations import ConversationAnalysisClient


def detect_intent(intent):
    try:
        # Crear un diccionario para almacenar los resultados
        output_content = {}

        # Get Configuration Settings
        load_dotenv()
        ls_prediction_endpoint = os.getenv('LS_CONVERSATIONS_ENDPOINT')
        ls_prediction_key = os.getenv('LS_CONVERSATIONS_KEY')
        ls_prediction_project_name = os.getenv('LS_CONVERSATIONS_PROJECT_NAME')
        ls_deployment_name = os.getenv('LS_DEPLOYMENT_NAME')
        
        # Get user input (until they enter "quit")
        userText = intent

        # Create a client for the Language service model
        client = ConversationAnalysisClient(
            ls_prediction_endpoint, AzureKeyCredential(ls_prediction_key))

        with client:
            query = userText
            result = client.analyze_conversation(
                task={
                    "kind": "Conversation",
                    "analysisInput": {
                        "conversationItem": {
                            "participantId": "1",
                            "id": "1",
                            "modality": "text",
                            "language": "es",
                            "text": query
                        },
                        "isLoggingEnabled": False
                    },
                    "parameters": {
                        "projectName": ls_prediction_project_name,
                        "deploymentName": ls_deployment_name,
                        "verbose": True
                    }
                }
            )

        top_intent = result["result"]["prediction"]["topIntent"]
        entities = result["result"]["prediction"]["entities"]

        # Agregar los detalles de la intención y las entidades al diccionario
        output_content["topIntent"] = top_intent
        output_content["intents"] = [
            {
                "category": result["result"]["prediction"]["intents"][0]["category"],
                "confidenceScore": result["result"]["prediction"]["intents"][0]["confidenceScore"]
            }
        ]
        output_content["entities"] = [
            {
                "category": entity["category"],
                "text": entity["text"],
                "confidenceScore": entity["confidenceScore"]
            } for entity in entities
        ]
        output_content["query"] = result["result"]["query"]

        # Apply the appropriate action
        if top_intent == 'GetPilot':
            if len(entities) > 0:
                for entity in entities:
                    if 'Nombre del Piloto' == entity["category"]:
                        response_text = entity["text"]
                output_content["pilotInfo"] = GetPilot(response_text)

        elif top_intent == 'GetCalendar':
            if len(entities) > 0:
                for entity in entities:
                    if 'Gran Premio' == entity["category"]:
                        response_text = entity["text"]
                output_content["calendarInfo"] = GetCalendar(response_text)

        # Convertir el diccionario a formato JSON
        return json.dumps(output_content), top_intent  # Devolver el JSON y la intención

    except Exception as e:
        # Capturar excepciones y devolver un mensaje de error en lugar de None
        error_output = {"error": str(e)}
        return json.dumps(error_output), None  # Retornar el error en formato JSON y None para la intención
    

def GetPilot(pilot):
    return "Solicita información del piloto: " + pilot

def GetCalendar(premio):
    return "Solicita información del: " + premio

