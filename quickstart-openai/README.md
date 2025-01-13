# Chatbot con Azure OpenAI

Este proyecto muestra cómo integrar Azure OpenAI con un chatbot utilizando el modelo GPT-3.5 Turbo y GPT-4, aprovechando las características avanzadas del servicio de Azure. Además, hemos realizado algunas mejoras para personalizar la interacción, registrar las conversaciones y facilitar el uso del asistente.

## Descripción

En este repositorio, hemos creado un chatbot que utiliza la API de Azure OpenAI para generar respuestas conversacionales en tiempo real. El código permite la interacción con el modelo GPT-3.5 Turbo o GPT-4, y tiene algunas mejoras adicionales, como:

- **Interacción continua**: El bot puede mantener una conversación con el usuario, añadiendo cada nuevo mensaje al historial.
- **Registro de conversación**: Los mensajes del sistema, usuario y asistente se almacenan en un archivo de log con la fecha y hora, lo que facilita el seguimiento de la interacción.
- **Configuración simplificada**: Se utiliza un archivo `.env` para almacenar las credenciales de Azure OpenAI de manera segura, evitando exponer las claves directamente en el código.

## Requisitos

Antes de empezar, asegúrate de tener lo siguiente instalado en tu entorno:

- **Python 3.7+**
- **Paquete `openai`**: Para interactuar con el servicio de Azure OpenAI.
- **Paquete `python-dotenv`**: Para manejar las credenciales de Azure OpenAI desde un archivo `.env`.
- **Una cuenta de Azure con acceso a OpenAI**: Necesitarás las credenciales de Azure, específicamente el `API_KEY` y el `ENDPOINT`.

## Instalación

### 1. Crear y Configurar el Entorno Virtual

Si aún no has configurado un entorno virtual, puedes hacerlo siguiendo estos pasos:
```bash
# Crear un entorno virtual

python -m venv venv
# Activar el entorno virtual
# En Windows:
venv\Scripts\activate

# En Linux/macOS:
source venv/bin/activate
```
### 2. Instalar las Dependencias

Con el entorno virtual activo, instala las bibliotecas necesarias utilizando el archivo `requirements.txt`:
```bash
# Si tienes un archivo `requirements.txt` con las dependencias
pip install -r requirements.txt

# Si no tienes el archivo `requirements.txt`, puedes instalar las dependencias manualmente:
pip install openai python-dotenv
```
Si `pip` no está instalado en tu entorno virtual, puedes instalarlo con:
```bash
# Asegúrate de que pip esté instalado
python -m ensurepip --upgrade
```
### 3. Crear el archivo `.env`

Crea un archivo llamado `.env` en la raíz de tu proyecto y agrega las siguientes variables con las credenciales de tu cuenta de Azure:
```bash
AZURE_OPENAI_ENDPOINT="https://<your-endpoint>"
AZURE_OPENAI_API_KEY="<your-api-key>"
```
Reemplaza `<your-endpoint>` y `<your-api-key>` con la información proporcionada por tu cuenta de Azure OpenAI.

## Uso

### 1. Código de Ejemplo

El código principal se encuentra en el archivo `quickstart.py`. A continuación, se describe su funcionamiento.

### 2. Cómo Funciona

1. **Carga de Credenciales**: Utilizamos la librería `python-dotenv` para cargar las credenciales de Azure OpenAI desde un archivo `.env`. Esto garantiza que las claves no se expongan en el código fuente.

2. **Inicialización de la API de Azure OpenAI**: Configuramos el cliente de Azure OpenAI utilizando el endpoint y la clave de la API.

3. **Interacción con el Usuario**: El usuario puede interactuar con el modelo proporcionando entradas por consola. Estas entradas se envían a la API de OpenAI, y el modelo responde con un texto generado.

4. **Registro de la Conversación**: Cada mensaje del sistema, usuario y asistente se guarda en un archivo de log dentro de la carpeta `chatlogs`. El nombre del archivo incluye la fecha y la hora de la ejecución, lo que facilita el seguimiento de las interacciones.

### 3. Ejemplo de Ejecución

El código pedirá al usuario que ingrese un mensaje. A continuación, el modelo generará una respuesta y ambas interacciones se guardarán en el archivo `chatlogs/chat_log_2025-01-13_10-30-45.txt`.

Ejemplo de archivo de log:
```bash
[system]:
----
Eres un asistente virtual. Responde con amabilidad y claridad.

[user]:
----
Hola, ¿cómo estás?

[assistant]:
----
Estoy bien, gracias por preguntar. ¿Cómo te puedo ayudar hoy?

[user]:
----
¿Cuál es la capital de Japón?

[assistant]:
----
La capital de Japón es Tokio.
```
### 4. Salir de la Conversación

Si en cualquier momento deseas terminar la conversación, puedes escribir `salir`. El programa terminará y no agregará más mensajes al archivo de log.

## Mejoras Implementadas

- **Interacción continua**: El asistente recuerda todo el historial de la conversación, proporcionando respuestas más contextualizadas.
- **Registro de mensajes**: Todos los mensajes (system, user, assistant) se guardan en un archivo de texto para realizar un seguimiento detallado de las interacciones.
- **Formato de log claro**: Los logs se almacenan con formato claro y estructurado, lo que facilita la comprensión de la conversación.
- **Carga de credenciales segura**: Las credenciales se cargan desde un archivo `.env` para evitar exponerlas en el código.

## Conclusión

Este código es un ejemplo simple y práctico de cómo integrar Azure OpenAI con un chatbot utilizando GPT-3.5 Turbo o GPT-4. Con las mejoras implementadas, ahora puedes tener una conversación continua con el modelo, y todo el historial de la interacción se guarda en un archivo de log para futuras referencias.
