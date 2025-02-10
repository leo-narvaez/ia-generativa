from dotenv import load_dotenv
import os
import json
from datetime import datetime, timedelta, date, timezone
from dateutil.parser import parse as is_date

# Import namespaces
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.conversations import ConversationAnalysisClient


def main():

    try:
        # Get Configuration Settings
        load_dotenv()
        ls_prediction_endpoint = os.getenv('LS_CONVERSATIONS_ENDPOINT')
        ls_prediction_key = os.getenv('LS_CONVERSATIONS_KEY')
        ls_prediction_project_name = os.getenv('LS_CONVERSATIONS_PROJECT_NAME')
        ls_deployment_name = os.getenv('LS_DEPLOYMENT_NAME')
        # Get user input (until they enter "quit")
        userText = ''
        while userText.lower() != 'quit':
            userText = input('\nEnter some text ("quit" to stop)\n')
            if userText.lower() != 'quit':

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

                print("view top intent:")
                print("\ttop intent: {}".format(result["result"]["prediction"]["topIntent"]))
                print("\tcategory: {}".format(result["result"]["prediction"]["intents"][0]["category"]))
                print("\tconfidence score: {}\n".format(result["result"]["prediction"]["intents"][0]["confidenceScore"]))

                print("view entities:")
                for entity in entities:
                    print("\tcategory: {}".format(entity["category"]))
                    print("\ttext: {}".format(entity["text"]))
                    print("\tconfidence score: {}".format(entity["confidenceScore"]))

                print("query: {}".format(result["result"]["query"]))
                
                # Apply the appropriate action
                if top_intent == 'GetPilot':
                    # Check for entities
                    if len(entities) > 0:
                        # Check for a location entity
                        for entity in entities:
                            if 'Nombre del Piloto' == entity["category"]:
                                # ML entities are strings, get the first one
                                pilot = entity["text"]
                    # Get the time for the specified pilot
                    print(GetPilot(pilot))

                elif top_intent == 'GetCalendar':
                    # Check for entities
                    if len(entities) > 0:
                        # Check for a location entity
                        for entity in entities:
                            if 'Gran Premio' == entity["category"]:
                                # ML entities are strings, get the first one
                                premio = entity["text"]
                    # Get the time for the specified pilot
                    print(GetCalendar(premio))

    except Exception as ex:
        print(ex)

def GetPilot(pilot):
    return "Solicita información del piloto: " + pilot

def GetCalendar(premio):
    return "Solicita información del: " + premio

if __name__ == "__main__":
    main()