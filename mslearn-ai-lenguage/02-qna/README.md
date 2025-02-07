# MotoBot - Chatbot de MotoGP 🏍️💨

**MotoBot** es un chatbot interactivo que proporciona respuestas rápidas y precisas sobre MotoGP. Utilizando el poder de la inteligencia artificial, este bot puede responder preguntas relacionadas con el campeonato, el calendario de carreras, pilotos, equipos y mucho más. ¡Es tu fuente instantánea de sabiduría sobre MotoGP!

[Accede a MotoBot aquí](https://motobot.streamlit.app/)

### Funcionalidades

- **Respuestas rápidas** a preguntas frecuentes sobre MotoGP, como:
  - Tabla de clasificación del campeonato.
  - Calendario de grandes premios.
  - Información sobre pilotos y equipos.
  
- **Interacción dinámica** a través de una interfaz sencilla, donde puedes escribir tu pregunta y obtener respuestas generadas automáticamente.

### Herramientas y Tecnologías Utilizadas

Este proyecto hace uso de varias herramientas avanzadas de **Azure** para mejorar la experiencia del usuario, incluyendo la integración con **Azure Cognitive Services** para el procesamiento de lenguaje natural y la obtención de respuestas inteligentes.

#### Azure SDKs Utilizados

- **AzureKeyCredential**: Para la autenticación segura con los servicios de Azure.
- **QuestionAnsweringClient**: Para acceder al servicio de Preguntas y Respuestas, que permite realizar consultas sobre datos preentrenados para obtener respuestas precisas.
- **TextAnalyticsClient**: Para analizar el sentimiento del texto y obtener insights adicionales sobre las interacciones del usuario.

```python
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.questionanswering import QuestionAnsweringClient
from azure.ai.textanalytics import TextAnalyticsClient
```
### Instalación

Para ejecutar este proyecto localmente, asegúrate de tener Python 3.7+ y los siguientes paquetes instalados.

1. Clona este repositorio:
   ```bash
   git clone https://github.com/leo-narvaez/ia-generativa/tree/main/mslearn-ai-lenguage/02-qna
   cd motobot
   ```
2. Crea un entorno virtual:
   - En Linux/macOS:
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```
   - En Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configura las credenciales de Azure (asegúrate de tener una cuenta de Azure y haber creado los recursos de AI):
   - **AI_SERVICE_ENDPOINT**: El endpoint de tu servicio Azure.
   - **AI_SERVICE_KEY**: La clave de tu servicio Azure.
   - **QA_PROJECT_NAME**: El nombre del proyecto de preguntas y respuestas en Azure.
   - **QA_DEPLOYMENT_NAME**: El nombre del despliegue de tu servicio.

   Puedes establecer estas variables de entorno en un archivo `.env` o directamente en tu entorno de ejecución. Un ejemplo del archivo `.env` sería:
```bash
# .env

AI_SERVICE_ENDPOINT=https://<tu_endpoint_de_azure>
AI_SERVICE_KEY=<tu_clave_de_azure>
QA_PROJECT_NAME=<nombre_de_tu_proyecto>
QA_DEPLOYMENT_NAME=<nombre_de_tu_despliegue>

```
5. Ejecuta la aplicación:
```bash
streamlit run app.py
```
