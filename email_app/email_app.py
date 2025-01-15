import os
import streamlit as st
from openai import AzureOpenAI
from dotenv import load_dotenv
import time

# Cargar el archivo .env
load_dotenv()

# Configurar el cliente de Azure OpenAI
client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-01"
)
model = "gpt-4o-mini"


# Título y encabezado de la aplicación
st.title("Aplicación de Resumen y Respuesta de Correos Electrónicos")
st.subheader("¡Bienvenido a la aplicación web de Resumen y Respuesta de Correos Electrónicos!")

# Crear un área de texto para ingresar un email
email_text = st.text_area("Ingresa el email:", "")

# Función para generar el resumen
def generate_summary(email_text):
    prompt = f"Resume este email: {email_text}"
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": "Eres un asistente."},
                  {"role": "user", "content": prompt}],
        temperature=0,
    )
    summary = response.choices[0].message.content
    return summary

# Función para generar la respuesta
def generate_answer(email_text):
    prompt = f"Responde este email: {email_text}"
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": "Eres un asistente."},
                  {"role": "user", "content": prompt}],
        temperature=0,
    )
    answer = response.choices[0].message.content
    return answer

# Verifica si hay texto en el email
if email_text:
    col1, col2 = st.columns(2)
    response = ''
    with col1:
        if st.button("Resumen", use_container_width=True):
            with st.spinner("Generando resumen..."):
                response = generate_summary(email_text)
                st.success("Resumen generado correctamente!")
                time.sleep(1)
            
    with col2:
        if st.button("Respuesta", use_container_width=True):
            with st.spinner("Generando respuesta..."):
                response = generate_answer(email_text)
                st.success("Respuesta generada correctamente!")
                time.sleep(1)

    if response:    
        st.write(response)

        # Botón para reiniciar o limpiar respuesta
        if st.button("Empezar de nuevo", use_container_width=True):
            email_text = ""  # Limpiar el campo de texto
            response = None  # Limpiar la respuesta
            st.experimental_rerun()

else:
    st.write("🤔 ¡¿Qué pasa amigo?! No has escrito nada. ¡Escribe un email! ✨")

