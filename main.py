# import streamlit as st

# # 1. Configuración de la página
# st.set_page_config(page_title="Nexus Query", page_icon="🚀", layout="wide")

# # 2. CSS Personalizado Avanzado
# st.markdown("""
#     <style>
#     /* Eliminar cabecera y tira blanca */
#     [data-testid="stHeader"] { display: none; }
    
#     .stApp {
#         background: linear-gradient(180deg, #2D1B4E 0%, #160D26 100%);
#         color: white;
#     }

#     /* Título y Subtítulo Centrados */
#     .titulo-principal {
#         text-align: center;
#         font-size: 4rem !important;
#         font-weight: 800;
#         margin-top: 2rem;
#         color: #FFFFFF;
#     }
#     .subtitulo {
#         text-align: center;
#         font-size: 2.2rem !important;
#         color: #B19CD9;
#         margin-bottom: 20px;
#     }

#     /* Alineación perfecta de la descripción */
#     .descripcion {
#         text-align: center;
#         font-size: 1.15rem;
#         color: #DCD0FF;
#         line-height: 1.6;
#         margin-bottom: 2.5rem;
#     }

#     /* ÁREA DE TEXTO: Fondo claro y letra negra */
#     .stTextArea textarea {
#         background-color: #F0F2F6 !important; /* Gris muy claro (estilo Gemini) */
#         border-radius: 25px !important;
#         border: 1px solid #B19CD9 !important;
#         color: #160D26 !important; /* Letra violeta muy oscuro (casi negro) */
#         padding: 15px 25px !important;
#         font-size: 1.1rem !important;
#     }

#     /* Color del texto sugerido (placeholder) */
#     .stTextArea textarea::placeholder {
#         color: #6E6E6E !important;
#     }
    
#     /* Contenedor de la respuesta (Estilo Chat) */
#     .bloque-respuesta {
#         background-color: rgba(255, 255, 255, 0.05);
#         border-radius: 20px;
#         padding: 25px;
#         margin-top: 30px;
#         border-left: 5px solid #B19CD9;
#     }

#     /* Botones Login/Registro */
#     div.stButton > button {
#         border-radius: 20px;
#         border: 1px solid #B19CD9;
#         background-color: transparent;
#         color: white;
#         padding: 5px 20px;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # 3. Lógica de sesión
# if 'pagina' not in st.session_state: st.session_state.pagina = 'inicio'
# if 'resultado_sql' not in st.session_state: st.session_state.resultado_sql = None

# # 4. Botones superiores
# cols_head = st.columns([8, 1, 1])
# with cols_head[1]:
#     if st.button("Login"): st.session_state.pagina = 'construccion'
# with cols_head[2]:
#     if st.button("Registro"): st.session_state.pagina = 'construccion'

# # 5. Contenido Principal
# if st.session_state.pagina == 'inicio':
#     # Título y Subtítulo
#     st.markdown('<h1 class="titulo-principal">Nexus Query 🚀</h1>', unsafe_allow_html=True)
#     st.markdown('<p class="subtitulo">Traductor de Lenguaje Natural a SQL</p>', unsafe_allow_html=True)

#     # Contenedor centralizado para alineación perfecta
#     _, col_central, _ = st.columns([1, 3, 1])
    
#     with col_central:
#         st.markdown('<div class="descripcion">Nexus Query es una herramienta inteligente diseñada para democratizar el acceso a los datos. Permite generar consultas SQL complejas simplemente escribiendo en lenguaje humano.</div>', unsafe_allow_html=True)
        
#         # El st.text_area en Streamlit ya se expande solo si el usuario escribe mucho
#         consulta = st.text_area("", placeholder="¿Con qué puedo ayudarte hoy?", label_visibility="collapsed", height=68)
        
#         # Botón de acción centrado
#         btn_cols = st.columns([1, 1, 1])
#         with btn_cols[1]:
#             if st.button("Generar Consulta ✨", use_container_width=True):
#                 if consulta:
#                     # Simulamos la respuesta (Aquí conectaremos a Gemini luego)
#                     st.session_state.resultado_sql = f"SELECT * FROM tabla WHERE condicion = '{consulta}';"
#                 else:
#                     st.warning("Por favor, ingresa una pregunta primero.")

