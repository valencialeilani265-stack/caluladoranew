import streamlit as st
import math

st.set_page_config(page_title="Calculadora Pro", page_icon="📱", layout="centered")

# ---- ESTILO ----
st.markdown("""
<style>
.stApp { background-color: #000000; }
.block-container { max-width: 400px !important; padding-top: 2rem !important; }

.display {
    color: white;
    font-size: 70px;
    text-align: right;
    min-height: 100px;
    margin-bottom: 20px;
}

.stButton > button {
    border-radius: 50% !important;
    width: 75px !important;
    height: 75px !important;
    font-size: 22px !important;
    margin: 4px auto !important;
    color: white !important;
    background-color: #ff9f0a !important;
}
</style>
""", unsafe_allow_html=True)

# ---- ESTADO ----
if "current" not in st.session_state:
    st.session_state.current = "0"

if "stored" not in st.session_state:
    st.session_state.stored = None

if "op" not in st.session_state:
    st.session_state.op = None


# ---- CALCULO ----
def operar(a, b, op):
    a, b = float(a), float(b)
    try:
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "×":
            return a * b
        elif op == "÷":
            return a / b if b != 0 else "Error"
    except:
        return "Error"


# ---- BOTONES ----
def click(label):
    cur = st.session_state.current

    if label == "AC":
        st.session_state.current = "0"
        st.session_state.stored = None
        st.session_state.op = None

    elif label == "⌫":
        st.session_state.current = cur[:-1] if len(cur) > 1 else "0"

    elif label in ["+", "-", "×", "÷"]:
        st.session_state.stored = cur
        st.session_state.op = label
        st.session_state.current = "0"

    elif label == "=":
        if st.session_state.op:
            res = operar(st.session_state.stored, cur, st.session_state.op)
            st.session_state.current = str(res)
            st.session_state.op = None

    # ---- FUNCIONES ----
    elif label == "%":
        st.session_state.current = str(float(cur) / 100)

    elif label == "√":
        try:
            st.session_state.current = str(math.sqrt(float(cur)))
        except:
            st.session_state.current = "Error"

    elif label == "x²":
        st.session_state.current = str(float(cur) ** 2)

    elif label == "x³":
        st.session_state.current = str(float(cur) ** 3)

    # ---- NUMEROS ----
    else:
        if cur == "0":
            st.session_state.current = label
        else:
            if len(cur) < 12:
                st.session_state.current += label


# ---- DISPLAY ----
st.markdown(f'<div class="display">{st.session_state.current}</div>', unsafe_allow_html=True)

# ---- LAYOUT ----
filas = [
    ["AC", "⌫", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", "√"],
    ["x²", "x³"]
]

for i, fila in enumerate(filas):
    cols = st.columns(len(fila))
    for j, label in enumerate(fila):
        cols[j].button(label, key=f"{i}-{j}", on_click=click, args=(label,))