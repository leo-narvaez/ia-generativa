# Embedding de textos más largos que la longitud máxima del contexto del modelo

Este notebook muestra cómo manejar textos que superan la longitud máxima de contexto de los modelos de embedding de OpenAI, específicamente utilizando el modelo `text-embedding-ada-002`. Proporciona dos soluciones principales para gestionar textos largos: truncar el texto y dividirlo en fragmentos.

## Descripción

En este notebook, exploraremos cómo gestionar textos que exceden el límite máximo de tokens de un modelo de OpenAI. Para ello, implementaremos dos enfoques principales:

1. **Truncar el texto**: Reducir el texto de entrada a la longitud máxima permitida en tokens.
2. **Dividir el texto en fragmentos**: Dividir el texto en fragmentos más pequeños y embeder cada uno de estos fragmentos por separado.

## Requisitos

Es necesario instalar las siguientes dependencias para ejecutar el notebook:

```bash
pip install openai tenacity tiktoken matplotlib scikit-learn
```
## Configuración

Antes de ejecutar el notebook, es necesario configurar las siguientes variables en un archivo `.env`:

```bash
AZURE_OPENAI_API_KEY = "your-api-key"
AZURE_OPENAI_ENDPOINT = "your-azure-openai-endpoint"
```
## Conclusión

Este notebook ofrece soluciones para manejar textos largos que exceden el límite de tokens de los modelos de OpenAI. Se abordan dos enfoques: truncamiento, que ajusta el texto al límite máximo, y fragmentación, que divide el texto en partes más pequeñas para preservar su significado. Ambas técnicas permiten trabajar con textos extensos de manera eficiente sin perder calidad en los embeddings generados.

