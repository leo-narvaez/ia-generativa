from dotenv import load_dotenv
import os
import streamlit as st
import streamlit.components.v1 as components
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.questionanswering import QuestionAnsweringClient
from azure.ai.textanalytics import TextAnalyticsClient


st.set_page_config(
    page_title="MotoBot",  # Título de la página en la pestaña
    page_icon="🏍️",  # Puedes poner la URL de un icono o la ruta local
)

# Título y encabezado de la aplicación
st.title("MotoBot")
st.subheader("Tu fuente instantánea de sabiduría sobre MotoGP. 🏍️💨")

# Preguntas predefinidas
default_questions = [
    "Tabla de clasificación Campeonato 2024",
    "Calendario grandes premios MotoGP 2025",
    "Pilotos y equipos MotoGP 2025"
]
# Imágenes predefinidas asociadas a cada pregunta (Puedes poner las URLs de las imágenes que desees)
image_links = [
    "https://e00-xlk-ue-marca.uecdn.es/uploads/2024/12/04/17318548398367.jpeg",
    "https://estaticos-cdn.prensaiberica.es/clip/56d57d8a-2cd9-4cc8-b564-29129b1ab361_alta-libre-aspect-ratio_default_0.jpg",
    "https://resources.motogp.pulselive.com/photo-resources/2024/09/19/c8d424b9-69b1-43e6-8327-8f4faa4119de/Line_up-initial-2025-16_9-3_06.jpg?width=1440&height=810"
]

# Imagen por defecto (que se mostrará inicialmente)
default_image = "https://e00-xlk-ue-marca.uecdn.es/uploads/2024/11/20/17073103830374.jpeg"

# Función para mostrar la imagen correspondiente
def show_image(image_url):
    st.image(image_url, use_container_width=True)

# Crear las columnas para los botones
cols = st.columns(len(default_questions))

# Lógica para procesar la pregunta y mostrar la imagen correspondiente
image_shown = False  # Variable de control para saber si se ha mostrado una imagen

for i, question in enumerate(default_questions):
    if cols[i].button(question, use_container_width=True):
        show_image(image_links[i])  # Muestra la imagen correspondiente
        image_shown = True  # Se marca que ya se mostró una imagen

# Si no se ha mostrado una imagen, mostrar la imagen por defecto
if not image_shown:
    show_image(default_image)


if 'messages' not in st.session_state:
    st.session_state.messages = []

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
    # Mostrar el historial de mensajes antes de procesar la nueva pregunta/respuesta
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Mostrar la pregunta del usuario
    st.chat_message("user").markdown(question)
    st.session_state.messages.append({"role": "user", "content": question})

    try:
        # Generar la respuesta de la IA
        response = generate_response(question)
        if response.answers:
            answer = response.answers[0].answer
        else:
            answer = "Lo siento, no pude encontrar una respuesta a esa pregunta."
    except Exception as e:
        answer = f"Hubo un error al procesar la pregunta: {e}"

    # Mostrar la respuesta de la IA
    with st.chat_message("assistant"):
        st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})

# Botones con preguntas por defecto
default_questions = [
    "¿Quién es el último campeón de MotoGP?",
    "¿Cuándo es la próxima carrera?",
    "¿Quién es el piloto con más campeonatos?"
]

cols = st.columns(len(default_questions))
for i, question in enumerate(default_questions):
    if cols[i].button(question, use_container_width=True):
        process_question(question)
        
# Caja de texto para entrada del usuario
if question := st.chat_input("Escribe tu pregunta aquí..."):
    process_question(question)

# Botón para reiniciar o limpiar el historial
if st.session_state.messages and st.button("Limpiar historial"):
    st.session_state.messages = []  # Limpiar
    st.rerun()  # Reiniciar la aplicación