#         # 6. ESPACIO PARA LA DEVOLUCIÓN (Tipo Gemini)
#         if st.session_state.resultado_sql:
#             st.markdown('<div class="bloque-respuesta">', unsafe_allow_html=True)
#             st.markdown("### 🤖 Resultado Generado:")
#             st.code(st.session_state.resultado_sql, language='sql')
#             st.markdown('</div>', unsafe_allow_html=True)
            
#             if st.button("Limpiar"):
#                 st.session_state.resultado_sql = None
#                 st.rerun()

# elif st.session_state.pagina == 'construccion':
#     st.markdown('<h1 style="text-align:center; padding-top:100px;">Próximamente... 🛠️</h1>', unsafe_allow_html=True)
#     if st.button("Volver al Inicio"):
#         st.session_state.pagina = 'inicio'
#         st.rerun()

##################################################################
#SEGUNDA VERSIÓN CON INTEGRACIÓN A LA API DE GEMINI
##################################################################

# import streamlit as st
# import os
# from google import genai
# from dotenv import load_dotenv
# from src.prompts import obtener_prompt_sql

# # 1. Cargar variables de entorno
# load_dotenv()

# # 2. Configuración de la página
# st.set_page_config(page_title="Nexus Query", page_icon="🚀", layout="wide")

# # 3. CSS Personalizado Avanzado (Restaurado según tu solicitud)
# st.markdown("""
#     <style>
#     /* Eliminar cabecera y tira blanca */
#     [data-testid="stHeader"] { display: none; }
    
#     .stApp {
#         background: linear-gradient(180deg, #2D1B4E 0%, #160D26 100%);
#         color: white;
#     }

#     /* Título y Subtítulo Centrados */
#     .titulo-principal {
#         text-align: center;
#         font-size: 4rem !important;
#         font-weight: 800;
#         margin-top: 2rem;
#         color: #FFFFFF;
#     }
#     .subtitulo {
#         text-align: center;
#         font-size: 2.2rem !important;
#         color: #B19CD9;
#         margin-bottom: 20px;
#     }

#     /* Alineación perfecta de la descripción */
#     .descripcion {
#         text-align: center;
#         font-size: 1.15rem;
#         color: #DCD0FF;
#         line-height: 1.6;
#         margin-bottom: 2.5rem;
#     }

#     /* ÁREA DE TEXTO: Fondo claro y letra negra */
#     .stTextArea textarea {
#         background-color: #F0F2F6 !important; /* Gris muy claro */
#         border-radius: 25px !important;
#         border: 1px solid #B19CD9 !important;
#         color: #160D26 !important; /* Letra violeta oscuro/negro */
#         padding: 15px 25px !important;
#         font-size: 1.1rem !important;
#     }

#     /* Color del texto sugerido (placeholder) */
#     .stTextArea textarea::placeholder {
#         color: #6E6E6E !important;
#     }
    
#     /* Contenedor de la respuesta (Estilo Chat) */
#     .bloque-respuesta {
#         background-color: rgba(255, 255, 255, 0.05);
#         border-radius: 20px;
#         padding: 25px;
#         margin-top: 30px;
#         border-left: 5px solid #B19CD9;
#     }

#     /* Botones Login/Registro */
#     div.stButton > button {
#         border-radius: 20px;
#         border: 1px solid #B19CD9;
#         background-color: transparent;
#         color: white;
#         padding: 5px 20px;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # 4. Lógica de sesión y Memoria
# if 'pagina' not in st.session_state: st.session_state.pagina = 'inicio'
# if 'resultado_sql' not in st.session_state: st.session_state.resultado_sql = None
# if 'messages' not in st.session_state: st.session_state.messages = [] # Historial para contexto

# # 5. Botones superiores
# cols_head = st.columns([8, 1, 1])
# with cols_head[1]:
#     if st.button("Login"): st.session_state.pagina = 'construccion'
# with cols_head[2]:
#     if st.button("Registro"): st.session_state.pagina = 'construccion'

# # 6. Contenido Principal
# if st.session_state.pagina == 'inicio':
#     # Título y Subtítulo
#     st.markdown('<h1 class="titulo-principal">Nexus Query 🚀</h1>', unsafe_allow_html=True)
#     st.markdown('<p class="subtitulo">Traductor de Lenguaje Natural a SQL</p>', unsafe_allow_html=True)

#     # Contenedor centralizado
#     _, col_central, _ = st.columns([1, 3, 1])
    
