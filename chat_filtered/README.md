# Filtrado de Contenido en Chats con Azure OpenAI

Este proyecto muestra cómo integrar el filtrado de contenido en los resultados de los chats utilizando el servicio **Azure OpenAI**. Se utiliza el modelo GPT-4 y su capacidad de filtrar respuestas en base a diferentes categorías para evitar contenido inapropiado o sensible.

## Descripción

El filtrado de contenido es una característica importante del servicio Azure OpenAI que permite verificar si una solicitud o respuesta generada contiene contenido sensible, ofensivo o peligroso. En este proyecto, se realiza una prueba de filtrado de contenido para observar cómo el sistema categoriza y maneja los resultados, identificando qué respuestas están "filtradas" y su nivel de **severidad**.

## Requisitos

Asegúrate de tener las siguientes dependencias instaladas:

- **openai**: Para interactuar con la API de OpenAI.

Puedes instalar las dependencias necesarias con el siguiente comando:

```bash
pip install openai
```
o 
```bash
pip install -r requirements.txt
```

## Configuración

1. **Obten las claves de API de Azure OpenAI**:
   - Dirígete a [Azure OpenAI](https://azure.microsoft.com/en-us/services/cognitive-services/openai/) y crea una instancia de la API de OpenAI.
   - Copia el **Endpoint** y la **API Key**.

2. **Configura las variables de entorno**:
   Crea un archivo `.env` en el directorio del proyecto con tus credenciales de Azure:


## Cómo ejecutar

Este proyecto está diseñado para ejecutarse en un notebook. Puedes probar las funcionalidades directamente en tu entorno de Jupyter o Google Colab. A continuación, se muestran los pasos esenciales para ejecutar el código:

1. **Cargar las librerías y configuraciones**:
- Importa las librerías necesarias y configura tu clave de API de OpenAI.

2. **Realizar una consulta de chat**:
- Envía una pregunta o un mensaje general al modelo GPT-4 utilizando el siguiente código:

```bash
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What are the benefits of exercising regularly?"}
]
completion = client.chat.completions.create(
    model=deployment,
    messages=messages
)
print(f"Answer: {completion.choices[0].message.content}")
```

3. **Filtrado de contenido en los resultados**:
- Extrae los resultados del filtro de contenido del prompt y la respuesta generada para analizar qué categorías fueron filtradas y su severidad.

```bash
# prompt content filter result in "model_extra" for azure
prompt_filter_result = completion.model_extra["prompt_filter_results"][0]["content_filter_results"]
print("\nPrompt content filter results:")
for category, details in prompt_filter_result.items():
    filtered = details.get('filtered', 'N/A')
    severity = details.get('severity', 'N/A')
    print(f"{category}:\n filtered={filtered}\n severity={severity}")

# completion content filter result
print("\nCompletion content filter results:")
completion_filter_result = completion.choices[0].model_extra["content_filter_results"]
for category, details in completion_filter_result.items():
    filtered = details.get('filtered', 'N/A')
    severity = details.get('severity', 'N/A')
    print(f"{category}:\n filtered={filtered}\n severity={severity}")
```

## ¿Qué hace este código?

- **Envía una consulta** a la API de Azure OpenAI con un mensaje general del usuario (en este caso, sobre los beneficios del ejercicio).
- **Genera una respuesta** y verifica si la respuesta y el prompt cumplen con los criterios de filtrado de contenido establecidos por el modelo.
- **Extrae los resultados** del filtrado, incluyendo las categorías de contenido y su severidad (por ejemplo, "violencia", "lenguaje ofensivo", etc.).
- **Imprime los resultados del filtrado** para el **prompt** y la **respuesta**, mostrando si han sido filtrados y el nivel de severidad.

## ¿Por qué es importante el filtrado de contenido?

El filtrado de contenido ayuda a evitar que los modelos generen respuestas que puedan ser inapropiadas, ofensivas o peligrosas. Azure OpenAI proporciona un sistema de filtrado que clasifica el contenido en categorías como:

- **Violencia**
- **Lenguaje ofensivo**
- **Contenido para adultos**
- **Discriminación**
- **Otras categorías**

El sistema determina si el contenido debe ser bloqueado o si se permite, en función de su severidad.

## Contribuciones

Si deseas contribuir al proyecto:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadí una nueva característica'`).
4. Haz push a tu rama (`git push origin feature/nueva-caracteristica`).
5. Abre un Pull Request para revisión.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
