import streamlit as st

# Usuario y contraseña predefinidos para el ejemplo
USUARIO_ADMIN = "admin"
CONTRASENA_ADMIN = "admin123"

# Función para manejar el login
def login():
    st.title("Inicio de sesión")
    
    # Formulario de login
    usuario = st.text_input("Usuario")
    contrasena = st.text_input("Contraseña", type="password")
    
    if st.button("Iniciar sesión"):
        if usuario == USUARIO_ADMIN and contrasena == CONTRASENA_ADMIN:
            st.session_state.logged_in = True
            st.session_state.usuario = usuario
            st.success("¡Inicio de sesión exitoso!")
            st.session_state.login_exitoso = True  # Marca como login exitoso
            st.experimental_rerun()  # Recarga la aplicación para acceder a otras vistas
        else:
            st.error("Credenciales incorrectas. Intenta nuevamente.")
    
    # Mostrar mensaje si el usuario ya ha iniciado sesión
    if 'logged_in' in st.session_state and st.session_state.logged_in:
        st.success(f"Bienvenido, {st.session_state.usuario}!")
        st.sidebar.success(f"Hola, {st.session_state.usuario}!")
        st.sidebar.radio("Ir a", ["Inicio", "Producto", "Gestión de productos"])