#     with col_central:
#         st.markdown('<div class="descripcion">Nexus Query es una herramienta inteligente diseñada para democratizar el acceso a los datos. Permite generar consultas SQL complejas simplemente escribiendo en lenguaje humano.</div>', unsafe_allow_html=True)
        
#         # Entrada del usuario
#         consulta = st.text_area("", placeholder="¿Con qué puedo ayudarte hoy?", label_visibility="collapsed", height=100)
        
#         # Botón de acción
#         btn_cols = st.columns([1, 1, 1])
#         with btn_cols[1]:
#             if st.button("Generar Consulta ✨", use_container_width=True):
#                 if consulta:
#                     try:
#                         api_key = os.getenv("GEMINI_API_KEY")
#                         if not api_key:
#                             st.error("No se encontró la API Key en el .env")
#                         else:
#                             client = genai.Client(api_key=api_key)
                            
#                             # Prompt e Historial
#                             current_schema = "Aún no hay tablas definidas." # Esto puede ser dinámico
#                             system_prompt = obtener_prompt_sql(current_schema)
                            
#                             # Construir historial para Gemini
#                             history = []
#                             for m in st.session_state.messages:
#                                 role = "user" if m["role"] == "user" else "model"
#                                 history.append({"role": role, "parts": [{"text": m["content"]}]})

#                             # Crear chat con memoria usando el modelo gemini-2.5-flash
#                             chat = client.chats.create(
#                                 model="gemini-2.5-flash",
#                                 config={"system_instruction": system_prompt},
#                                 history=history
#                             )
                            
#                             # Enviar mensaje y obtener respuesta
#                             response = chat.send_message(consulta)
                            
#                             # Guardar en historial y mostrar resultado
#                             st.session_state.messages.append({"role": "user", "content": consulta})
#                             st.session_state.messages.append({"role": "model", "content": response.text})
#                             st.session_state.resultado_sql = response.text
#                             st.rerun()

#                     except Exception as e:
#                         st.error(f"Error con la IA: {e}")
#                 else:
#                     st.warning("Por favor, ingresa una pregunta primero.")

#         # 7. ESPACIO PARA LA DEVOLUCIÓN (Estilo bloque que pediste)
#         if st.session_state.resultado_sql:
#             st.markdown('<div class="bloque-respuesta">', unsafe_allow_html=True)
#             st.markdown("### 🤖 Respuesta de Nexus Query:")
#             st.write(st.session_state.resultado_sql)
#             st.markdown('</div>', unsafe_allow_html=True)
            
#             if st.button("Limpiar Chat"):
#                 st.session_state.resultado_sql = None
#                 st.session_state.messages = []
#                 st.rerun()

# elif st.session_state.pagina == 'construccion':
#     st.markdown('<h1 style="text-align:center; padding-top:100px;">Próximamente... 🛠️</h1>', unsafe_allow_html=True)
#     if st.button("Volver al Inicio"):
#         st.session_state.pagina = 'inicio'
#         st.rerun()
#########################################################
#TERCERA VERSIÓN CON INTEGRACIÓN A LA API DE GEMINI
#########################################################
# import streamlit as st
# import os
# from google import genai
# from dotenv import load_dotenv
# from src.prompts import obtener_prompt_sql

# # 1. Cargar variables de entorno
# load_dotenv()

# # 2. Configuración de la página
# st.set_page_config(page_title="Nexus Query", page_icon="🚀", layout="wide")

# # 3. CSS Personalizado Avanzado
# st.markdown("""
#     <style>
#     /* Eliminar cabecera y tira blanca */
#     [data-testid="stHeader"] { display: none; }
    
#     .stApp {
#         background: linear-gradient(180deg, #2D1B4E 0%, #160D26 100%);
#         color: white;
#     }

#     /* Título y Subtítulo Centrados */
#     .titulo-principal {
#         text-align: center;
#         font-size: 4rem !important;
#         font-weight: 800;
#         margin-top: 2rem;
#         color: #FFFFFF;
#     }
#     .subtitulo {
#         text-align: center;
#         font-size: 2.2rem !important;
#         color: #B19CD9;
#         margin-bottom: 20px;
#     }

#     /* Alineación de la descripción */
#     .descripcion {
#         text-align: center;
#         font-size: 1.15rem;
#         color: #DCD0FF;
#         line-height: 1.6;
#         margin-bottom: 2.5rem;
#     }

