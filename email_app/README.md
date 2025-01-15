# Aplicación de Resumen y Respuesta de Correos Electrónicos

## Descripción

Aplicación web para generar resúmenes y respuestas automáticas a correos electrónicos utilizando **GPT-4** de OpenAI. Desarrollada con **Streamlit**, la aplicación permite generar un resumen o respuesta para cualquier correo que ingreses y ofrece la posibilidad de reiniciar el proceso.

## Requisitos

- Python 3.7+
- Bibliotecas: `streamlit`, `openai`, `python-dotenv`

Instala las dependencias con:
```bash
pip install streamlit openai python-dotenv
```
o
```bash
pip install -r requirements.txt
```

## Configuración

1. **Obten tus claves de API de Azure OpenAI** y cópialas.
2. Crea un archivo `.env` en el directorio principal con el siguiente contenido:
```bash
AZURE_OPENAI_ENDPOINT=<tu_endpoint_de_azure> 
AZURE_OPENAI_API_KEY=<tu_api_key_de_azure>
```
## Ejecución

1. Navega al directorio del proyecto.
2. Ejecuta la aplicación con:

```bash
streamlit run app.py
```


## Uso

1. Ingresa el texto de un correo en el campo proporcionado.
2. Haz clic en **Resumen** o **Respuesta** para generar el contenido deseado.
3. Después de generar la respuesta o resumen, puedes hacer clic en **Empezar de nuevo** para reiniciar.

## Estructura del Proyecto

- **app.py**: Código de la aplicación.
- **.env**: Archivo para las credenciales de la API.
- **requirements.txt**: Dependencias del proyecto.

## Contribuciones

1. Haz un fork del repositorio.
2. Crea una rama con tus cambios (`git checkout -b feature/mi-nueva-caracteristica`).
3. Haz commit y push a tu rama.
4. Crea un Pull Request para revisión.

## Licencia

Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
