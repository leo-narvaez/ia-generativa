import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

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
            messages=[{"role": "system", "content": "Dado el siguiente listado de información con etiquetas, por favor, devuélvelo en formato de lista estructurada, con las etiquetas correctamente organizadas y separadas por su respectivo valor:"},
                    {"role": "user", "content": command}],
            temperature=0,
        )
        response_text = response.choices[0].message.content
        print("Respondido...")
        return response_text
    
    except Exception as e:
        print("Error en la llamada a OpenAI:", e)
        return "Lo siento, ocurrió un error al procesar tu solicitud."