#     /* Burbujas de Chat */
#     .chat-bubble {
#         padding: 20px;
#         border-radius: 20px;
#         margin-bottom: 15px;
#         line-height: 1.5;
#         max-width: 90%;
#     }
    
#     .user-bubble {
#         background-color: rgba(177, 156, 217, 0.15);
#         border-left: 5px solid #B19CD9;
#         margin-left: auto;
#         color: #E0B0FF;
#     }

#     .ai-bubble {
#         background-color: rgba(255, 255, 255, 0.05);
#         border-left: 5px solid #FFFFFF;
#         margin-right: auto;
#         color: #FFFFFF;
#     }

#     /* ÁREA DE TEXTO: Fondo claro y letra negra */
#     .stTextArea textarea {
#         background-color: #F0F2F6 !important;
#         border-radius: 25px !important;
#         border: 1px solid #B19CD9 !important;
#         color: #160D26 !important;
#         padding: 15px 25px !important;
#         font-size: 1.1rem !important;
#     }

#     /* Botones Login/Registro */
#     div.stButton > button {
#         border-radius: 20px;
#         border: 1px solid #B19CD9;
#         background-color: transparent;
#         color: white;
#         padding: 5px 20px;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # 4. Lógica de sesión y Memoria
# if 'pagina' not in st.session_state: st.session_state.pagina = 'inicio'
# if 'messages' not in st.session_state: st.session_state.messages = [] # Historial completo

# # 5. Botones superiores
# cols_head = st.columns([8, 1, 1])
# with cols_head[1]:
#     if st.button("Login"): st.session_state.pagina = 'construccion'
# with cols_head[2]:
#     if st.button("Registro"): st.session_state.pagina = 'construccion'

# # 6. Contenido Principal
# if st.session_state.pagina == 'inicio':
#     # Título y Subtítulo
#     st.markdown('<h1 class="titulo-principal">Nexus Query 🚀</h1>', unsafe_allow_html=True)
#     st.markdown('<p class="subtitulo">Traductor de Lenguaje Natural a SQL</p>', unsafe_allow_html=True)

#     # Contenedor centralizado
#     _, col_central, _ = st.columns([1, 3, 1])
    
#     with col_central:
#         st.markdown('<div class="descripcion">Conversa con Nexus Query para definir tus tablas y generar consultas SQL complejas de forma instantánea.</div>', unsafe_allow_html=True)
        
#         # VISUALIZACIÓN DE TODA LA CONVERSACIÓN
#         for msg in st.session_state.messages:
#             if msg["role"] == "user":
#                 st.markdown(f'<div class="chat-bubble user-bubble"><strong>👤 Tú:</strong><br>{msg["content"]}</div>', unsafe_allow_html=True)
#             else:
#                 st.markdown('<div class="chat-bubble ai-bubble"><strong>🤖 Nexus Query:</strong></div>', unsafe_allow_html=True)
#                 # Si la respuesta parece SQL (o según las reglas de nuestro prompt), le damos formato de código
#                 # Verificamos si contiene palabras clave de SQL para decidir si usar st.code
#                 if any(kw in msg["content"].upper() for kw in ["SELECT", "INSERT", "CREATE", "UPDATE", "DELETE"]):
#                     st.code(msg["content"], language='sql')
#                 else:
#                     st.write(msg["content"])

#         # Espacio extra
#         st.write("")
        
#         # Entrada del usuario (Formulario para limpiar al enviar)
#         with st.form(key="chat_form", clear_on_submit=True):
#             consulta = st.text_area("", placeholder="¿Con qué puedo ayudarte hoy?", label_visibility="collapsed", height=100)
#             submit_col1, submit_col2, submit_col3 = st.columns([1, 1, 1])
#             with submit_col2:
#                 enviar = st.form_submit_button("Generar Consulta ✨", use_container_width=True)

#         if enviar and consulta:
#             try:
#                 api_key = os.getenv("GEMINI_API_KEY")
#                 if not api_key:
#                     st.error("No se encontró la API Key en el .env")
#                 else:
#                     client = genai.Client(api_key=api_key)
                    
#                     # Definimos el esquema dinámico para el prompt
#                     current_schema = "Tablas detectadas en la conversación." 
#                     system_prompt = obtener_prompt_sql(current_schema)
                    
#                     # Construir historial para Gemini
#                     history = []
#                     for m in st.session_state.messages:
#                         role = "user" if m["role"] == "user" else "model"
#                         history.append({"role": role, "parts": [{"text": m["content"]}]})

