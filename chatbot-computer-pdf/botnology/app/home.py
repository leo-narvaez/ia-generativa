import streamlit as st
import json

# Cargar los productos desde el archivo JSON con codificación UTF-8
def load_products():
    with open('data/products.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data['products']

def view_home():
    st.title("Bienvenido a BotNology")

    # Cargar los productos
    productos = load_products()

    # Mostrar los productos en un grid
    columnas = st.columns(3)  # Crear tres columnas para los productos

    # Mostrar productos en el grid
    for i, producto in enumerate(productos.values()):
        col = columnas[i % 3]
        with col:
            st.write(f"**{producto['product_name']}**")
            st.write(f"${producto['price']}")

            # Botón para ver detalles del producto
            if st.button(f"Ver detalles", key=f"btn_{i}"):
                st.session_state.producto_seleccionado = producto
                st.session_state.page = "detail"  # Cambiar el estado a "detalle"
                return  # Salir para no seguir mostrando más elementos de la vista de inicio

