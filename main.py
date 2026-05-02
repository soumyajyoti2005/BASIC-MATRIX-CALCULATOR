# py -3.13 -m streamlit run "Matrix_Calculator/main.py"

import streamlit as st
import numpy as np

st.markdown("""
<style>
/* ---- Google Font ---- */
@import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Rajdhani:wght@400;600;700&display=swap');

/* ---- Animated gradient background ---- */
@keyframes gradientShift {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

@keyframes particleDrift {
    0%   { transform: translateY(0px) translateX(0px) rotate(0deg); opacity: 0.15; }
    33%  { transform: translateY(-30px) translateX(20px) rotate(120deg); opacity: 0.35; }
    66%  { transform: translateY(-15px) translateX(-15px) rotate(240deg); opacity: 0.2; }
    100% { transform: translateY(0px) translateX(0px) rotate(360deg); opacity: 0.15; }
}

@keyframes glowPulse {
    0%, 100% { box-shadow: 0 0 20px rgba(99, 179, 237, 0.15), 0 0 40px rgba(99, 179, 237, 0.05); }
    50%       { box-shadow: 0 0 30px rgba(99, 179, 237, 0.3),  0 0 60px rgba(99, 179, 237, 0.1); }
}

@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(24px); }
    to   { opacity: 1; transform: translateY(0); }
}

@keyframes scanline {
    0%   { transform: translateY(-100%); }
    100% { transform: translateY(100vh); }
}

/* ---- Root overrides ---- */
html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    background: transparent !important;
}

[data-testid="stAppViewContainer"]::before {
    content: '';
    position: fixed;
    inset: 0;
    background: linear-gradient(
        135deg,
        #0a0a0f 0%,
        #0d1117 20%,
        #0f1923 40%,
        #0a0e1a 60%,
        #0d1117 80%,
        #0a0a0f 100%
    );
    background-size: 400% 400%;
    animation: gradientShift 12s ease infinite;
    z-index: -3;
}

/* Subtle grid overlay */
[data-testid="stAppViewContainer"]::after {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
        linear-gradient(rgba(99,179,237,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(99,179,237,0.03) 1px, transparent 1px);
    background-size: 40px 40px;
    z-index: -2;
    pointer-events: none;
}

/* Floating orb — top left */
[data-testid="stMain"]::before {
    content: '';
    position: fixed;
    top: -120px; left: -120px;
    width: 480px; height: 480px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(56,189,248,0.08) 0%, transparent 70%);
    animation: particleDrift 14s ease-in-out infinite;
    z-index: -1;
    pointer-events: none;
}

/* Floating orb — bottom right */
[data-testid="stMain"]::after {
    content: '';
    position: fixed;
    bottom: -80px; right: -80px;
    width: 360px; height: 360px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(139,92,246,0.07) 0%, transparent 70%);
    animation: particleDrift 18s ease-in-out infinite reverse;
    z-index: -1;
    pointer-events: none;
}

/* ---- Hide default Streamlit chrome ---- */
[data-testid="stHeader"],
footer,
#MainMenu { display: none !important; }

/* ---- Main content wrapper ---- */
.main .block-container {
    padding: 2.5rem 3rem;
    max-width: 1200px;
    animation: fadeInUp 0.7s ease both;
}

/* ---- Page title ---- */
.page-title {
    font-family: 'Rajdhani', sans-serif;
    font-weight: 700;
    font-size: 2rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #e2e8f0;
    text-align: center;
    margin-bottom: 0.25rem;
    text-shadow: 0 0 20px rgba(99,179,237,0.4);
}

.page-subtitle {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.75rem;
    color: rgba(99,179,237,0.5);
    text-align: center;
    letter-spacing: 0.25em;
    margin-bottom: 2.5rem;
}

/* ---- Section headers ---- */
.matrix-label {
    font-family: 'Rajdhani', sans-serif;
    font-weight: 700;
    font-size: 1.6rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #e2e8f0;
    margin-bottom: 1rem;
    text-shadow: 0 0 12px rgba(99,179,237,0.3);
}

/* ---- Panel card ---- */
.matrix-panel {
    background: rgba(15, 23, 42, 0.7);
    border: 1px solid rgba(99,179,237,0.15);
    border-radius: 12px;
    padding: 1.5rem 1.75rem 1.75rem;
    backdrop-filter: blur(12px);
    animation: glowPulse 4s ease-in-out infinite;
    transition: border-color 0.3s;
}
.matrix-panel:hover {
    border-color: rgba(99,179,237,0.35);
}

/* ---- Result panel ---- */
.result-panel {
    background: rgba(10, 18, 35, 0.8);
    border: 1px solid rgba(99,179,237,0.2);
    border-radius: 12px;
    padding: 1.5rem 1.75rem;
    backdrop-filter: blur(16px);
    margin-top: 1.5rem;
    text-align: center;
}

.result-title {
    font-family: 'Rajdhani', sans-serif;
    font-weight: 700;
    font-size: 1.4rem;
    letter-spacing: 0.2em;
    color: #90cdf4;
    text-transform: uppercase;
    margin-bottom: 1rem;
    text-shadow: 0 0 14px rgba(99,179,237,0.4);
}

/* ---- Number inputs ---- */
div[data-testid="stNumberInput"] input {
    background: rgba(15, 23, 42, 0.9) !important;
    border: 1px solid rgba(99,179,237,0.2) !important;
    border-radius: 6px !important;
    color: #e2e8f0 !important;
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 0.9rem !important;
    transition: border-color 0.2s, box-shadow 0.2s !important;
}
div[data-testid="stNumberInput"] input:focus {
    border-color: rgba(99,179,237,0.6) !important;
    box-shadow: 0 0 0 2px rgba(99,179,237,0.15) !important;
    outline: none !important;
}
div[data-testid="stNumberInput"] label {
    color: rgba(148,163,184,0.85) !important;
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 0.75rem !important;
    letter-spacing: 0.05em !important;
}

/* ---- Select box ---- */
div[data-testid="stSelectbox"] select,
div[data-testid="stSelectbox"] div[data-baseweb="select"] {
    background: rgba(15,23,42,0.9) !important;
    border: 1px solid rgba(99,179,237,0.2) !important;
    border-radius: 6px !important;
    color: #e2e8f0 !important;
    font-family: 'Share Tech Mono', monospace !important;
}

/* ---- Button ---- */
div[data-testid="stButton"] button {
    background: linear-gradient(135deg, rgba(56,189,248,0.15), rgba(99,179,237,0.25)) !important;
    border: 1px solid rgba(99,179,237,0.45) !important;
    border-radius: 8px !important;
    color: #90cdf4 !important;
    font-family: 'Rajdhani', sans-serif !important;
    font-weight: 600 !important;
    font-size: 1rem !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;
    padding: 0.55rem 1.8rem !important;
    transition: all 0.25s !important;
    cursor: pointer !important;
}
div[data-testid="stButton"] button:hover {
    background: linear-gradient(135deg, rgba(56,189,248,0.3), rgba(99,179,237,0.4)) !important;
    border-color: rgba(99,179,237,0.8) !important;
    box-shadow: 0 0 18px rgba(99,179,237,0.3) !important;
    transform: translateY(-1px) !important;
}

/* ---- Result cells ---- */
.result-grid {
    display: inline-grid;
    gap: 8px;
    margin-top: 0.5rem;
}
.result-cell {
    background: rgba(15, 23, 42, 0.9);
    border: 1px solid rgba(99,179,237,0.25);
    border-radius: 8px;
    padding: 0.55rem 1rem;
    color: #90cdf4;
    font-family: 'Share Tech Mono', monospace;
    font-size: 1rem;
    text-align: center;
    min-width: 68px;
    animation: fadeInUp 0.4s ease both;
}

/* ---- Error / info messages ---- */
div[data-testid="stAlert"] {
    background: rgba(15,23,42,0.8) !important;
    border: 1px solid rgba(239,68,68,0.3) !important;
    border-radius: 8px !important;
    color: #fca5a5 !important;
    font-family: 'Share Tech Mono', monospace !important;
}

/* ---- Divider ---- */
hr {
    border-color: rgba(99,179,237,0.12) !important;
    margin: 1.5rem 0 !important;
}

/* ---- Scrollbar ---- */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: #0a0a0f; }
::-webkit-scrollbar-thumb { background: rgba(99,179,237,0.3); border-radius: 4px; }
</style>
""", unsafe_allow_html=True)