#                     # Llamada a la IA
#                     chat = client.chats.create(
#                         model="gemini-2.5-flash",
#                         config={"system_instruction": system_prompt},
#                         history=history
#                     )
                    
#                     response = chat.send_message(consulta)
                    
#                     # Guardar ambos mensajes en el historial
#                     st.session_state.messages.append({"role": "user", "content": consulta})
#                     st.session_state.messages.append({"role": "model", "content": response.text})
                    
#                     # Refrescar para mostrar el nuevo mensaje
#                     st.rerun()

#             except Exception as e:
#                 st.error(f"Error con la IA: {e}")

#         # Botón para reiniciar la conversación
#         if st.session_state.messages:
#             st.write("")
#             if st.button("Limpiar conversación"):
#                 st.session_state.messages = []
#                 st.rerun()

# elif st.session_state.pagina == 'construccion':
#     st.markdown('<h1 style="text-align:center; padding-top:100px;">Próximamente... 🛠️</h1>', unsafe_allow_html=True)
#     if st.button("Volver al Inicio"):
#         st.session_state.pagina = 'inicio'
#         st.rerun()
##########################################################
#CUARTA VERSIÓN CON INTEGRACIÓN A LA API DE GEMINI
##########################################################
# import streamlit as st
# import os
# from google import genai
# from dotenv import load_dotenv
# from src.prompts import obtener_prompt_sql

# # 1. Cargar variables de entorno
# load_dotenv()

# # 2. Configuración de la página
# st.set_page_config(page_title="Nexus Query", page_icon="🚀", layout="wide")

# # 3. CSS Personalizado Avanzado
# st.markdown("""
#     <style>
#     /* Eliminar cabecera y tira blanca */
#     [data-testid="stHeader"] { display: none; }
    
#     .stApp {
#         background: linear-gradient(180deg, #2D1B4E 0%, #160D26 100%);
#         color: white;
#     }

#     /* Título y Subtítulo Centrados */
#     .titulo-principal {
#         text-align: center;
#         font-size: 3.5rem !important;
#         font-weight: 800;
#         margin-top: 1rem;
#         color: #FFFFFF;
#     }
#     .subtitulo {
#         text-align: center;
#         font-size: 1.8rem !important;
#         color: #B19CD9;
#         margin-bottom: 10px;
#     }

#     /* Alineación de la descripción */
#     .descripcion {
#         text-align: center;
#         font-size: 1rem;
#         color: #DCD0FF;
#         line-height: 1.4;
#         margin-bottom: 1.5rem;
#     }

#     /* Burbujas de Chat */
#     .chat-bubble {
#         padding: 15px;
#         border-radius: 20px;
#         margin-bottom: 15px;
#         line-height: 1.5;
#         width: fit-content;
#         max-width: 85%;
#     }
    
#     .user-bubble {
#         background-color: rgba(177, 156, 217, 0.25);
#         border-bottom-right-radius: 5px;
#         margin-left: auto;
#         color: #E0B0FF;
#         border-right: 4px solid #B19CD9;
#     }

#     .ai-bubble {
#         background-color: rgba(255, 255, 255, 0.08);
#         border-bottom-left-radius: 5px;
#         margin-right: auto;
#         color: #FFFFFF;
#         border-left: 4px solid #FFFFFF;
#     }

#     /* ÁREA DE TEXTO: Fondo claro y letra negra */
#     .stTextArea textarea {
#         background-color: #F0F2F6 !important;
#         border-radius: 20px !important;
#         border: 2px solid #B19CD9 !important;
#         color: #160D26 !important;
#         padding: 15px 20px !important;
#         font-size: 1rem !important;
#     }

#     /* Botones Login/Registro */
#     div.stButton > button {
#         border-radius: 20px;
#         border: 1px solid #B19CD9;
#         background-color: transparent;
#         color: white;
#         padding: 5px 20px;
#     }
    
#     /* Contenedor del Chat (Scrollable) */
#     .stChatFloatingInputContainer {
#         background-color: transparent !important;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # 4. Lógica de sesión y Memoria
# if 'pagina' not in st.session_state: st.session_state.pagina = 'inicio'
# if 'messages' not in st.session_state: st.session_state.messages = [] 

# # 5. Botones superiores
# cols_head = st.columns([8, 1, 1])
# with cols_head[1]:
#     if st.button("Login"): st.session_state.pagina = 'construccion'
# with cols_head[2]:
#     if st.button("Registro"): st.session_state.pagina = 'construccion'

