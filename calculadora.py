import streamlit as st
import re

st.set_page_config(page_title="Formulario Pro", page_icon="📋", layout="centered")

# ---- ESTILO ----
st.markdown("""
<style>
.stApp { background-color: #000000; }
.block-container { max-width: 500px !important; padding-top: 2rem !important; }

.title {
    color: white;
    font-size: 40px;
    text-align: center;
    margin-bottom: 20px;
}

.stTextInput input, .stTextArea textarea {
    background-color: #1c1c1c !important;
    color: white !important;
    border-radius: 10px !important;
}

.stButton > button {
    border-radius: 10px !important;
    width: 100% !important;
    height: 50px !important;
    font-size: 18px !important;
    color: white !important;
    background-color: #ff9f0a !important;
}
</style>
""", unsafe_allow_html=True)

# ---- TÍTULO ----
st.markdown('<div class="title">📋 Formulario de Registro</div>', unsafe_allow_html=True)

# ---- FORMULARIO ----
with st.form("formulario"):
    nombre = st.text_input("Nombre completo")
    email = st.text_input("Correo electrónico")
    edad = st.number_input("Edad", min_value=0, max_value=120, step=1)
    mensaje = st.text_area("Mensaje")

    aceptar = st.checkbox("Acepto los términos y condiciones")

    submit = st.form_submit_button("Enviar")

# ---- VALIDACIONES ----
def email_valido(email):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, email)

# ---- RESULTADO ----
if submit:
    errores = []

    if not nombre:
        errores.append("El nombre es obligatorio")
    if not email or not email_valido(email):
        errores.append("Correo inválido")
    if edad < 1:
        errores.append("Edad no válida")
    if not aceptar:
        errores.append("Debes aceptar los términos")

    if errores:
        for e in errores:
            st.error(e)
    else:
        st.success("✅ Formulario enviado correctamente")

        st.markdown("### 📄 Resumen")
        st.write(f"**Nombre:** {nombre}")
        st.write(f"**Correo:** {email}")
        st.write(f"**Edad:** {edad}")
        st.write(f"**Mensaje:** {mensaje if mensaje else 'Sin mensaje'}")

        # Simulación de guardado
        st.info("Datos guardados (simulado)")

# ---- EXTRA ----
st.markdown("---")
st.caption("App creada con Streamlit 🚀")