col1, op, col2 = st.columns(3)
MatrixA = []
MatrixB = []
submit = False

if "op_button" not in st.session_state:
    st.session_state.op_button = None


with col1:
    st.header("MATRIX A")
    cols=[]
    rowsA = st.number_input("Enter no of rows in Matrix A :", step=1, format="%d")
    colsA = st.number_input("Enter no of columns in Matrix A :", step=1, format="%d")
    rows = rowsA

    if colsA > 0:
        cols = st.columns(int(colsA))

    for i in range(rows):
        rowA = []
        for j in range(int(colsA)):
            val = cols[j].number_input(
                "A",
                key = f"A{i}{j}",
                label_visibility="collapsed"
            )
            rowA.append(val)
        MatrixA.append(rowA)



with op :
    cols = st.columns(3)

    for j in range(3):
        if j==0 : 
            cols[j].write("")
            cols[j].write("")
            cols[j].write("")
            cols[j].write("")
            cols[j].write("")
            cols[j].write("")
            cols[j].write("")
            cols[j].write("")
            if cols[0].button("+",key="+"):
              st.session_state.op_button = "+"

        if j==1 : 
            cols[j].write("")
            cols[j].write("")
            cols[j].write("")
            cols[j].write("")
            cols[j].write("")
            cols[j].write("")
            cols[j].write("")
            cols[j].write("")
            if cols[1].button("X",key="X"):
              st.session_state.op_button = "X"

        if j==2 : 
            cols[j].write("")
            cols[j].write("")
            cols[j].write("")
            cols[j].write("")
            cols[j].write("")
            cols[j].write("")
            cols[j].write("")
            cols[j].write("")
            if cols[2].button("-",key="-"):
              st.session_state.op_button = "-"

        
        if j==1 and st.session_state.op_button is not None:
            cols[j].write("")
            cols[j].write("")
            cols[j].write("")
            cols[j].write("")
            cols[1].button(f"{st.session_state.op_button}",disabled=True)
        