# # 6. Contenido Principal
# if st.session_state.pagina == 'inicio':
#     # Título y Subtítulo
#     st.markdown('<h1 class="titulo-principal">Nexus Query 🚀</h1>', unsafe_allow_html=True)
#     st.markdown('<p class="subtitulo">Traductor de Lenguaje Natural a SQL</p>', unsafe_allow_html=True)
    
#     # Contenedor centralizado para la estructura principal
#     _, col_central, _ = st.columns([1, 4, 1])
    
#     with col_central:
#         st.markdown('<div class="descripcion">Conversa con Nexus Query para definir tus tablas y generar consultas SQL complejas.</div>', unsafe_allow_html=True)
        
#         # --- ÁREA DE CONVERSACIÓN (SCROLLABLE) ---
#         # Usamos un contenedor con altura definida para habilitar el scroll interno
#         chat_container = st.container(height=500, border=False)
        
#         with chat_container:
#             for msg in st.session_state.messages:
#                 if msg["role"] == "user":
#                     st.markdown(f'<div class="chat-bubble user-bubble"><strong>👤 Tú:</strong><br>{msg["content"]}</div>', unsafe_allow_html=True)
#                 else:
#                     st.markdown('<div class="chat-bubble ai-bubble"><strong>🤖 Nexus Query:</strong></div>', unsafe_allow_html=True)
#                     if any(kw in msg["content"].upper() for kw in ["SELECT", "INSERT", "CREATE", "UPDATE", "DELETE"]):
#                         st.code(msg["content"], language='sql')
#                     else:
#                         st.write(msg["content"])
        
#         # --- ÁREA DE ENTRADA (PROMPT) ---
#         st.write("---") # Separador visual
#         with st.form(key="chat_form", clear_on_submit=True):
#             consulta = st.text_area("", placeholder="¿Con qué puedo ayudarte hoy?", label_visibility="collapsed", height=90)
            
#             c1, c2, c3 = st.columns([1, 1, 1])
#             with c2:
#                 enviar = st.form_submit_button("Generar Consulta ✨", use_container_width=True)

#         if enviar and consulta:
#             try:
#                 api_key = os.getenv("GEMINI_API_KEY")
#                 if not api_key:
#                     st.error("No se encontró la API Key en el .env")
#                 else:
#                     client = genai.Client(api_key=api_key)
                    
#                     # Definimos el esquema dinámico para el prompt
#                     current_schema = "Historial de tablas mencionadas en el chat." 
#                     system_prompt = obtener_prompt_sql(current_schema)
                    
#                     # Construir historial para Gemini
#                     history = []
#                     for m in st.session_state.messages:
#                         role = "user" if m["role"] == "user" else "model"
#                         history.append({"role": role, "parts": [{"text": m["content"]}]})

#                     # Llamada a la IA
#                     chat = client.chats.create(
#                         model="gemini-2.5-flash",
#                         config={"system_instruction": system_prompt},
#                         history=history
#                     )
                    
#                     response = chat.send_message(consulta)
                    
#                     # Guardar mensajes
#                     st.session_state.messages.append({"role": "user", "content": consulta})
#                     st.session_state.messages.append({"role": "model", "content": response.text})
                    
#                     st.rerun()

#             except Exception as e:
#                 st.error(f"Error con la IA: {e}")

#         # Opciones adicionales debajo del input
#         if st.session_state.messages:
#             col_reset, _ = st.columns([1, 3])
#             with col_reset:
#                 if st.button("🗑️ Limpiar chat", use_container_width=True):
#                     st.session_state.messages = []
#                     st.rerun()

# elif st.session_state.pagina == 'construccion':
#     st.markdown('<h1 style="text-align:center; padding-top:100px;">Próximamente... 🛠️</h1>', unsafe_allow_html=True)
#     if st.button("Volver al Inicio"):
#         st.session_state.pagina = 'inicio'
#         st.rerun()
###########################################################
#QUINTA VERSIÓN CON INTEGRACIÓN A LA API DE GEMINI
############################################################
import streamlit as st
import os
import re  # IMPORTANTE: Necesario para recuperar el formato lindo
from google import genai
from dotenv import load_dotenv
from src.prompts import obtener_prompt_sql

# 1. Cargar variables de entorno
load_dotenv()

