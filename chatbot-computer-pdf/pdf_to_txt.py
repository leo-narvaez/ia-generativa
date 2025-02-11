import os
import re
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
from dotenv import load_dotenv

# Cargar las credenciales de Azure desde el archivo .env
load_dotenv()

# Configurar el cliente de Azure Form Recognizer
key = os.getenv("AZURE_FORM_RECOGNIZER_KEY")
endpoint = os.getenv("AZURE_FORM_RECOGNIZER_ENDPOINT")
form_recognizer_client = DocumentAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# Carpeta de entrada y salida
INPUT_FOLDER = "files"
OUTPUT_FOLDER = "outputs"

# Crear la carpeta de salida si no existe
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def extract_and_format_data_from_pdf(file_path, form_recognizer_client):
    with open(file_path, "rb") as file:
        poller = form_recognizer_client.begin_analyze_document("prebuilt-document", file)
        result = poller.result()

    # Variables para almacenar los datos extraídos
    product_name = ""
    product_code = ""
    price = ""
    description = ""
    warranty = ""
    components = {}
    observations = ""
    
    # Procesamos las páginas del documento
    for page in result.pages:
        page_text = "\n".join([line.content for line in page.lines])

        # Extraer el nombre del producto (justo debajo del e-mail)
        if not product_name:
            email_position = page_text.find("e-mail:")
            if email_position != -1:
                product_name_match = re.search(r"e-mail:\s*(.*?)(?=Código:)", page_text[email_position:])
                if product_name_match:
                    product_name = product_name_match.group(1).strip()

        # Extraer el código de producto
        if not product_code:
            code_match = re.search(r"Código\s*[:\-]?\s*(\S+)", page_text)
            if code_match:
                product_code = code_match.group(1).strip()

        # Extraer el precio (por ejemplo: "2.130,00 €")
        if not price:
            price_match = re.search(r"(\d{1,3}(?:\.\d{3})*,\d{2} €)", page_text)
            if price_match:
                price = price_match.group(1).strip()

        # Extraer la descripción (todo lo que esté entre el nombre del producto y la garantía)
        if not description:
            description_match = re.search(r"Resistente a test militares\s*(.*?)Garantía\s*[:\-]?", page_text, re.DOTALL)
            if description_match:
                description = description_match.group(1).strip()

        # Extraer la garantía
        if not warranty:
            warranty_match = re.search(r"(?<=Garantía\s*[:\-]?\s*)\d+meses", page_text)
            if warranty_match:
                warranty = warranty_match.group(0).strip()

        # Extraer los componentes técnicos (procesador, RAM, etc.)
        component_patterns = {
            "disco_duro": r"Disco\s*duro\s*[:\-]?\s*(\S+)",
            "grafica": r"Gráfica\s*[:\-]?\s*(\S+)",
            "procesador": r"Familia\s*Procesador\s*[:\-]?\s*(\S.+?)(?=\n)",
            "pantalla": r"Tamaño\s*pantalla\s*[:\-]?\s*(\d+\s?[A-Za-z]+)",
            "ram": r"RAM\s*Instalada\s*[:\-]?\s*(\S+)",
            "bateria": r"Duración\s*de\s*la\s*batería\s*[:\-]?\s*(\S+)",
            "conexiones": r"Ethernet\s*[:\-]?\s*(\S+)",
        }

        for key, pattern in component_patterns.items():
            match = re.search(pattern, page_text)
            if match:
                components[key] = match.group(1).strip()

        # Extraer las observaciones (todo lo que venga después de "Opciones")
        if not observations:
            observations_match = re.search(r"Opciones\s*(.*)", page_text, re.DOTALL)
            if observations_match:
                observations = observations_match.group(1).strip()

    # Organizar y retornar toda la información estructurada
    structured_text = f"Nombre del Producto: {product_name}\n"
    structured_text += f"Código de Producto: {product_code}\n"
    structured_text += f"Precio: {price}\n"
    structured_text += f"Descripción del Producto: {description}\n"
    structured_text += f"Garantía: {warranty}\n\n"
    
    # Agregar componentes técnicos
    structured_text += "Componentes:\n"
    for key, value in components.items():
        structured_text += f"{key.capitalize()}: {value}\n"
    
    structured_text += f"\nObservaciones:\n{observations}\n"

    return structured_text


# Función para procesar todos los PDFs de la carpeta "files" y guardarlos en "outputs"
def process_pdfs(form_recognizer_client):
    # Listar los archivos PDF en la carpeta "files"
    pdf_files = [f for f in os.listdir(INPUT_FOLDER) if f.endswith('.pdf')]

    # Procesar cada archivo PDF
    for pdf_file in pdf_files:
        pdf_path = os.path.join(INPUT_FOLDER, pdf_file)

        # Extraer el texto del PDF usando Form Recognizer
        print(f"Extrayendo texto de {pdf_file}...")
        extracted_text = extract_and_format_data_from_pdf(pdf_path, form_recognizer_client)

        # Guardar el texto extraído en un archivo .txt
        txt_filename = os.path.splitext(pdf_file)[0] + ".txt"  # Cambiar extensión a .txt
        txt_path = os.path.join(OUTPUT_FOLDER, txt_filename)

        with open(txt_path, "w", encoding="utf-8") as txt_file:
            txt_file.write(extracted_text)

        print(f"Texto guardado en {txt_path}")


# Ejecutar la función
process_pdfs(form_recognizer_client)