with col2:
    st.header("MATRIX B")
    cols=[]
    rowsB = st.number_input("Enter no of rows in Matrix B :", step=1, format="%d")
    colsB = st.number_input("Enter no of columns in Matrix B :", step=1, format="%d")
    rows = rowsB

    if colsB > 0:
        cols = st.columns(int(colsB))

    for i in range(rows):
        rowB = []
        for j in range(int(colsB)):
            val = cols[j].number_input(
                "B",
                key = f"B{i}{j}",
                label_visibility="collapsed"
            )
            rowB.append(val)
        MatrixB.append(rowB)
        if i==rows-1: 
            submit=st.button("Submit",key="enter")

if submit == True:
    ui_cols = st.columns(3)
    arr_2dA = np.array(MatrixA)
    arr_2dB = np.array(MatrixB)
    res = None
    print(arr_2dA)
    print(arr_2dB)

    if st.session_state.op_button == "+":
        res = arr_2dA + arr_2dB
        print(res)

    if st.session_state.op_button == "X":
        res = arr_2dA @ arr_2dB
        print(res)

    if st.session_state.op_button == "-":
        res = arr_2dA - arr_2dB
        print(res)

    shape = res.shape
    rows = shape[0]
    cols = shape[1]

    with ui_cols[1]:
        st.header("Matrix Res")
        inside_cols = st.columns(cols)
        for i in range(rows):
            for j in range(int(cols)):
                but = inside_cols[j].button(
                    f"{res[i][j]}",
                    key=f"res{i}{j}",
                    disabled=True
                )
                


    









