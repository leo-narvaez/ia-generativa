from dotenv import load_dotenv
from datetime import datetime
import os
import tempfile
# Import namespaces
import azure.cognitiveservices.speech as speech_sdk
from openai import AzureOpenAI

def gpt_response(command):
    try:
        client = AzureOpenAI(
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version="2024-02-01"
        )
        model = os.getenv("AZURE_OPENAI_MODEL")
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "system", "content": "Eres un asistente, que tiene la capacidad de responder preguntas de forma corta y clara."},
                    {"role": "user", "content": command}],
            temperature=0,
        )
        response_text = response.choices[0].message.content
        return response_text
    
    except Exception as e:
        print("Error en la llamada a OpenAI:", e)
        return "Lo siento, ocurrió un error al procesar tu solicitud."

def TranscribeCommand(speech_config, audio):
    command = ''
    
    # Guardamos el audio recibido en un archivo temporal
    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_audio_file:
        temp_audio_file.write(audio)  # Escribimos el audio en el archivo temporal
        temp_audio_file_path = temp_audio_file.name  # Obtenemos la ruta del archivo temporal

    print(f"Archivo temporal creado: {temp_audio_file_path}")

    # Configura el archivo de audio para Azure
    audio_config = speech_sdk.audio.AudioConfig(filename=temp_audio_file_path)
    
    # Crea el Speech Recognizer para capturar el audio del archivo
    speech_recognizer = speech_sdk.SpeechRecognizer(speech_config, audio_config)

    print("Reconociendo el audio...")

    # Usamos el reconocedor de voz para obtener la transcripción
    speech = speech_recognizer.recognize_once_async().get()

    # Verificamos si el reconocimiento fue exitoso
    if speech.reason == speech_sdk.ResultReason.RecognizedSpeech:
        command = speech.text
        print(f"Comando reconocido: {command}")
    else:
        print(speech.reason)
        if speech.reason == speech_sdk.ResultReason.Canceled:
            cancellation = speech.cancellation_details
            print(f"Error en la cancelación: {cancellation.reason}")
            print(f"Detalles del error: {cancellation.error_details}")

    # Eliminamos el archivo temporal después de procesarlo
    os.remove(temp_audio_file_path)

    return command

def Tellme(response_text: str, speech_config):
    # Configure speech synthesis
    speech_config.speech_synthesis_voice_name = "es-ES-XimenaMultilingualNeural"
    speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config)
    # Synthesize spoken output
    responseSsml = " \
        <speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='en-US'> \
            <voice name='es-ES-XimenaMultilingualNeural'> \
                {} \
            </voice> \
        </speak>".format(response_text)
    speak = speech_synthesizer.speak_ssml_async(responseSsml).get()
    if speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
        print(speak.reason)

    # Print the response
    print(response_text)