# Guardrail para Detectar Alucinaciones en las Respuestas de Modelos de Lenguaje

## Visión General

Un **guardrail** es un conjunto de reglas y verificaciones diseñadas para asegurar que las salidas de un modelo de lenguaje grande (LLM) sean precisas, apropiadas y estén alineadas con las expectativas del usuario. Los guardrails son esenciales para mantener la fiabilidad de los LLMs, asegurando que generen respuestas significativas y confiables.

En este notebook, vamos a desarrollar un **guardrail de salida** que específicamente verifica las respuestas del modelo en busca de **alucinaciones**—instancias en las que el modelo genera información incorrecta o inventada.

Para más información sobre cómo desarrollar guardrails, puedes consultar esta [guía sobre el desarrollo de guardrails](https://cookbook.openai.com/examples/how_to_use_guardrails).

## Objetivos

Este notebook se centrará en los siguientes puntos clave:

1. **Construcción de un Conjunto de Evaluación Fuerte**: Crearemos un conjunto robusto de datos de evaluación para probar las salidas del modelo.
2. **Definición de Criterios para Detectar Alucinaciones**: Definiremos criterios específicos para medir las alucinaciones en las respuestas del modelo.
3. **Mejora de la Precisión del Guardrail con Prompts de Pocas Ejemplos**: Utilizaremos el aprendizaje con pocos ejemplos para mejorar la precisión del guardrail que detecta alucinaciones.

## Enfoque

Seguiremos un enfoque sistemático para crear y evaluar el guardrail:

### 1. Construcción de un Conjunto de Evaluación Fuerte
   - Crearemos un conjunto de datos de interacciones que incluya consultas de usuarios y respuestas esperadas del modelo.
   - Esto nos permitirá probar la capacidad del modelo para responder correctamente y detectar alucinaciones.

### 2. Definición de Criterios para Alucinaciones
   - Definiremos criterios específicos para determinar si una respuesta contiene alucinaciones. Esto puede incluir la verificación de la precisión fáctica, relevancia y cumplimiento con la política.
   
### 3. Uso de Prompts de Pocas Ejemplos
   - Utilizando ejemplos con pocos disparadores, guiaremos al modelo para generar respuestas más confiables y precisas.

## Proceso

### Paso 1: Definir Criterios de Evaluación

Definimos criterios específicos de evaluación para detectar alucinaciones basados en varios factores, como:
- **Precisión Fáctica**: Si la información en la respuesta es correcta.
- **Relevancia**: La relevancia de la respuesta con respecto a la consulta del usuario.
- **Cumplimiento de Políticas**: Si la respuesta se ajusta a las pautas y políticas predefinidas.
- **Coherencia Contextual**: Si la respuesta tiene sentido en el contexto dado.

### Paso 2: Implementar Guardrail para Detectar Alucinaciones

Desarrollamos un guardrail que evalúa las respuestas del modelo basándose en estos criterios. Para cada respuesta, el guardrail asigna una puntuación y marca aquellas respuestas que puedan contener alucinaciones.

### Paso 3: Evaluación y Resultados

Aplicamos este guardrail a un conjunto de interacciones de ejemplo y evaluamos su efectividad para detectar alucinaciones. Los resultados incluyen métricas de precisión y recall para evaluar el rendimiento del guardrail.

## Ejemplo de Salida

La siguiente tabla muestra el resultado de aplicar el guardrail a algunas interacciones de ejemplo:

| Preciso | Alucinación | Artículo KB | Historial de Chat | Respuesta del Asistente |
|---------|-------------|-------------|-------------------|-------------------------|
| Verdadero | Aprobado   | 1. **Reconocimiento Inicial** - Saludar al cliente cálidamente y agradecerle por ponerse en contacto. | [{'role': 'user', 'content': 'Quería dar mi opinión sobre la nueva licuadora que compré.'}, {'role': 'assistant', 'content': '¡Gracias por ponerte en contacto! Apreciamos mucho tu comentario. ¿Podrías darnos detalles específicos sobre la licuadora? ¿Qué aspectos te gustaría comentar y tienes alguna sugerencia de mejora?'}] | {'role': 'assistant', 'content': '¡Gracias por tus amables palabras sobre el diseño! Enviaré tu sugerencia sobre el ruido del motor a nuestro equipo de desarrollo de productos para su revisión. ¿Hay algo más en lo que te pueda asistir hoy?'} |
| Verdadero | Aprobado   | 1. **Determinar el tipo de consulta del cliente** - Identificar el problema del cliente y clasificarlo. | [{'role': 'user', 'content': '¿Me puedes hablar de tu política de devoluciones?'}] | {'role': 'assistant', 'content': 'Una vez tenga más detalles sobre el problema, podré proporcionarte la información relevante acerca de nuestra política de devoluciones.'} |

### Métricas de Evaluación

- **Precisión**: 1.00
  - La precisión mide la proporción de verdaderos positivos correctamente identificados entre todas las instancias predichas como positivas.
  
- **Recall**: 1.00
  - El recall mide la proporción de verdaderos positivos correctamente identificados entre todas las instancias positivas reales en el conjunto de datos.

Estos resultados indican que el guardrail ha logrado una precisión y recall perfectos, detectando las alucinaciones con un 100% de exactitud en este conjunto de evaluación.

## Conclusión

En este notebook, hemos demostrado cómo crear y aplicar un guardrail para detectar alucinaciones en las respuestas de un LLM. Al construir un conjunto de evaluación fuerte, definir criterios claros para las alucinaciones y utilizar prompting de pocos ejemplos, hemos podido desarrollar un guardrail preciso y efectivo.

Este enfoque se puede extender a otros tipos de salidas y puede integrarse en sistemas de producción para asegurar que los LLMs proporcionen información confiable, precisa y relevante.
