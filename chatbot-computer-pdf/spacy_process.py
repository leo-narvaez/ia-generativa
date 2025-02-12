import spacy
from spacy.training import Example
import random
import json
import re

# Cargar los productos desde el archivo JSON
json_file_path = "json_outputs/products.json"

with open(json_file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Crear ejemplos de entrenamiento compatibles con spaCy v3
def create_training_example(product_code, product_data):
    text = f"{product_data['product_name']}, {product_data['processor']}, {product_data['ram']}, {product_data['price']}"
    
    # Verificar si hay garantía
    if 'warranty' in product_data:
        text += f", {product_data['warranty']}"
    
    # Etiquetas de entidades
    entities = []

    # Producto: product_name
    start = text.find(product_data['product_name'])
    end = start + len(product_data['product_name'])
    entities.append((start, end, "PRODUCT_NAME"))

    # Precio: price
    price_match = re.search(r"\d{1,3}(?:\.\d{3})*,\d{2} €", text)
    if price_match:
        start = price_match.start()
        end = price_match.end()
        entities.append((start, end, "PRICE"))

    # RAM: ram
    ram_match = re.search(r"\d+GB", text)
    if ram_match:
        start = ram_match.start()
        end = ram_match.end()
        entities.append((start, end, "RAM"))

    # Procesador: processor
    start = text.find(product_data['processor'])
    end = start + len(product_data['processor'])
    entities.append((start, end, "PROCESSOR"))

    # Garantía: warranty (solo si existe en los datos)
    if 'warranty' in product_data:
        warranty_match = re.search(r"\d+ meses", text)
        if warranty_match:
            start = warranty_match.start()
            end = warranty_match.end()
            entities.append((start, end, "WARRANTY"))

    # Crear el ejemplo de entrenamiento
    return (text, {"entities": entities})

# Generar los datos de entrenamiento
TRAINING_DATA = []
for product_code, product_data in data["products"].items():
    training_example = create_training_example(product_code, product_data)
    TRAINING_DATA.append(training_example)

# Crear un objeto de spaCy
nlp = spacy.blank("es")

# Crear el componente NER si no existe
if "ner" not in nlp.pipe_names:
    ner = nlp.create_pipe("ner")
    nlp.add_pipe(ner, last=True)
else:
    ner = nlp.get_pipe("ner")

# Añadir las etiquetas al componente NER
for example in TRAINING_DATA:
    for _, annotations in example:
        for ent in annotations.get("entities"):
            ner.add_label(ent[2])

# Entrenar el modelo
optimizer = nlp.begin_training()
for epoch in range(10):
    random.shuffle(TRAINING_DATA)
    losses = {}
    for text, annotations in TRAINING_DATA:
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, annotations)
        nlp.update([example], drop=0.5, losses=losses)
    print(f"Epoch {epoch}, Losses: {losses}")

# Guardar el modelo entrenado
nlp.to_disk("custom_ner_model")
