from dotenv import load_dotenv
import os
import streamlit as st
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.questionanswering import QuestionAnsweringClient
from azure.ai.textanalytics import TextAnalyticsClient

st.set_page_config(
    page_title="MotoBot",  # Título de la página en la pestaña
    page_icon="🏍️",  # Puedes poner la URL de un icono o la ruta local
)

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

# Cambiar el fondo de toda la página
st.markdown("""
    <style>
        body {
            background-color: #2C3E50;
        }
    </style>
""", unsafe_allow_html=True)

# Título y encabezado de la aplicación
st.title("MotoBot")
st.subheader("Tu fuente instantánea de sabiduría sobre MotoGP. 🏍️💨")

if 'messages' not in st.session_state:
    st.session_state.messages = []

# Función para generar el resumen
def generate_response(question):
    response = ai_client.get_answers(
        project_name=ai_project_name,
        deployment_name=ai_deployment_name,
        question=question,
    )
    return response

# Función para analizar el sentimiento
def analyze_sentiment(text):
    sentiment_result = ai_client_sentiment.analyze_sentiment([text])
    sentiment = sentiment_result[0].sentiment
    return sentiment

# Función para procesar la pregunta y mostrar la respuesta
def process_question(question):
    st.chat_message("user").markdown(question)
    sentiment = analyze_sentiment(question)
    st.session_state.messages.append({"role": "user", "content": question, "sentiment": sentiment})

    try:
        response = generate_response(question)
        if response.answers:
            answer = response.answers[0].answer
        else:
            answer = "Lo siento, no pude encontrar una respuesta a esa pregunta."
    except Exception as e:
        answer = f"Hubo un error al procesar la pregunta: {e}"

    with st.chat_message("assistant"):
        st.markdown(answer)
        response_sentiment = analyze_sentiment(answer)
        st.markdown(f"_Sentimiento: {response_sentiment}_")
    
    st.session_state.messages.append({"role": "assistant", "content": answer, "sentiment": response_sentiment})

# Botones con preguntas por defecto
default_questions = [
    "¿Quién es el último campeón de MotoGP?",
    "¿Cuándo es la próxima carrera?",
    "¿Quién es el piloto con más campeonatos?"
]

cols = st.columns(len(default_questions))
for i, question in enumerate(default_questions):
    if cols[i].button(question):
        process_question(question)

# Mostrar mensajes previos como una conversación
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "sentiment" in message:
            st.markdown(f"_Sentimiento: {message['sentiment']}_")

# Caja de texto para entrada del usuario
if question := st.chat_input("Escribe tu pregunta aquí..."):
    process_question(question)

# Botón para reiniciar o limpiar el historial
if st.button("Empezar de nuevo"):
    st.session_state.messages = []  # Limpiar el historial
