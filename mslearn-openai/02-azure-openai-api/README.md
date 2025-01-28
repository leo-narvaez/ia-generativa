# Proyecto: Recomendaciones de Senderismo con Azure OpenAI Service

## Descripción
Este proyecto utiliza el **Azure OpenAI Service** para implementar una aplicación de recomendaciones de senderismo que se basa en modelos de lenguaje generativo de OpenAI. El sistema puede generar, modificar y personalizar recomendaciones de rutas de senderismo a partir de entradas en lenguaje natural. Los modelos pueden:

- **Generar recomendaciones** de rutas de senderismo basadas en las preferencias del usuario.
- **Personalizar las rutas** según condiciones específicas como dificultad, duración, y ubicación.
- **Sugerir mejoras** en los planes de senderismo según el clima, la temporada y otros factores.
  
Este proyecto está diseñado para ayudar a los desarrolladores a integrar soluciones de IA generativa para mejorar la experiencia del usuario en aplicaciones móviles o web relacionadas con actividades al aire libre.

## Objetivo
El principal objetivo de este ejercicio es enseñar a los desarrolladores cómo usar las APIs de Azure OpenAI para crear aplicaciones interactivas que puedan generar recomendaciones basadas en lenguaje natural. A través de este ejercicio, los desarrolladores aprenderán cómo implementar un sistema de recomendaciones dinámico que se adapta a las solicitudes de los usuarios.

## Tecnologías Utilizadas
- **Azure OpenAI Service**: Para generar recomendaciones de senderismo basadas en texto.
- **Python (opcional)**: Lenguaje recomendado para interactuar con la API de OpenAI. _Se puede usar con otros lenguajes_.
- **API de Azure OpenAI**: Para conectar la aplicación con los modelos de OpenAI a través de la nube.

## Funcionamiento
Este proyecto utiliza un modelo de lenguaje entrenado de OpenAI para interactuar con los usuarios. Los usuarios pueden ingresar sus preferencias, como nivel de dificultad o ubicación, y el modelo generará recomendaciones personalizadas. Además, la aplicación permite a los desarrolladores ajustar los parámetros del modelo para satisfacer las necesidades específicas de su aplicación.

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

```bash
AZURE_OAI_KEY = ""
AZURE_OAI_ENDPOINT = ""
AZURE_OAI_DEPLOYMENT = ""
```

## Ejecuta el programa

1. **Configura la entrada del usuario**: La aplicación pedirá al usuario información sobre sus preferencias para las recomendaciones de senderismo. Un ejemplo de prompt podría ser:

```bash
¿Qué tipo de senderismo prefieres? (fácil, moderado, difícil)
```

2. **Genera recomendaciones**: Usando la respuesta del usuario, la aplicación enviará una solicitud a la API de OpenAI para obtener rutas recomendadas basadas en las preferencias ingresadas.

```bash
Genera recomendaciones de senderismo basadas en las siguientes preferencias: dificultad moderada, duración de 3 horas, en la región de los Alpes suizos.
```

3. **Ajusta y personaliza las recomendaciones**: Los resultados generados se mostrarán al usuario, permitiendo personalizar aún más la experiencia, como ajustar la ruta en función del clima o la temporada.

4. **Mostrar resultados**: Las recomendaciones generadas por la IA se mostrarán en la interfaz de usuario de la aplicación para que el usuario pueda tomar una decisión informada sobre qué ruta seguir.

Los resultados generados se almacenarán en un archivo `result/recommendations.txt`, donde el código de la recomendación será escrito en formato amigable para el usuario.

## Conclusión
Este proyecto te permitirá crear una aplicación de recomendaciones de senderismo inteligente, personalizada y dinámica utilizando las potentes herramientas que ofrece Azure OpenAI. La integración de estas tecnologías puede mejorar significativamente la experiencia de los usuarios al brindarles recomendaciones precisas y relevantes basadas en sus preferencias.
