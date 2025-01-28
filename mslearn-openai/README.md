# Azure OpenAI Exercises

Este repositorio contiene una serie de **prácticas de Microsoft Learn** que te permiten aprender a trabajar con **Azure OpenAI Service**. A través de estos ejercicios, podrás integrar y utilizar modelos de lenguaje de OpenAI en tus aplicaciones, mejorar la interacción con los usuarios, y aplicar tecnologías avanzadas como **Generación Aumentada por Recuperación (RAG)**, generación de imágenes con **DALL-E**, y la automatización de la creación y mejora de código. Los ejercicios están diseñados para ayudarte a dominar la implementación de modelos de OpenAI en diferentes escenarios, mejorando la precisión y relevancia de las respuestas y proporcionando una experiencia más dinámica e inteligente en tus proyectos.

## Requisitos

- **Azure OpenAI Service**: Acceso a los modelos de OpenAI.
- **Azure AI Search**: Para implementar RAG y mejorar la precisión de las respuestas.
- **Python** (opcional): Recomendado para interactuar con las APIs, pero también puedes usar otros lenguajes.

## Instrucciones

1. **Clona el Repositorio**

```bash
git clone <URL_DEL_REPOSITORIO>
```

### Configura el Archivo `.env`

Agrega tus credenciales de **Azure OpenAI** y **Azure AI Search** en un archivo `.env`:
```bash
AZURE_OAI_KEY = "<tu_clave_de_openai>"
AZURE_OAI_ENDPOINT = "<tu_endpoint_de_openai>"
AZURE_OAI_DEPLOYMENT = "<tu_nombre_de_despliegue>"
AZURE_SEARCH_KEY = "<tu_clave_de_search>"
AZURE_SEARCH_ENDPOINT = "<tu_endpoint_de_search>"
AZURE_SEARCH_INDEX = "<tu_indice_de_search>"
```

### Ejecuta el Programa

Inicia los ejercicios ejecutando el siguiente comando:
```bash
python <nombre_del_ejercicio>.py
```


## Conclusión

Estos ejercicios proporcionan una guía práctica para implementar **Azure OpenAI** en tus aplicaciones, mejorando la generación de contenido, la interacción con los usuarios y la automatización de procesos complejos. Al completar estos proyectos, podrás aprovechar las capacidades de **OpenAI** para desarrollar soluciones más inteligentes y eficientes.
