# Proyecto: Generación y Mejora de Código con Azure OpenAI Service

## Descripción
Este proyecto utiliza los modelos de **Azure OpenAI Service** para generar y mejorar código mediante prompts en lenguaje natural. Los modelos de OpenAI pueden:

- **Generar código** a partir de descripciones en lenguaje natural.
- **Corregir errores** en código ya escrito.
- **Agregar comentarios explicativos** en el código generado.
- **Explicar y simplificar** el código existente para facilitar su comprensión y mejora.

Este proyecto está orientado a facilitar tareas de desarrollo mediante el uso de la inteligencia artificial, ayudando a los desarrolladores a ser más eficientes y a optimizar sus flujos de trabajo.

## Objetivo
El objetivo principal de este ejercicio es explorar cómo los desarrolladores pueden usar la inteligencia artificial para hacer que tareas de programación como generación, corrección y documentación del código sean más fáciles y rápidas. Las técnicas utilizadas en este proyecto son aplicables a una amplia variedad de lenguajes de programación y escenarios de uso.

## Tecnologías Utilizadas
- **Azure OpenAI Service**: Para generar, mejorar y explicar el código.
- **Python (opcional)**: Lenguaje recomendado para interactuar con la API de OpenAI. _Se puede usar con otros lenguajes_
  
## Funcionamiento
El modelo de OpenAI puede generar código automáticamente a partir de un **prompt en lenguaje natural**, corregir errores en el código existente, explicar su propósito y funcionamiento para facilitar su comprensión, y agregar comentarios para mejorar la legibilidad y documentación, todo de manera eficiente.

## Cómo Usar

**Instalar Dependencias**  
Para usar este proyecto, asegúrate de tener las dependencias necesarias instaladas. Si estás usando Python, puedes instalar las librerías requeridas ejecutando:

```bash
pip install -r requirements.txt
```
## Configuración de Azure OpenAI
Asegúrate de tener una cuenta de Azure y una clave de API para acceder a los modelos de OpenAI. Configura tu entorno para que pueda comunicarse con la API.

## Cargar credenciales
Crea un archivo `.env` en la raíz de tu proyecto y agrega las siguientes líneas con tus credenciales de Azure:

```makefile
AZURE_OAI_KEY = ""
AZURE_OAI_ENDPOINT = ""
AZURE_OAI_DEPLOYMENT = ""
```
## Ejecuta el programa

```bash
python code-generation.py
```


1. **Elige la opción 1** para agregar comentarios a tu código e ingresa el siguiente prompt. Ten en cuenta que la respuesta podría tardar unos segundos en cada una de estas tareas.
```bash
Add comments to the following function. Return only the commented code.
```

2. **Luego, elige la opción 2** para escribir pruebas unitarias para esa misma función e ingresa el siguiente prompt.

```bash
Write four unit tests for the following function.
```

3. **Por último, elige la opción 3** para corregir errores en una aplicación para jugar Go Fish. Ingresa el siguiente prompt.

```bash
Fix the code below for an app to play Go Fish with the user. Return only the corrected code.
```

Los resultados reemplazarán lo que estaba en `result/app.txt`, y deberían mostrar un código muy similar pero con algunas correcciones.

