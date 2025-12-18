import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Nexus Query", page_icon="🚀", layout="wide")

# 2. CSS Personalizado Avanzado
st.markdown("""
    <style>
    /* Eliminar cabecera y tira blanca */
    [data-testid="stHeader"] { display: none; }
    
    .stApp {
        background: linear-gradient(180deg, #2D1B4E 0%, #160D26 100%);
        color: white;
    }

    /* Título y Subtítulo Centrados */
    .titulo-principal {
        text-align: center;
        font-size: 4rem !important;
        font-weight: 800;
        margin-top: 2rem;
        color: #FFFFFF;
    }
    .subtitulo {
        text-align: center;
        font-size: 2.2rem !important;
        color: #B19CD9;
        margin-bottom: 20px;
    }

    /* Alineación perfecta de la descripción */
    .descripcion {
        text-align: center;
        font-size: 1.15rem;
        color: #DCD0FF;
        line-height: 1.6;
        margin-bottom: 2.5rem;
    }

    /* ÁREA DE TEXTO: Fondo claro y letra negra */
    .stTextArea textarea {
        background-color: #F0F2F6 !important; /* Gris muy claro (estilo Gemini) */
        border-radius: 25px !important;
        border: 1px solid #B19CD9 !important;
        color: #160D26 !important; /* Letra violeta muy oscuro (casi negro) */
        padding: 15px 25px !important;
        font-size: 1.1rem !important;
    }

    /* Color del texto sugerido (placeholder) */
    .stTextArea textarea::placeholder {
        color: #6E6E6E !important;
    }
    
    /* Contenedor de la respuesta (Estilo Chat) */
    .bloque-respuesta {
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 25px;
        margin-top: 30px;
        border-left: 5px solid #B19CD9;
    }

    /* Botones Login/Registro */
    div.stButton > button {
        border-radius: 20px;
        border: 1px solid #B19CD9;
        background-color: transparent;
        color: white;
        padding: 5px 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Lógica de sesión
if 'pagina' not in st.session_state: st.session_state.pagina = 'inicio'
if 'resultado_sql' not in st.session_state: st.session_state.resultado_sql = None

# 4. Botones superiores
cols_head = st.columns([8, 1, 1])
with cols_head[1]:
    if st.button("Login"): st.session_state.pagina = 'construccion'
with cols_head[2]:
    if st.button("Registro"): st.session_state.pagina = 'construccion'

# 5. Contenido Principal
if st.session_state.pagina == 'inicio':
    # Título y Subtítulo
    st.markdown('<h1 class="titulo-principal">Nexus Query 🚀</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitulo">Traductor de Lenguaje Natural a SQL</p>', unsafe_allow_html=True)

    # Contenedor centralizado para alineación perfecta
    _, col_central, _ = st.columns([1, 3, 1])
    
    with col_central:
        st.markdown('<div class="descripcion">Nexus Query es una herramienta inteligente diseñada para democratizar el acceso a los datos. Permite generar consultas SQL complejas simplemente escribiendo en lenguaje humano.</div>', unsafe_allow_html=True)
        
        # El st.text_area en Streamlit ya se expande solo si el usuario escribe mucho
        consulta = st.text_area("", placeholder="¿Con qué puedo ayudarte hoy?", label_visibility="collapsed", height=68)
        
        # Botón de acción centrado
        btn_cols = st.columns([1, 1, 1])
        with btn_cols[1]:
            if st.button("Generar Consulta ✨", use_container_width=True):
                if consulta:
                    # Simulamos la respuesta (Aquí conectaremos a Gemini luego)
                    st.session_state.resultado_sql = f"SELECT * FROM tabla WHERE condicion = '{consulta}';"
                else:
                    st.warning("Por favor, ingresa una pregunta primero.")

        # 6. ESPACIO PARA LA DEVOLUCIÓN (Tipo Gemini)
        if st.session_state.resultado_sql:
            st.markdown('<div class="bloque-respuesta">', unsafe_allow_html=True)
            st.markdown("### 🤖 Resultado Generado:")
            st.code(st.session_state.resultado_sql, language='sql')
            st.markdown('</div>', unsafe_allow_html=True)
            
            if st.button("Limpiar"):
                st.session_state.resultado_sql = None
                st.rerun()

elif st.session_state.pagina == 'construccion':
    st.markdown('<h1 style="text-align:center; padding-top:100px;">Próximamente... 🛠️</h1>', unsafe_allow_html=True)
    if st.button("Volver al Inicio"):
        st.session_state.pagina = 'inicio'
        st.rerun()