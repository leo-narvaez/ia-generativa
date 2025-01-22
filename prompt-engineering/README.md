# Ejercicios de Ingeniería de Prompts

Este repositorio contiene varios ejercicios prácticos para aprender y practicar la ingeniería de prompts utilizando modelos de OpenAI. Para cada ejercicio, se te proporcionará un texto de entrada y un resultado esperado, y tu tarea será escribir el prompt adecuado para generar dicho resultado.

---

## Configuración Inicial

Antes de empezar a trabajar con los ejercicios, es necesario configurar tu entorno. Crea un archivo `.env` en la raíz del proyecto y agrega las siguientes variables de entorno:

```bash
AZURE_OPENAI_API_KEY = <tu_clave_api>
AZURE_OPENAI_ENDPOINT = <tu_endpoint_de_azure>
```
Estas variables son necesarias para autenticarte y utilizar la API de OpenAI a través de Azure.

## 1. Ejercicios de Ingeniería de Prompts
Este ejercicio está diseñado para que practiques cómo escribir prompts que generen resultados específicos utilizando los modelos de OpenAI. Aprenderás a estructurar tus entradas para obtener salidas como resúmenes, clasificaciones de texto o generación creativa.

[Enlace al proyecto: Ejercicio 1: Ingeniería de Prompts](https://github.com/leo-narvaez/ia-generativa/tree/main/prompt-engineering/prompt-engineering)

---

## 2. Control de la Salida del Modelo con Parámetros
En este proyecto, aprenderás cómo controlar la salida del modelo utilizando parámetros específicos, como temperature, top_p, y penalty de frecuencia. Estos parámetros permiten ajustar la creatividad y precisión de las respuestas generadas por los modelos de OpenAI.

[Enlace al proyecto: Ejercicio 2: Control de Parámetros](https://github.com/leo-narvaez/ia-generativa/tree/main/prompt-engineering/model-output-control)

---

## 3. Mejores Prácticas para la Ingeniería de Prompts
Aquí aprenderás las mejores prácticas para crear prompts efectivos. Esto incluye cómo usar delimitadores (como ### o comillas triples """) y cómo proporcionar ejemplos previos para mejorar la efectividad del modelo. También verás cómo estructurar las solicitudes para obtener resultados más precisos y relevantes.

[Enlace al proyecto: Ejercicio 3: Mejores Prácticas](https://github.com/leo-narvaez/ia-generativa/tree/main/prompt-engineering/best-practices)

---

## 4. Predicción con Emojis
En este ejercicio, te enfocarás en la predicción de emojis usando métodos de clasificación Zero-shot y Few-shot. A través de ejemplos, aprenderás a hacer que el modelo prediga emojis adecuados para el contexto emocional o temático de un mensaje, utilizando pocos ejemplos previos.

[Enlace al proyecto: Ejercicio 4: Predicción de Emojis](https://github.com/leo-narvaez/ia-generativa/tree/main/prompt-engineering/emoji-prediction)

---

## Conclusión
Estos ejercicios te proporcionarán las habilidades necesarias para trabajar con la API de OpenAI y crear prompts efectivos y personalizados para una variedad de tareas. Experimenta con diferentes configuraciones y parámetros para comprender cómo afectan la salida del modelo y cómo puedes utilizar estos conocimientos para aplicaciones prácticas.

Si tienes dudas o preguntas, no dudes en abrir un issue en el repositorio.
