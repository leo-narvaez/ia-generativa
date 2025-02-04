from dotenv import load_dotenv
import os
import streamlit as st
import time

# Import namespaces
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
from azure.ai.language.questionanswering import QuestionAnsweringClient


try:
    # Get Configuration Settings
    load_dotenv()
    ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
    ai_key = os.getenv('AI_SERVICE_KEY')
    ai_project_name = os.getenv('QA_PROJECT_NAME')
    ai_deployment_name = os.getenv('QA_DEPLOYMENT_NAME')

    # Create client using endpoint and key
    credential = AzureKeyCredential(ai_key)
    ai_client = QuestionAnsweringClient(endpoint=ai_endpoint, credential=credential)
    ai_client_sentiment = TextAnalyticsClient(endpoint=ai_endpoint, credential=credential)

except Exception as ex:
    print(ex)


# Título y encabezado de la aplicación
st.title("MotoBot")
st.subheader("Tu fuente instantánea de sabiduría sobre MotoGP. 🏍️💨")


# Crear un área de texto para ingresar un email
question = st.text_area("Que quieres saber:", "")

# Función para generar el resumen
def genereate_response(question=""):
    # Submit a question and display the answer
    response = ai_client.get_answers(question=question,
        project_name=ai_project_name,
        deployment_name=ai_deployment_name)
    return response.answers[0].answer

def get_sentiment(question=""):
    try:
        # Realizar análisis de sentimientos
        sentiment_result = ai_client_sentiment.analyze_sentiment([question])
        sentiment = sentiment_result[0].sentiment
        return sentiment_to_emoji(sentiment)
    except Exception as e:
        return f"Error en el análisis de sentimientos: {e}"

# Función para mostrar el emoji según el sentimiento
def sentiment_to_emoji(sentiment):
    if sentiment == 'positive':
        return "🤩"  # Emoji positivo
    elif sentiment == 'neutral':
        return "😐"  # Emoji neutral
    else:
        return "😡"  # Emoji negativo

response = ''
if st.button("Preguntar", use_container_width=True):
    with st.spinner("Generando respuesta... Espera mi pana..."):
        sentiment = get_sentiment(question)
        response = genereate_response(question)
        st.success("Ya respondí!")
        time.sleep(1)

if response:    
        st.write(sentiment)
        st.write(response)
        # Botón para reiniciar o limpiar respuesta
        if st.button("Empezar de nuevo", use_container_width=True):
            question = ""  # Limpiar el campo de texto
            response = None  # Limpiar la respuesta
            st.experimental_rerun()