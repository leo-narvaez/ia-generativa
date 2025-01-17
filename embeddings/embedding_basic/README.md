# Ejemplo de Embeddings

Este notebook aborda varias tareas comunes en el procesamiento de lenguaje natural (NLP) utilizando embeddings de texto generados por una API como OpenAI. Los siguientes son los principales objetivos del notebook:

- **Comparar la similitud entre dos frases usando embeddings**: Se calculan los embeddings de dos frases y se mide su similitud utilizando la similitud coseno.
- **Clasificación de texto simple usando embeddings**: Se entrenan clasificadores utilizando embeddings para categorizar textos en diferentes clases, como "positivo" o "negativo".
- **Visualización de embeddings en 2D usando PCA**: Los embeddings generados se proyectan en un espacio 2D utilizando el análisis de componentes principales (PCA) para facilitar su visualización.
- **Búsqueda de texto similar en una base de datos de embeddings**: Se busca el texto más cercano a una consulta específica dentro de una base de datos de documentos utilizando similitud coseno.

## Requisitos


Puedes instalar las dependencias necesarias utilizando el archivo `requirements.txt` o instalarlas individualmente:

- Instalar desde `requirements.txt`: Este archivo contiene todas las librerías necesarias para ejecutar el notebook.
```bash
pip install -r requirements.txt
```
- **Instalar librerías individualmente**: Si prefieres instalar las librerías manualmente, puedes hacerlo utilizando pip.
```bash
pip install requests openai numpy scikit-learn matplotlib 
```
## Configuración

Dentro del archivo `config.json` debes ajustar los siguientes valores para que el notebook funcione correctamente:

```json
{
    "EMBEDDINGS_MODEL": "text-embedding-ada-002",
    "OPENAI_API_BASE": "",
    "OPENAI_API_KEY": "",
    "OPENAI_API_VERSION": "2022-12-01"
}
```
Asegúrate de completar los valores para la clave API y la URL de la API para poder interactuar con el servicio correctamente.