# 2. Configuración de la página
st.set_page_config(page_title="Nexus Query", page_icon="🚀", layout="wide")

# 3. CSS Personalizado Avanzado - Estética Original + Optimización de Espacio
st.markdown("""
    <style>
    /* 1. ELIMINACIÓN DE CABECERAS Y ESPACIOS */
    header[data-testid="stHeader"] { display: none; }
    
    /* Ajuste del contenedor principal para subir todo el contenido */
    .main .block-container {
        padding-top: 2rem !important; /* Un poco de aire arriba */
        padding-bottom: 0 !important;
        max-width: 100% !important;
        margin-top: 0px !important; /* Quitamos el margen negativo para dar aire */
    }

    .stApp {
        background: linear-gradient(180deg, #2D1B4E 0%, #160D26 100%);
        color: white;
    }

    /* Título Grande y Estético (Con más espacio y centrado perfecto) */
    .titulo-principal {
        text-align: center;
        width: 100%; /* Asegura que ocupe todo el ancho disponible */
        font-size: 4rem !important;
        font-weight: 800;
        margin-top: 0px !important;
        margin-bottom: 5px !important;
        color: #FFFFFF;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.3);
        line-height: 1.2;
        display: block; /* Comportamiento de bloque para centrado correcto */
    }
    
    /* Subtítulo Estético */
    .subtitulo {
        text-align: center;
        width: 100%;
        font-size: 1.8rem !important;
        color: #B19CD9;
        margin-bottom: 20px !important;
        margin-top: 0px !important;
        font-weight: 500;
    }

    /* Descripción */
    .descripcion {
        text-align: center;
        font-size: 1.1rem;
        color: #DCD0FF;
        margin-bottom: 25px !important;
        max-width: 750px;
        margin: 0 auto;
        line-height: 1.4;
    }

    /* BURBUJAS DE CHAT */
    .chat-bubble {
        padding: 12px 16px;
        border-radius: 18px;
        margin-bottom: 25px; /* Aumentado de 10px a 25px para evitar superposición */
        line-height: 1.4;
        width: fit-content;
        max-width: 85%;
        font-size: 0.95rem;
    }
    
    .user-bubble {
        background-color: rgba(177, 156, 217, 0.25);
        border-bottom-right-radius: 5px;
        margin-left: auto;
        color: #E0B0FF;
        border-right: 4px solid #B19CD9;
    }

    .ai-bubble {
        background-color: rgba(255, 255, 255, 0.08);
        border-bottom-left-radius: 5px;
        margin-right: auto;
        color: #FFFFFF;
        border-left: 4px solid #FFFFFF;
    }

    /* ÁREA DE TEXTO (PROMPT) */
    .stTextArea textarea {
        background-color: #F0F2F6 !important;
        border-radius: 20px !important;
        border: 2px solid #B19CD9 !important;
        color: #160D26 !important;
        padding: 15px 20px !important;
        font-size: 1rem !important;
        min-height: 60px !important;
    }

    /* Botones */
    div.stButton > button, div.stFormSubmitButton > button {
        border-radius: 20px;
        border: 2px solid #B19CD9 !important;
        background-color: transparent !important;
        color: #B19CD9 !important;
        padding: 5px 20px;
        font-weight: 600;
        font-size: 0.9rem;
    }
    
    div.stButton > button:hover, div.stFormSubmitButton > button:hover {
        background-color: #B19CD9 !important;
        color: #2D1B4E !important;
    }
    
    /* Quitar espacios extra de formularios y columnas */
    [data-testid="stForm"] { border: none; padding: 0; }
    div[data-testid="stVerticalBlock"] { gap: 0rem; }
    
    /* Separador sutil */
    hr { margin: 10px 0; border: 0; border-top: 1px solid rgba(177, 156, 217, 0.2); }
    </style>
    """, unsafe_allow_html=True)

# 4. Lógica de sesión
if 'pagina' not in st.session_state: st.session_state.pagina = 'inicio'
if 'messages' not in st.session_state: st.session_state.messages = [] 

# 5. HEADER COMPACTO (Botones alineados con el margen superior)
cols_top = st.columns([8, 1, 1])
with cols_top[1]:
    if st.button("Login"): st.session_state.pagina = 'construccion'
with cols_top[2]:
    if st.button("Registro"): st.session_state.pagina = 'construccion'

