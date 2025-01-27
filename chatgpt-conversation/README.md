# ChatGPT Conversation Management with Azure OpenAI

Este proyecto tiene como objetivo gestionar las interacciones y el historial de conversaciones con el modelo ChatGPT utilizando el servicio de Azure OpenAI. Permite personalizar el comportamiento del modelo y optimizar el uso de los tokens a través de diferentes estrategias.

## Descripción

El proyecto demuestra cómo configurar y gestionar las conversaciones con el modelo ChatGPT, manteniendo un control eficiente sobre el número de tokens utilizados y el historial de mensajes. A través de una serie de funciones y ejercicios, se muestran varias maneras de interactuar con el modelo de manera creativa y eficiente. Algunas de las funcionalidades clave incluyen:

- **Gestión de Tokens**: Calcula el número de tokens generados en cada mensaje y asegura que se mantenga dentro de los límites del modelo.
- **Personalización del Asistente**: Permite modificar el comportamiento del modelo, como el rol del asistente (por ejemplo, "analista financiero experto" o "asistente creativo").
- **Control de la Historia de la Conversación**: Administra la longitud de la conversación mediante dos estrategias: mantener la conversación dentro de un número máximo de tokens o limitar la cantidad de turnos en la conversación.
- **Ajuste de Creatividad**: Permite ajustar la creatividad de las respuestas mediante la configuración de la temperatura, lo que afecta el estilo y la variabilidad de las respuestas generadas.
- **Cambio de Tono**: Configura el tono de las respuestas, como respuestas humorísticas o formales, según sea necesario.
- **Ejercicios Prácticos**: Incluye ejercicios que permiten personalizar aún más el modelo, como resumir mensajes anteriores o generar ideas creativas para startups.

## Objetivos del Proyecto

- Mostrar cómo gestionar conversaciones con el modelo de manera eficiente, teniendo en cuenta los límites de tokens.
- Permitir personalizar el comportamiento de ChatGPT a través de la modificación de mensajes del sistema y el ajuste de parámetros como la temperatura.
- Ofrecer ejemplos prácticos que permitan entender cómo manejar la historia de la conversación y la personalización del modelo según el contexto.

## Requisitos

Este proyecto requiere una cuenta de Azure y acceso a la API de Azure OpenAI. Se deben configurar las variables de entorno para autenticar el acceso y gestionar los recursos de la API.

## Configuración Inicial

Antes de empezar a trabajar con los ejercicios, es necesario configurar tu entorno. Crea un archivo `.env` en la raíz del proyecto y agrega las siguientes variables de entorno:

```bash
AZURE_OPENAI_API_KEY = <tu_clave_api>
AZURE_OPENAI_ENDPOINT = <tu_endpoint_de_azure>
```

## Uso

- El proyecto puede utilizarse para crear asistentes personalizados basados en ChatGPT para tareas específicas, como la redacción de contenido, asistencia técnica o análisis financiero.
- Permite optimizar la interacción con el modelo, asegurando un uso eficiente de los recursos y manteniendo conversaciones fluidas y dentro de los límites de tokens.

## Contribuciones

Se invita a los usuarios a contribuir al proyecto a través de *pull requests* o sugerencias para mejorar su funcionalidad y flexibilidad.
