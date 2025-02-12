import json

def generar_json_azure(data):
    documentos = []
    
    for product_code, product_data in data['products'].items():
        # El texto completo del producto
        texto = product_data['product_name'] + '\n' + product_data.get('description', '') + '\n' + product_data.get('price', '') + '\n' + product_data.get('observations', '')
        
        # Las anotaciones de las entidades
        anotaciones = []
        
        # Asignar las entidades al texto con su respectiva posición
        
        # Extract product name
        start_pos = texto.find(product_data['product_name'])
        end_pos = start_pos + len(product_data['product_name'])
        anotaciones.append({
            "regionOffset": start_pos,
            "regionLength": end_pos - start_pos,
            "labels": [{"category": "Marca"}]  # Etiqueta de la entidad
        })
        
        # Extract product code
        start_pos = texto.find(product_data['product_code'])
        end_pos = start_pos + len(product_data['product_code'])
        anotaciones.append({
            "regionOffset": start_pos,
            "regionLength": end_pos - start_pos,
            "labels": [{"category": "Modelo"}]
        })
        
        # Extract price
        start_pos = texto.find(product_data.get('price', ''))
        end_pos = start_pos + len(product_data.get('price', ''))
        anotaciones.append({
            "regionOffset": start_pos,
            "regionLength": end_pos - start_pos,
            "labels": [{"category": "precio"}]
        })
        
        # Extract warranty (if exists)
        warranty = product_data.get('warranty', '')
        if warranty:
            start_pos = texto.find(warranty)
            end_pos = start_pos + len(warranty)
            anotaciones.append({
                "regionOffset": start_pos,
                "regionLength": end_pos - start_pos,
                "labels": [{"category": "Garantia"}]
            })
        
        # Extract description (if exists)
        description = product_data.get('description', '')
        if description:
            start_pos = texto.find(description)
            end_pos = start_pos + len(description)
            anotaciones.append({
                "regionOffset": start_pos,
                "regionLength": end_pos - start_pos,
                "labels": [{"category": "Descripción"}]
            })
        
        # Similar extraction for other fields like processor, RAM, etc.
        processor = product_data.get('processor', '')
        if processor:
            start_pos = texto.find(processor)
            end_pos = start_pos + len(processor)
            anotaciones.append({
                "regionOffset": start_pos,
                "regionLength": end_pos - start_pos,
                "labels": [{"category": "Procesador"}]
            })
        
        ram = product_data.get('ram', '')
        if ram:
            start_pos = texto.find(ram)
            end_pos = start_pos + len(ram)
            anotaciones.append({
                "regionOffset": start_pos,
                "regionLength": end_pos - start_pos,
                "labels": [{"category": "Memoria RAM"}]
            })
        
        # Build the document for Azure NER training
        document = {
            "location": f"{product_code}.txt",  # Puedes cambiar el nombre o usar un identificador único
            "language": "es",
            "entities": anotaciones
        }
        
        documentos.append(document)

    # Generate final JSON format for Azure
    json_output = {
        "projectFileVersion": "2022-10-01-preview",
        "stringIndexType": "Utf16CodeUnit",
        "metadata": {
            "projectKind": "CustomEntityRecognition",
            "storageInputContainerName": "compubot",  # Asegúrate de que esto sea correcto
            "settings": {
                "confidenceThreshold": 0
            },
            "projectName": "compubot",
            "multilingual": True,
            "description": "",
            "language": "es"
        },
        "assets": {
            "projectKind": "CustomEntityRecognition",
            "entities": [
                {"category": "Marca"},
                {"category": "Modelo"},
                {"category": "Procesador"},
                {"category": "Memoria RAM"},
                {"category": "Disco Duro"},
                {"category": "Grafica"},
                {"category": "Pantalla"},
                {"category": "Sistema Operativo"},
                {"category": "Garantia"},
                {"category": "Bateria"},
                {"category": "precio"}
            ],
            "documents": documentos
        }
    }

    # Save the final JSON file
    with open('json_outputs/azure_training_data.json', 'w', encoding='utf-8') as f:
        json.dump(json_output, f, ensure_ascii=False, indent=4)

# Load the products from the JSON file
json_file_path = 'json_outputs/products.json'
with open(json_file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Generate the JSON file for Azure NER training
generar_json_azure(data)
