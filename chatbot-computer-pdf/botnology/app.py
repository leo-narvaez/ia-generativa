import streamlit as st
from app.home import view_home
from app.product import product_detail
from app.login import login
from app.dashboard import admin_products

# Función principal que carga las vistas
def main():
    st.set_page_config(page_title="BotNology - Ecommerce de Electrónica", page_icon="🔌", layout="wide")

    # Inicializar st.session_state si no está presente
    if "page" not in st.session_state:
        st.session_state.page = "home"  # Página inicial por defecto

    # Barra lateral con el menú de navegación
    st.sidebar.title("Menú")
    page = st.sidebar.radio("Selecciona una página", ["Inicio", "Producto", "Login", "Gestión de productos"])

    # Aquí se selecciona la página a view según la elección del usuario
    if page == "Inicio":
        st.session_state.page = "home"
    elif page == "Producto":
        st.session_state.page = "detail"
    elif page == "Login":
        st.session_state.page = "login"
    elif page == "Gestión de productos":
        st.session_state.page = "admin"

    # Mostrar la vista según el estado de la página
    if st.session_state.page == "home":
        view_home()
    elif st.session_state.page == "detail":
        product_detail()  # Mostrar detalle del producto
    elif st.session_state.page == "login":
        login()
    elif st.session_state.page == "admin":
        admin_products()

if __name__ == "__main__":
    main()
