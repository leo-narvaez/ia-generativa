import json
import os

# Ruta del archivo JSON con los productos
json_file_path = "json_outputs/products.json"

# Cargar el archivo JSON de productos
with open(json_file_path, 'r', encoding='utf-8') as f:
    products_data = json.load(f)

# Función para dividir los valores por saltos de línea y asignar labels
def split_value_into_labels(value):
    return [line.strip() for line in value.split('\n') if line.strip()]

# Carpeta de salida para los archivos .txt
output_folder = "outputs_clean"
os.makedirs(output_folder, exist_ok=True)  # Crea la carpeta si no existe

# Iterar sobre los productos y procesar los datos
for product_code, product_info in products_data['products'].items():
    # Crear el nombre del archivo .txt
    file_name = f"{product_code}.txt"
    file_path = os.path.join(output_folder, file_name)

    # Abrir el archivo para escritura
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(f"Entidad y Etiquetas para el Producto: {product_code}\n")
        file.write("=" * 50 + "\n")

        # Iterar sobre cada clave del producto y escribir las entidades y sus etiquetas
        for key, value in product_info.items():
            if isinstance(value, str):
                # Si el valor es una cadena, separar por saltos de línea y crear etiquetas
                labels = split_value_into_labels(value)
                file.write(f"\nEntidad: {key}\n")
                file.write("Etiquetas:\n")
                for idx, label in enumerate(labels, start=1):
                    file.write(f"- {label}\n")
                file.write("-" * 50 + "\n")

print(f"Archivos .txt generados en la carpeta '{output_folder}'")
