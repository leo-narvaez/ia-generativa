# Proyecto: Implementación de Generación Aumentada por Recuperación (RAG) con Azure OpenAI Service

## Descripción
Este proyecto explora la implementación de **Generación Aumentada por Recuperación (RAG)** utilizando el **Azure OpenAI Service**. Con Azure OpenAI, es posible combinar la potencia de los modelos de lenguaje preentrenados con datos personalizados, lo que permite generar respuestas más precisas y relevantes a partir de información propia. En este escenario, el desarrollador actuará como parte del equipo de **Margie’s Travel Agency**, donde se utilizarán datos internos para mejorar las respuestas generadas por el modelo OpenAI, mediante la integración con **Azure AI Search** para indexar y recuperar datos.

El modelo RAG permite enriquecer las respuestas de OpenAI al permitirle acceder y utilizar datos específicos de la agencia de viajes, lo que resulta en respuestas más contextualizadas y alineadas con la información interna.

## Objetivo
El objetivo principal de este ejercicio es enseñar cómo **integrar Azure AI Search** con **Azure OpenAI** para mejorar la generación de contenido mediante la recuperación de datos relevantes. A través de este enfoque, las aplicaciones pueden obtener resultados más precisos y específicos para casos de uso personalizados, como recomendaciones de viajes basadas en información propia.

## Tecnologías Utilizadas
- **Azure OpenAI Service**: Para generar respuestas basadas en lenguaje natural utilizando modelos de OpenAI.
- **Azure AI Search**: Para indexar y recuperar datos relevantes personalizados.
- **Python (opcional)**: Lenguaje recomendado para interactuar con las APIs de Azure y OpenAI.

## Funcionamiento
El proceso de RAG combina la recuperación de información relevante (desde una base de datos o sistema de indexación) con la generación de respuestas a partir de esa información utilizando el modelo OpenAI. Al utilizar **Azure AI Search**, se pueden indexar grandes cantidades de datos internos de Margie’s Travel Agency (por ejemplo, información sobre destinos, ofertas y preguntas frecuentes), y luego hacer que el modelo OpenAI recupere esta información para generar respuestas contextuales.

### Flujo de Trabajo
1. **Indexar datos**: Los datos relevantes de la agencia de viajes (por ejemplo, destinos, promociones o información sobre servicios) se cargan en **Azure AI Search**.
2. **Realizar la consulta**: El usuario realiza una consulta, por ejemplo, sobre destinos turísticos.
3. **Recuperación de información**: Azure AI Search recupera los datos pertinentes de la base de datos indexada.
4. **Generación de respuesta**: Usando los datos recuperados, el modelo de OpenAI genera una respuesta que integra tanto la información de la base de datos como el contexto general aprendido durante el entrenamiento del modelo.

## Cómo Usar

### 1. **Instalar Dependencias**  
Para usar este proyecto, asegúrate de tener las dependencias necesarias instaladas. Si estás usando Python, puedes instalar las librerías requeridas ejecutando:

```bash
pip install -r requirements.txt
```

### 2. Configurar Azure OpenAI y Azure AI Search

Asegúrate de tener cuentas y claves API tanto para **Azure OpenAI** como para **Azure AI Search**. Configura tu entorno para que pueda comunicarse con ambos servicios.

### Configuración de Azure OpenAI

Crea un archivo `.env` en la raíz de tu proyecto y agrega las siguientes líneas con tus credenciales de Azure:

```bash
AZURE_OAI_ENDPOINT=<endpoint>
AZURE_OAI_KEY=<key>
AZURE_OAI_DEPLOYMENT=<deployment_name>
AZURE_SEARCH_ENDPOINT=<search_endpoint>
AZURE_SEARCH_KEY=<search_key>
AZURE_SEARCH_INDEX=<search_index>
```


### 3. Indexar Datos en Azure AI Search

Carga los datos relevantes de **Margie’s Travel Agency** en **Azure AI Search**. Esto puede incluir información sobre destinos turísticos, paquetes especiales, ofertas de viaje y más. Asegúrate de que los datos estén bien estructurados para facilitar su búsqueda y recuperación.

### 4. Ejecutar el Programa

Una vez que tengas todo configurado, ejecuta el siguiente comando para iniciar la integración:

```bash
python ownData.py
```
Ejemplo de ejecución:
```bash
$ python ownData.py

Enter a question:
tell me about london
...Sending the following request to Azure OpenAI endpoint...
Request: tell me about london

Response: London is the capital and most populous city of England and the United Kingdom, located on the River Thames in the southeast of Great Britain. Founded by the Romans, it was originally named Londinium and has been a major settlement for over two millennia. The ancient core of London, known as the City of London, retains its medieval boundaries of 1.12 square miles. 
....
```

### 5. Mostrar Resultados

Los resultados generados por la IA se mostrarán en la interfaz de usuario de la aplicación, combinando la información recuperada de **Azure AI Search** con la generación de OpenAI.

### 6. Ajustar la Configuración

Puedes ajustar el proceso de integración según sea necesario, añadiendo más datos a la base de **Azure AI Search** o modificando los prompts para cambiar el tipo de recomendaciones generadas.

## Conclusión

Este proyecto te permitirá crear una aplicación inteligente y personalizada utilizando **Generación Aumentada por Recuperación (RAG)** con **Azure OpenAI** y **Azure AI Search**. Al combinar datos propios con el poder de los modelos de lenguaje, puedes generar respuestas más precisas y útiles para tus usuarios, lo que mejora la experiencia de servicios como agencias de viajes, asistencia al cliente y más.

La integración de estas tecnologías avanzadas proporcionará una solución robusta para recuperar y generar contenido contextualizado, permitiendo aplicaciones más eficientes y centradas en el usuario.


