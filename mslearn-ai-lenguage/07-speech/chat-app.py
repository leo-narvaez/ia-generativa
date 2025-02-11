import streamlit as st
import openai
import os
from dotenv import load_dotenv
from speaking import *

st.set_page_config(
    page_title="Hablameloo",  # Título de la página en la pestaña
    page_icon="📣",  # Puedes poner la URL de un icono o la ruta local
)

# Título y encabezado de la aplicación
st.title("Hablamelo")
st.subheader("📣 A ver si te puedo responder")

# Imagen por defecto (que se mostrará inicialmente)
default_image = "https://img.freepik.com/vector-gratis/inteligencia-artificial-robot-isometrico-ai-pantalla-telefono-movil-aplicacion-chatbot_39422-767.jpg?t=st=1739271141~exp=1739274741~hmac=c3161613ef3df23767bacc90171b3e4793f1da81b4ec741ab21242ce8fe5a3be&w=996"

# Función para mostrar la imagen correspondiente
def show_image(image_url):
    st.image(image_url, use_container_width=True)

show_image(default_image)

# Configuración de Azure Speech
def setup_speech_config():
    load_dotenv()
    ai_key = os.getenv('SPEECH_KEY')
    ai_region = os.getenv('SPEECH_REGION')

    # Configure speech service
    speech_config = speech_sdk.SpeechConfig(ai_key, ai_region)
    return speech_config

# Configuración de Azure Speech
speech_config = setup_speech_config()

# Función para capturar el audio o texto
def get_user_input():
    # Primero intentamos capturar audio
    audio = st.audio_input(label="Habla conmigo")

    if audio is not None:
        # Si se ha recibido audio, lo procesamos
        return TranscribeCommand(speech_config, audio)
    else:
        # Si no hay audio, le damos al usuario la opción de ingresar texto
        return st.text_input("Escribe algo:", "")

command = get_user_input()

if command:
    response = gpt_response(command)
    Tellme(response, speech_config)
    st.write(response)