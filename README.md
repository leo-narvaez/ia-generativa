# IA Generativa

Este repositorio contiene una colección de proyectos prácticos relacionados con la inteligencia artificial generativa, incluyendo ejemplos de preprocesamiento de texto y la integración de modelos OpenAI a través de servicios como Azure.

## Proyectos

### [Preprocesamiento de Texto para Modelos de OpenAI](https://github.com/leo-narvaez/ia-generativa/tree/main/preprocessing)
Este proyecto incluye ejemplos prácticos para realizar preprocesamiento de texto antes de enviar datos a modelos de OpenAI. El preprocesamiento adecuado es fundamental para obtener mejores resultados y evitar problemas de procesamiento de datos, como la inclusión de palabras inapropiadas, caracteres no deseados o textos que superen los límites de tokens del modelo.

### [Integración de Azure OpenAI con un Chatbot](https://github.com/leo-narvaez/ia-generativa/tree/main/quickstart-openai)
Este proyecto muestra cómo integrar Azure OpenAI con un chatbot utilizando el modelo GPT-3.5 Turbo y GPT-4. Se aprovechan las características avanzadas del servicio de Azure y se incluyen mejoras para personalizar la interacción, registrar las conversaciones y facilitar el uso del asistente.

### [Guardrail para Detectar Alucinaciones en Respuestas de Modelos de Lenguaje](https://github.com/leo-narvaez/ia-generativa/tree/main/hallucination)
Este proyecto se enfoca en la creación de un guardrail de salida que verifica las respuestas generadas por modelos de lenguaje (LLMs) para detectar alucinaciones, es decir, respuestas incorrectas o inventadas. A través de un enfoque basado en un conjunto de evaluación robusto, se definen criterios específicos para identificar alucinaciones en las respuestas del modelo.

### [Exploración de Capacidades de Modelos de OpenAI](https://github.com/leo-narvaez/ia-generativa/tree/main/sdk-python/notebook)
Este proyecto proporciona ejercicios prácticos para explorar diversas funcionalidades de los modelos de OpenAI, como la experimentación con prompts, comparación de similitudes entre textos, tokenización, generación de texto en tiempo real, y análisis de emociones. Los usuarios podrán aprender a utilizar estos modelos en tareas de procesamiento de lenguaje natural, incluyendo la evaluación de similitudes semánticas, extracción de palabras clave y generación de resúmenes.

### [Aplicación de Resumen y Respuesta de Correos Electrónicos](https://github.com/leo-narvaez/ia-generativa/tree/main/email_app)  
Este proyecto presenta una aplicación web que utiliza **GPT-4** de OpenAI para generar resúmenes y respuestas automáticas para correos electrónicos. Desarrollada con **Streamlit**, permite a los usuarios ingresar un correo, generar un resumen o una respuesta sugerida, y reiniciar el proceso fácilmente. La aplicación está configurada para funcionar con la API de Azure OpenAI y ofrece una experiencia de usuario sencilla y eficiente.


## Requisitos

Asegúrate de contar con los siguientes requisitos antes de ejecutar los proyectos:

- [Python 3.x](https://www.python.org/downloads/)
- Dependencias necesarias (detalladas en cada subproyecto).

## Instalación

Para instalar y configurar los proyectos, sigue las instrucciones de cada carpeta de proyecto individual.

1. Clona el repositorio:
 ```bash
   git clone https://github.com/leo-narvaez/ia-generativa.git
 ```
2. Navega al proyecto deseado y sigue las instrucciones dentro de cada subdirectorio.

## Contribuciones

Las contribuciones son bienvenidas. Si tienes una idea o mejora, por favor abre un "issue" o crea un "pull request". Asegúrate de seguir las guías de estilo y las buenas prácticas del código.

## Licencia

Este proyecto está bajo la licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.
