import streamlit as st
import json
import os

# Ruta al archivo JSON donde están los productos
JSON_FILE_PATH = "json_outputs/products.json"

# Cargar los productos desde el archivo JSON
def load_products():
    if os.path.exists(JSON_FILE_PATH):
        with open(JSON_FILE_PATH, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        return data.get("products", {})
    else:
        return {}

# Función para mostrar los productos en un grid
def display_products_grid(products):
    if not products:
        st.write("No se encontraron productos.")
    else:
        # Crear columnas para mostrar los productos en formato grid
        cols = st.columns(3)  # Ajusta este número según cuántos productos quieras mostrar por fila

        # Contador de columnas
        col_index = 0

        # Iterar sobre los productos y mostrarlos en un grid
        for product_code, details in products.items():
            # Cada producto se mostrará en una de las columnas
            with cols[col_index]:
                # Mostrar la imagen por defecto (puedes reemplazarla por una URL de imagen si tienes imágenes)
                st.image("https://media.idownloadblog.com/wp-content/uploads/2022/11/MacBook-desktop-macOS-Ventura.jpg", use_container_width =True)
                
                # Mostrar el nombre y precio del producto
                st.markdown(f"#### {details.get('product_name', 'Desconocido')}")
                st.write(f"**Precio:** {details.get('price', 'N/A')}")
            # Actualizar el índice de columna
            col_index += 1
            if col_index == 3:
                col_index = 0  # Resetear cuando se llegue al número máximo de columnas

# Configuración básica de la aplicación
def main():
    st.title("Listado de Productos")
    
    # Cargar los productos desde el archivo JSON
    products = load_products()
    
    # Mostrar los productos en formato grid
    display_products_grid(products)

if __name__ == "__main__":
    main()