# 6. Contenido Principal
if st.session_state.pagina == 'inicio':
    # Título y Subtítulo Restaurados
    st.markdown('<h1 class="titulo-principal">Nexus Query 🚀</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitulo">Traductor de Lenguaje Natural a SQL</p>', unsafe_allow_html=True)
    
    # Estructura Central
    _, col_central, _ = st.columns([1, 4, 1])
    
    with col_central:
        # Descripción Restaurada
        st.markdown('<div class="descripcion">Define tus tablas y genera consultas SQL conversando con la IA.</div>', unsafe_allow_html=True)
        
        # --- ÁREA DE CONVERSACIÓN (Scrollable) ---
        chat_container = st.container(height=250, border=False)
        
        with chat_container:
            for msg in st.session_state.messages:
                if msg["role"] == "user":
                    # Formatear saltos de línea del usuario
                    user_text = msg["content"].replace('\n', '<br>')
                    st.markdown(f'<div class="chat-bubble user-bubble"><strong>👤 Tú:</strong><br>{user_text}</div>', unsafe_allow_html=True)
                else:
                    # Detectar si es SQL antes de renderizar
                    if any(kw in msg["content"].upper() for kw in ["SELECT", "INSERT", "CREATE", "UPDATE", "DELETE"]):
                        # Si es SQL, mantenemos el comportamiento de bloque separado
                        st.markdown('<div class="chat-bubble ai-bubble"><strong>🤖 Nexus Query:</strong></div>', unsafe_allow_html=True)
                        st.code(msg["content"], language='sql')
                    else:
                        # --- MAGIA DE FORMATO AQUÍ ---
                        # Procesamos el texto para restaurar el formato lindo (Markdown a HTML manual)
                        text = msg["content"]
                        
                        # 1. Convertir **negrita** a <b>negrita</b>
                        text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
                        
                        # 2. Convertir `código` (burbuja blanca con letras verdes)
                        # Esto crea el efecto "lindo" que te gustaba
                        text = re.sub(
                            r'`([^`]*)`', 
                            r'<span style="background-color: white; color: #2e7d32; padding: 2px 6px; border-radius: 4px; font-family: monospace; font-weight: bold;">\1</span>', 
                            text
                        )
                        
                        # 3. Convertir saltos de línea
                        text = text.replace('\n', '<br>')
                        
                        st.markdown(f'<div class="chat-bubble ai-bubble"><strong>🤖 Nexus Query:</strong><br>{text}</div>', unsafe_allow_html=True)
        
        # --- ÁREA DE PROMPT (Visible sin scroll) ---
        
        with st.form(key="chat_form", clear_on_submit=True):
            # Input de altura controlada
            consulta = st.text_area("", placeholder="Escribe tu consulta aquí...", label_visibility="collapsed", height=70)
            
            # Espaciador para separar el botón del cuadro de texto
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Botón de enviar centrado
            _, btn_col, _ = st.columns([1, 1, 1])
            with btn_col:
                enviar = st.form_submit_button("Generar Consulta ✨", use_container_width=True)

        # Lógica de IA
        if enviar and consulta:
            try:
                api_key = os.getenv("GEMINI_API_KEY")
                if api_key:
                    client = genai.Client(api_key=api_key)
                    current_schema = "Historial del chat." 
                    system_prompt = obtener_prompt_sql(current_schema)
                    
                    history = []
                    for m in st.session_state.messages:
                        role = "user" if m["role"] == "user" else "model"
                        history.append({"role": role, "parts": [{"text": m["content"]}]})

                    chat = client.chats.create(
                        model="gemini-3-flash-preview",
                        config={"system_instruction": system_prompt},
                        history=history
                    )
                    
                    response = chat.send_message(consulta)
                    
                    st.session_state.messages.append({"role": "user", "content": consulta})
                    st.session_state.messages.append({"role": "model", "content": response.text})
                    st.rerun()
            except Exception as e:
                st.error(f"Error: {e}")

        # Botón Limpiar (discreto)
        if st.session_state.messages:
            if st.button("🗑️ Limpiar", use_container_width=False):
                st.session_state.messages = []
                st.rerun()

elif st.session_state.pagina == 'construccion':
    st.markdown('<h1 style="text-align:center; padding-top:100px;">Próximamente... 🛠️</h1>', unsafe_allow_html=True)
    if st.button("Volver al Inicio"):
        st.session_state.pagina = 'inicio'
        st.rerun()