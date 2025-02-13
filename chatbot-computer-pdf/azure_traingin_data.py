import json
import os
import re

# Carpeta de salida donde están los archivos .txt generados
output_folder = "outputs_clean"
json_output_folder = "json_outputs"  # Carpeta de salida para el JSON

# Crear la carpeta si no existe
if not os.path.exists(json_output_folder):
    os.makedirs(json_output_folder)

# Entidades que quieres identificar en los archivos
entities = [
    "product_name",
    "product_code",
    "price",
    "description",
    "warranty",
    "hard_drive",
    "graphics",
    "processor",
    "screen",
    "dimensions_and_weight",
    "connections",
    "ram",
    "audio",
    "battery",
    "webcam",
    "os_and_software"
]

# Crear el diccionario base para el proyecto con el formato que has solicitado
project_data = {
    "projectFileVersion": "2022-10-01-preview",
    "stringIndexType": "Utf16CodeUnit",
    "metadata": {
        "projectKind": "CustomEntityRecognition",
        "storageInputContainerName": "techbot",
        "settings": {
            "confidenceThreshold": 0
        },
        "projectName": "TechBotProject",
        "multilingual": True,
        "description": "",
        "language": "es"
    },
    "assets": {
        "projectKind": "CustomEntityRecognition",
        "entities": [{"category": entity} for entity in entities],
        "documents": []
    }
}

# Crear una lista para guardar los detalles de las etiquetas y sus offsets
offset_details = []

# Función para extraer las entidades y sus posiciones en un archivo de texto
def extract_entities_from_txt(txt_file_path):
    with open(txt_file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    document_entities = []
    region_length = len(text)  # Longitud total del documento
    entity_offsets = []  # Lista para hacer un seguimiento de los offsets

    # Lista para almacenar todas las etiquetas encontradas
    labels = []

    # Buscar todas las entidades y sus etiquetas en el archivo
    for entity in entities:
        # Buscar la sección que corresponde a la entidad y sus etiquetas
        pattern = re.compile(rf"Entidad:\s*{re.escape(entity)}\s*Etiquetas:\s*(-.*?)(?=Entidad:|$)", re.DOTALL)
        matches = re.finditer(pattern, text)  # Usar finditer para capturar todas las ocurrencias
        for match in matches:
            entity_text = match.group(1).strip().split("\n")
            # Encontramos la posición de las etiquetas
            etiquetas_inicio = match.group(0).find("Etiquetas:") + len("Etiquetas:")
            
            for label in entity_text:
                label = label.strip()
                # Ignorar líneas que consisten solo en guiones o espacios vacíos
                if "-" in label and len(set(label.strip())) == 1 or label == "":
                    continue

                if label:  # Asegurarse de que el valor no esté vacío
                    # Ahora, encontramos la posición de la etiqueta después de la palabra "Etiquetas:"
                    label_offset = text.find(label, etiquetas_inicio)  # Encontrar la posición inicial de la etiqueta, después de "Etiquetas:"
                    
                    # Ajuste para evitar solapamientos de offsets
                    while label_offset in entity_offsets:
                        # Saltar este valor de offset
                        label_offset = text.find(label, label_offset + 1)

                    # Añadir el offset ajustado a la lista de offsets
                    entity_offsets.append(label_offset)

                    # Añadir la etiqueta a las etiquetas del documento
                    labels.append({
                        "category": entity,
                        "offset": label_offset,
                        "length": len(label)
                    })

                    # Añadir la etiqueta, su offset y el texto extraído a los detalles (para el archivo adicional)
                    offset_details.append({
                        "entity": entity,
                        "label": label,
                        "offset": label_offset,
                        "extracted_text": text[label_offset:label_offset + len(label)],  # Extract the corresponding text
                    })

    # Si encontramos etiquetas en el documento, las añadimos a la lista de documentos
    if labels:
        # Asignar el primer offset encontrado de la primera etiqueta como "regionOffset"
        region_offset = labels[0]["offset"]
        print(f"Región de offset: {region_offset}")
        document_entities.append({
            "regionOffset": region_offset,
            "regionLength": region_length,
            "labels": labels
        })

        # Ahora agregamos el texto de la región entre region_offset y el offset de la etiqueta
        for detail in offset_details:
            # Asegurarse de que region_offset está definido
            detail["region_text"] = text[min(detail["offset"], region_offset):detail["offset"]]

    return document_entities

# Iterar sobre los archivos .txt generados y extraer las entidades
for txt_file in os.listdir(output_folder):
    if txt_file.endswith(".txt"):
        # Construir la ruta completa del archivo
        txt_file_path = os.path.join(output_folder, txt_file)

        # Extraer las entidades del archivo
        entities_in_document = extract_entities_from_txt(txt_file_path)

        # Crear el documento en la estructura requerida
        document_data = {
            "location": txt_file,
            "language": "es",
            "dataset": "Train",
            "entities": entities_in_document
        }

        # Añadir el documento a la lista de documentos
        project_data["assets"]["documents"].append(document_data)

# Guardar el JSON estructurado dentro de json_outputs/azure_training_data.json
output_json_path = os.path.join(json_output_folder, "azure_training_data.json")
with open(output_json_path, 'w', encoding='utf-8') as f:
    json.dump(project_data, f, ensure_ascii=False, indent=4)

# Guardar los detalles de las etiquetas y sus offsets en otro archivo JSON
offset_details_path = os.path.join(json_output_folder, "offset_details.json")
with open(offset_details_path, 'w', encoding='utf-8') as f:
    json.dump(offset_details, f, ensure_ascii=False, indent=4)

print(f"JSON de proyecto generado: {output_json_path}")
print(f"Archivo con los detalles de los offsets generado: {offset_details_path}")
