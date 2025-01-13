import os
from openai import AzureOpenAI
from dotenv import load_dotenv
from datetime import datetime

# Cargar el archivo .env
load_dotenv()

# Configurar el cliente de Azure OpenAI
client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-01"
)

# Crear la carpeta 'chatlogs' si no existe
if not os.path.exists("chatlogs"):
    os.makedirs("chatlogs")

# Obtener la fecha y hora actual para nombrar el archivo
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file = f"chatlogs/chat_log_{current_time}.txt"

# Función para escribir en el archivo con formato
def log_message(role, content):
    with open(log_file, "a", encoding="utf-8") as file:
        file.write(f"[{role}]:\n")
        file.write(f"{content}\n\n")

# Mensajes iniciales de la conversación
messages = [
    {"role": "system", "content": "Eres un asistente virtual. Responde con amabilidad y claridad pero de forma resumida y directa."}
]

# Registrar el mensaje del system en el archivo
log_message("system", messages[0]["content"])

# Bucle para interactuar con el usuario
while True:
    # Leer el mensaje del usuario
    user_input = input("Tú: ")

    if user_input.lower() == "salir":
        print("¡Hasta luego!")
        break

    # Agregar el mensaje del usuario a los mensajes
    messages.append({"role": "user", "content": user_input})

    # Registrar el mensaje del usuario en el archivo
    log_message("user", user_input)

    # Solicitar la respuesta del asistente
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Modelo que deseas usar
        messages=messages
    )

    # Obtener la respuesta del asistente
    assistant_response = response.choices[0].message.content

    # Mostrar la respuesta en la terminal
    print(f"Asistente: {assistant_response}")

    # Agregar la respuesta del asistente a los mensajes
    messages.append({"role": "assistant", "content": assistant_response})

    # Registrar la respuesta del asistente en el archivo
    log_message("assistant", assistant_response)
