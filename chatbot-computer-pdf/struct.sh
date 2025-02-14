#!/bin/bash

# Crear la carpeta principal del proyecto
mkdir -p botnology/app
mkdir -p botnology/data
mkdir -p botnology/admin
mkdir -p botnology/gpt
mkdir -p botnology/files
mkdir -p botnology/files/pdf
mkdir -p botnology/files/txt
mkdir -p botnology/files/json
mkdir -p botnology/files/output

# Crear los archivos necesarios dentro de la carpeta "app"
touch botnology/app/__init__.py
touch botnology/app/home.py
touch botnology/app/product.py
touch botnology/app/login.py
touch botnology/app/dashboard.py
touch botnology/app/utils.py

# Crear archivos necesarios para la administración
touch botnology/admin/__init__.py
touch botnology/admin/clean_txt.py
touch botnology/admin/extract_pdf.py
touch botnology/admin/azure_project.py

# Crear archivos sobre gpt
touch botnology/gpt/__init__.py
touch botnology/gpt/gpt_35.py

# Crear el archivo principal para ejecutar Streamlit
touch botnology/app.py

# Crear el archivo de dependencias
touch requirements.txt

# Archivos de datos
touch botnology/data/products.json
touch botnology/admin/db_sqlite.py

# Mensaje de éxito
echo "Estructura de carpetas y archivos creada exitosamente."
