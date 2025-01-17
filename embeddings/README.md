# Proyecto de Ejemplos de Embeddings

Este repositorio contiene varios notebooks que demuestran cómo trabajar con embeddings de texto en diferentes contextos utilizando APIs como OpenAI y Azure OpenAI. A continuación se presentan los tres notebooks principales que se abordan en el proyecto:

## 1. [Ejemplo de Embeddings](https://github.com/leo-narvaez/ia-generativa/tree/main/embeddings/embedding_basic)

Este notebook aborda varias tareas comunes en el procesamiento de lenguaje natural (NLP) utilizando embeddings de texto generados por una API como OpenAI. Las tareas incluyen la comparación de similitud entre frases, clasificación de texto, visualización de embeddings en 2D mediante PCA, y la búsqueda de texto similar en una base de datos de embeddings.

## 2. [Embedding con Azure OpenAI](https://github.com/leo-narvaez/ia-generativa/tree/main/embeddings/embedding_azure)

Este notebook demuestra cómo trabajar con embeddings utilizando el servicio Azure OpenAI. Incluye la generación de embeddings, el cálculo de similitudes entre frases, reducción de dimensionalidad con PCA, detección de temas mediante clustering, y la construcción de un motor de búsqueda simple basado en embeddings.

## 3. [Embedding de Textos Largos](https://github.com/leo-narvaez/ia-generativa/tree/main/embeddings/embedding_long)

Este notebook muestra cómo manejar textos que superan la longitud máxima de contexto de los modelos de embedding de OpenAI. Proporciona dos soluciones principales: truncar el texto a la longitud máxima permitida y dividir el texto en fragmentos más pequeños, embebiendo cada fragmento de forma independiente.
