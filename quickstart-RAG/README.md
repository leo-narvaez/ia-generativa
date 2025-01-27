# Funcionamiento

Este proyecto está diseñado para demostrar cómo integrar escenarios de *Retrieval-Augmented Generation* (RAG) utilizando **Azure AI Search** y **Azure OpenAI**. El objetivo principal es crear una experiencia de chat que se apoya en los datos almacenados en un índice de búsqueda en Azure, mejorando las respuestas del modelo con información específica de esos datos.

## Flujo Básico

1. **Azure AI Search**: Se utiliza un índice de búsqueda que contiene datos simples (como información de hoteles) en forma de texto plano. Este índice se puede crear rápidamente utilizando un servicio de Azure AI Search en un nivel básico o superior. El índice incluye características como la clasificación semántica, que ayuda a mejorar la relevancia de las búsquedas.

2. **Azure OpenAI**: Un modelo de lenguaje generativo (como GPT-4 o GPT-4 mini) se usa para generar respuestas en función de las consultas de los usuarios. En este caso, el modelo toma la información de búsqueda de **Azure AI Search** y la usa para proporcionar respuestas más precisas y contextualizadas a las preguntas que se le hacen.

3. **Sin Vectores ni Embeddings**: En este caso de ejemplo, no se utilizan vectores ni técnicas de *embedding*, lo que simplifica la integración. Aunque los vectores son más efectivos para escenarios RAG complejos, en este caso se opta por un enfoque más sencillo usando solo texto.

## Flujo de Trabajo

- Un usuario hace una consulta al modelo de chat.
- El sistema envía la consulta a **Azure AI Search** para buscar información relevante.
- **Azure OpenAI** recibe la consulta y la información de búsqueda y genera una respuesta mejorada y más precisa.

Este enfoque proporciona una experiencia de chat donde las respuestas se enriquecen con datos adicionales, sin necesidad de procesar vectores o embeddings, lo que lo hace más accesible para implementaciones rápidas.

Este es un punto de partida, y a medida que se adquiere más experiencia, se pueden añadir características avanzadas como vectores y consultas híbridas para mejorar aún más el rendimiento y la relevancia de las respuestas.
