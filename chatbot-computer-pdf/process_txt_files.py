import os
import re
from db_sqlite import save_to_db

page_text = 'outputs/16Z90R-E.AD78B.txt'

def extract_and_format_data_from_txt(page_text):
    # Inicializar un diccionario para almacenar los detalles extraídos
    details = {}

    # Buscar el nombre del producto, que está justo después de la línea con el e-mail
    product_name_match = re.search(r"e-mail:\s*([^\n]+)\s*\n(.*?)(?=\d{1,3}(?:\.\d{3})*,\d{2} €)", page_text, re.DOTALL)
    if product_name_match:
        details['product_name'] = product_name_match.group(2).strip()

    # Buscar el código del producto
    code_match = re.search(r"Código:\s*(\S+)", page_text)
    if code_match:
        details['product_code'] = code_match.group(1).strip()

    # Buscar el precio del producto (formato de precio en euros)
    price_match = re.search(r"(\d{1,3}(?:\.\d{3})*,\d{2} €)", page_text)
    if price_match:
        details['price'] = price_match.group(1).strip()

    # Buscar la descripción del producto
    description_match = re.search(r"Resistente a test militares(.*?)(?=Garantía)", page_text, re.DOTALL)
    if description_match:
        details['description'] = description_match.group(1).strip()

    # Buscar la garantía
    warranty_match = re.search(r"Garantía\s*:\s*(\d{1,2}meses)", page_text)
    if warranty_match:
        details['warranty'] = warranty_match.group(1).strip()

    # Buscar los componentes del producto (DISCO DURO, GRÁFICA, etc.)
    components = {
        'hard_drive': r"DISCO DURO\s*(.*?)\s*(?=GRÁFICA)",
        'graphics': r"GRÁFICA\s*(.*?)\s*(?=PROCESADOR)",
        'processor': r"PROCESADOR\s*(.*?)\s*(?=PANTALLA)",
        'screen': r"PANTALLA\s*(.*?)\s*(?=DIMENSIONES)",
        'dimensions_and_weight': r"DIMENSIONES & PESO\s*(.*?)\s*(?=GENERAL)",
        'connections': r"CONEXIONES\s*(.*?)\s*(?=RAM)",
        'ram': r"RAM\s*(.*?)\s*(?=UNIDADES ÓPTICAS)",
        'audio': r"AUDIO\s*(.*?)\s*(?=BATERÍA)",
        'battery': r"BATERÍA\s*(.*?)\s*(?=WEBCAM)",
        'webcam': r"WEBCAM\s*(.*?)\s*(?=SOLUCIONES)",
        'os_and_software': r"SISTEMA OPERATIVO & SOFTWARE\s*(.*?)\s*(?=Opciones)"
    }

    for component, pattern in components.items():
        component_match = re.search(pattern, page_text, re.DOTALL)
        if component_match:
            details[component] = component_match.group(1).strip()

    # Buscar observaciones (parte final después de "Opciones")
    observations_match = re.search(r"Opciones(.*)", page_text, re.DOTALL)
    if observations_match:
        details['observations'] = observations_match.group(1).strip()

    # Formatear la salida para guardarla en un archivo .txt
    formatted_text = ""
    for key, value in details.items():
        formatted_text += f"\n{key.capitalize()}: {value}\n\n"
    print(formatted_text)
    return formatted_text

TEXT_FOLDER = "outputs"
# Procesar todos los archivos .txt
def process_text_files():
    # Listar los archivos .txt en la carpeta de salida
    txt_files = [f for f in os.listdir(TEXT_FOLDER) if f.endswith('.txt')]

    # Procesar cada archivo .txt
    for txt_file in txt_files:
        txt_path = os.path.join(TEXT_FOLDER, txt_file)

        # Leer el contenido del archivo .txt
        with open(txt_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Extraer los detalles del ordenador
        details = extract_and_format_data_from_txt(text)

        # Guardar los detalles en la base de datos
        save_to_db(details)
        #print(f"Detalles del producto {details} guardados en la base de datos.")

# Ejecutar el procesamiento
process_text_files()
