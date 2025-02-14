import streamlit as st
import json
import os

# Ruta al archivo JSON donde se almacenan los productos
PRODUCTS_JSON_PATH = 'data/products.json'

# Función para cargar los productos desde el archivo JSON
def cargar_productos():
    if os.path.exists(PRODUCTS_JSON_PATH):
        with open(PRODUCTS_JSON_PATH, 'r') as f:
            return json.load(f)
    return []

# Función para guardar los productos en el archivo JSON
def guardar_productos(productos):
    with open(PRODUCTS_JSON_PATH, 'w') as f:
        json.dump(productos, f, indent=4)

# Función para agregar un nuevo producto
def agregar_producto():
    st.subheader("Agregar nuevo producto")

    nombre = st.text_input("Nombre del producto")
    descripcion = st.text_area("Descripción del producto")
    precio = st.number_input("Precio", min_value=0.0, format="%.2f")
    imagen = st.text_input("URL de la imagen")
    caracteristicas = st.text_area("Características del producto")
    
    if st.button("Agregar producto"):
        if nombre and descripcion and precio and imagen:
            producto_nuevo = {
                "nombre": nombre,
                "descripcion": descripcion,
                "precio": precio,
                "imagen": imagen,
                "caracteristicas": caracteristicas.split("\n")
            }

            productos = cargar_productos()
            productos.append(producto_nuevo)
            guardar_productos(productos)
            st.success("Producto agregado exitosamente.")
        else:
            st.error("Todos los campos son obligatorios.")

# Función para editar un producto existente
def editar_producto():
    st.subheader("Editar producto existente")

    productos = cargar_productos()
    productos_nombres = [producto['nombre'] for producto in productos]

    # Selección del producto a editar
    producto_seleccionado = st.selectbox("Selecciona un producto", productos_nombres)

    if producto_seleccionado:
        producto = next(prod for prod in productos if prod['nombre'] == producto_seleccionado)

        nombre = st.text_input("Nombre del producto", producto['nombre'])
        descripcion = st.text_area("Descripción del producto", producto['descripcion'])
        precio = st.number_input("Precio", min_value=0.0, value=producto['precio'], format="%.2f")
        imagen = st.text_input("URL de la imagen", producto['imagen'])
        caracteristicas = st.text_area("Características del producto", "\n".join(producto['caracteristicas']))

        if st.button("Actualizar producto"):
            producto['nombre'] = nombre
            producto['descripcion'] = descripcion
            producto['precio'] = precio
            producto['imagen'] = imagen
            producto['caracteristicas'] = caracteristicas.split("\n")

            # Guardamos los cambios
            guardar_productos(productos)
            st.success(f"Producto '{nombre}' actualizado exitosamente.")

# Función para eliminar un producto
def eliminar_producto():
    st.subheader("Eliminar producto")

    productos = cargar_productos()
    productos_nombres = [producto['nombre'] for producto in productos]

    # Selección del producto a eliminar
    producto_seleccionado = st.selectbox("Selecciona un producto a eliminar", productos_nombres)

    if st.button("Eliminar producto"):
        if producto_seleccionado:
            productos = [producto for producto in productos if producto['nombre'] != producto_seleccionado]
            guardar_productos(productos)
            st.success(f"Producto '{producto_seleccionado}' eliminado exitosamente.")
        else:
            st.error("No se seleccionó ningún producto.")

# Función que muestra el panel de administración de productos
def admin_products():
    st.title("Gestión de productos")

    menu = ["Agregar producto", "Editar producto", "Eliminar producto"]
    seleccion = st.selectbox("Selecciona una acción", menu)

    if seleccion == "Agregar producto":
        agregar_producto()
    elif seleccion == "Editar producto":
        editar_producto()
    elif seleccion == "Eliminar producto":
        eliminar_producto()
