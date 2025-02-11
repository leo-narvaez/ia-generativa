import streamlit as st
import openai
import os
from dotenv import load_dotenv
from speaking import *


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

# Llamar a la función de reconocimiento de voz en Streamlit
audio = st.audio_input(label="Habla conmigo")
if audio is not None:
    # Transcribe the audio
    command = TranscribeCommand(speech_config, audio)
    st.write(f"Comando: {command}")

    # Get the response from the AI model
    response = gpt_response(command)

    # Speak the response
    Tellme(response, speech_config)