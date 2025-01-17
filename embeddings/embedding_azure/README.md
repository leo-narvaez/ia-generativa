# Descripción del Notebook

Este notebook demuestra cómo trabajar con embeddings utilizando el servicio Azure OpenAI. A continuación se describen las principales tareas que se realizan en el notebook:

- **Generación de embeddings**: Se crea un embedding de texto utilizando el servicio de Azure OpenAI para representar de forma numérica frases o documentos.
- **Cálculo de similitudes entre frases**: Se genera un embedding para varias frases y se calcula la similitud entre ellas utilizando la similitud coseno.
- **Reducción de dimensionalidad y visualización de embeddings**: Se reduce la dimensionalidad de los embeddings utilizando PCA para visualizar la relación entre los textos en un espacio 2D.
- **Detección de temas con clustering**: Se agrupan los textos en clústeres basados en sus embeddings utilizando el algoritmo K-means.
- **Construcción de un motor de búsqueda simple con embeddings**: Se implementa un motor de búsqueda que encuentra el texto más similar a una consulta basada en embeddings.

## Requisitos

Para ejecutar este notebook, necesitas instalar las siguientes dependencias. Puedes instalarlas de forma individual o usando el archivo `requirements.txt`.

- **Instalar desde `requirements.txt`**: Este archivo contiene todas las librerías necesarias para ejecutar el notebook.
```bash
pip install -r requirements.txt
```
- **Instalar librerías individualmente**: Si prefieres instalar las librerías manualmente, puedes hacerlo utilizando pip.
```bash
pip install openai python-dotenv azure-identity
```
## Configuración

Antes de ejecutar el notebook, es necesario configurar las siguientes variables en un archivo `.env`:

```bash
AZURE_OPENAI_API_KEY = "your-api-key"
AZURE_OPENAI_ENDPOINT = "your-azure-openai-endpoint"
```

## Notas

Este notebook utiliza la API de Azure OpenAI para generar embeddings de texto. Asegúrate de tener acceso a la API de Azure y una clave API válida para poder ejecutar el código correctamente.

Asegúrate también de crear una implementación de un modelo para embeddings en el Azure OpenAI Studio, y usa el nombre del modelo desplegado en el parámetro correspondiente dentro del código.
