import os
import re
import fitz  # PyMuPDF para extraer texto de los PDFs
import json

from db_sqlite import save_to_db

TEXT_FOLDER = "outputs"
JSON_FOLDER = "json_outputs"
PDF_FOLDER = "files"

# Función para extraer texto de un PDF usando PyMuPDF
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text("text")
    return text

# Función para extraer y formatear los datos del PDF
def extract_and_format_data_from_pdf(pdf_path, page_text):
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
    description_match = re.search(r"(\d{1,3}(?:\.\d{3})*,\d{2} €)(.*?)(Garantía)", page_text, re.DOTALL)
    if description_match:
        details['description'] = description_match.group(2).strip()

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

    # Guardar los detalles extraídos en la base de datos
    save_to_db(details)

    # Guardar el archivo .txt y el archivo .json
    save_structured_files(details, pdf_path)
    return formatted_text

# Función para guardar el archivo .txt y .json
def save_structured_files(details, pdf_path):
    # Eliminar la extensión del PDF
    base_filename = os.path.splitext(os.path.basename(pdf_path))[0]
    
    # Asegurarse de que las carpetas existen
    if not os.path.exists(TEXT_FOLDER):
        os.makedirs(TEXT_FOLDER)
    if not os.path.exists(JSON_FOLDER):
        os.makedirs(JSON_FOLDER)
    
    # Guardar el archivo .txt
    txt_file_path = os.path.join(TEXT_FOLDER, f"{base_filename}.txt")
    with open(txt_file_path, 'w', encoding='utf-8') as file:
        for key, value in details.items():
            file.write(f"{key.capitalize()}: {value}\n\n")
    
    # Guardar el archivo .json
    json_file_path = os.path.join(JSON_FOLDER, "products.json")
    
    # Verificar si el archivo JSON ya existe y cargar su contenido
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
    else:
        data = {'products': {}}
    
    # Obtener el código del producto y agregarlo al diccionario global
    product_code = details.get('product_code')
    if product_code:
        data['products'][product_code] = details
    
    # Guardar todos los productos en el archivo JSON
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    
    print(f"Archivo guardado como: {txt_file_path} y {json_file_path}")

# Función para procesar los archivos PDF
def process_pdf_files():
    # Listar los archivos PDF en la carpeta "files"
    pdf_files = [f for f in os.listdir(PDF_FOLDER) if f.endswith('.pdf')]

    # Procesar cada archivo PDF
    for pdf_file in pdf_files:
        pdf_path = os.path.join(PDF_FOLDER, pdf_file)

        # Extraer el texto del PDF
        page_text = extract_text_from_pdf(pdf_path)

        # Extraer los detalles del producto
        details = extract_and_format_data_from_pdf(pdf_path, page_text)

# Ejecutar el procesamiento
process_pdf_files()
