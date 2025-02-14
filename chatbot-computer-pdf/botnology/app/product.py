import streamlit as st

def product_detail():
    # Verifica si hay un producto seleccionado en la sesión
    producto = st.session_state.get('producto_seleccionado', None)

    if producto:
        st.title(f"Detalles del producto: {producto['product_name']}")

        # Mostrar la descripción completa
        st.subheader("Descripción")
        descripcion = producto['description'].replace("\n", " <br> ")
        st.markdown(descripcion, unsafe_allow_html=True)

        # Mostrar las características adicionales
        st.subheader("Características")
        st.write(f"**Precio**: {producto['price']}")
        st.write(f"**Código del producto**: {producto['product_code']}")
        st.write(f"**Garantía**: {producto['warranty']}")
        st.write(f"**Disco Duro**: {producto['hard_drive']}")
        st.write(f"**Gráfica**: {producto['graphics']}")
        st.write(f"**Procesador**: {producto['processor']}")
        st.write(f"**Pantalla**: {producto['screen']}")
        st.write(f"**Dimensiones y peso**: {producto['dimensions_and_weight']}")
        st.write(f"**Conexiones**: {producto['connections']}")
        st.write(f"**RAM**: {producto['ram']}")
        st.write(f"**Audio**: {producto['audio']}")
        st.write(f"**Batería**: {producto['battery']}")
        st.write(f"**Webcam**: {producto['webcam']}")
        st.write(f"**Sistema Operativo**: {producto['os_and_software']}")

        # Botón de compra o acción adicional
        if st.button(f"Comprar {producto['product_name']}"):
            st.write(f"¡Gracias por tu compra de {producto['product_name']}!")
    else:
        st.error("No se ha seleccionado ningún producto.")
