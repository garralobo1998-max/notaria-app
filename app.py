import streamlit as st
from streamlit_lottie import st_lottie
import requests
import datetime
import os

# Configuración de página
st.set_page_config(page_title="Notaría Matta Núñez - Autorización de Viajes", layout="wide")

# Función para cargar animaciones Lottie
def load_lottieurl(url: str):
    try:
        r = requests.get(url, timeout=3)
        if r.status_code == 200:
            return r.json()
    except:
        return None
    return None

lottie_assistant = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_vnikbew6.json")

# Estilos visuales con fondo temático notarial y colores corporativos
st.markdown("""
    <style>
    /* Fondo general con degradado institucional */
    .stApp {
        background: linear-gradient(135deg, #1d2a44 0%, #2c3e50 50%, #8B0000 100%) !important;
    }
    
    /* Contenedor principal con tarjetas redondeadas */
    div[data-testid="stVerticalBlock"] > div {
        background-color: rgba(255, 255, 255, 0.96);
        border-radius: 12px;
        padding: 10px;
    }

    h1, h2, h3 { color: #1d2a44 !important; font-family: 'Segoe UI', Tahoma, sans-serif; }
    .stSubheader { color: #8B0000 !important; border-bottom: 2px solid #8B0000; padding-bottom: 4px; margin-top: 15px; }
    
    /* Tarjeta del Asistente Virtual */
    .assistant-card { 
        background: #ffffff; 
        padding: 20px; 
        border-radius: 12px; 
        border-left: 6px solid #8B0000; 
        box-shadow: 0px 4px 12px rgba(0,0,0,0.15); 
        text-align: center; 
    }
    
    .stButton>button { 
        background-color: #1d2a44 !important; 
        color: white !important; 
        border-radius: 8px !important; 
        font-weight: bold !important; 
        border: none !important; 
        width: 100%; 
        padding: 10px;
    }
    .stButton>button:hover { background-color: #8B0000 !important; }
    </style>
""", unsafe_allow_html=True)

# Encabezado Notarial
st.markdown("<h2 style='text-align: center; color: #1d2a44;'>NOTARÍA MATTA NÚÑEZ - PISCO</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #8B0000;'>Autorización Notarial para Viaje de Menores al Interior del País</h4>", unsafe_allow_html=True)
st.divider()

# Estado de sesión para manejar el borrador
if "borrador_generado" not in st.session_state:
    st.session_state.borrador_generado = False
if "texto_doc" not in st.session_state:
    st.session_state.texto_doc = ""
if "cliente_nombre" not in st.session_state:
    st.session_state.cliente_nombre = ""

col_asistente, col_form = st.columns([1.2, 2])

with col_asistente:
    st.markdown('<div class="assistant-card">', unsafe_allow_html=True)
    st.markdown("### 🤖 Asistente Virtual")
    if lottie_assistant:
        st_lottie(lottie_assistant, height=200, key="assistant_anim")
    elif os.path.exists("asistente.png"):
        st.image("asistente.png", use_container_width=True)
    else:
        st.info("🤖 **Sofía - Asistente Notarial**")
    st.info("👋 **¡Hola! Soy Sofía.**\n\nIngresa los datos para generar la vista previa del borrador.")
    st.markdown('</div>', unsafe_allow_html=True)

with col_form:
    with st.form("form_autorizacion"):
        st.subheader("1. Datos del Trámite Notarial")
        c1, c2 = st.columns(2)
        ciudad = c1.text_input("Ciudad del Trámite", value="Pisco", disabled=True)
        num_kardex = c2.text_input("Número de Kardex / Acta", value="I194-2025", disabled=False)
        notario_nom = c1.text_input("Nombre del Notario", value="Oscar Diego Matta Núñez", disabled=True)
        notario_dir = c2.text_input("Dirección Notaría", value="Calle Independencia N° 171-A, del Distrito y Provincia de Pisco, Departamento de Ica", disabled=True)

        st.subheader("2. Datos de él/los Autorizantes")
        opcion_padres = st.radio("¿Quién autoriza el viaje?", ["Solo la Madre", "Solo el Padre", "Ambos Padres"], horizontal=True)

        m_nombre, m_doc, m_domicilio = "", "", ""
        p_nombre, p_doc, p_domicilio = "", "", ""

        if opcion_padres in ["Solo la Madre", "Ambos Padres"]:
            st.markdown("**Datos de la Madre**")
            cm1, cm2 = st.columns(2)
            m_nombre = cm1.text_input("Nombre Completo de la Madre", value="ARACELI ROSA MOREYRA ASCONA")
            m_doc = cm2.text_input("DNI / Pasaporte de la Madre", value="46191097")
            m_domicilio = st.text_input("Domicilio Completo de la Madre", value="C.Poblado Alto Anama Mz. B Lt 10, del Distrito de Humay, Provincia de Pisco, Departamento de Ica")

        if opcion_padres in ["Solo el Padre", "Ambos Padres"]:
            st.markdown("**Datos del Padre**")
            cp1, cp2 = st.columns(2)
            p_nombre = cp1.text_input("Nombre Completo del Padre")
            p_doc = cp2.text_input("DNI / Pasaporte del Padre")
            p_domicilio = st.text_input("Domicilio Completo del Padre")

        st.subheader("3. Datos del Menor")
        ch1, ch2, ch3 = st.columns([2, 1, 1])
        hijo_nombre = ch1.text_input("Nombre Completo del Menor", value="MARYORI LISBETH JIMENEZ MOREYRA")
        hijo_doc = ch2.text_input("DNI del Menor", value="60709169")
        hijo_edad_num = ch3.text_input("Edad en números", value="16")
        hijo_edad_texto = ch3.text_input("Edad en letras", value="Dieciséis")
        hijo_genero = st.radio("Género del Menor", ["Hijo", "Hija"], horizontal=True)

        st.subheader("4. Detalle del Viaje")
        ruta = st.text_input("Ruta de Viaje", value="Humay – Pisco – Lima – Tarapoto y viceversa.")
        via_transporte = st.text_input("Vía de Transporte", value="Terrestre y/o aérea.")
        motivo = st.text_input("Motivo del Viaje", value="Viaje de promoción.")
        
        cf1, cf2 = st.columns(2)
        f_salida = cf1.text_input("Fecha de Salida", value="26 de Setiembre de 2025.")
        f_retorno = cf2.text_input("Fecha de Retorno", value="01 de octubre de 2025.")

        st.subheader("5. Condición del Viaje")
        condicion_viaje = st.radio("¿El menor viaja solo o acompañado?", ["Viaja Solo", "Viaja Acompañado"], index=1, horizontal=True)

        acomp_info = ""
        if condicion_viaje == "Viaja Acompañado":
            ca1, ca2, ca3 = st.columns([1, 2, 1])
            vinculo = ca1.text_input("Vínculo", value="su profesora doña")
            acomp_nom = ca2.text_input("Nombre del Acompañante", value="LIDIA STEPHANY CAMPOS MONRROY")
            acomp_doc = ca3.text_input("DNI Acompañante", value="46121031")
            art_m = "EL MENOR" if hijo_genero == "Hijo" else "LA MENOR"
            acomp_info = f"{art_m} viajará acompañado de {vinculo}: {acomp_nom} identificada con Documento Nacional de Identidad N° {acomp_doc}, quien será responsable del viaje y estadía del menor. " + "⎯" * 15
        else:
            art_m = "EL MENOR" if hijo_genero == "Hijo" else "LA MENOR"
            acomp_info = f"{art_m} viajará solo(a) bajo la responsabilidad de la empresa de transporte. " + "⎯" * 20

        btn_generar = st.form_submit_button("👁️ Generar Borrador para Revisión del Cliente")

# Cálculo de Avance (0% inicial)
pasos_completados = 0
if m_nombre or p_nombre: 
    pasos_completados += 1
if hijo_nombre and hijo_doc: 
    pasos_completados += 1
if ruta and f_salida: 
    pasos_completados += 1
if condicion_viaje: 
    pasos_completados += 1

porcentaje_avance = int((pasos_completados / 4) * 100)

with col_asistente:
    st.write("")
    st.markdown(f"**Progreso de Formulario: {porcentaje_avance}%**")
    st.progress(porcentaje_avance / 100)

# ACCIÓN: GENERAR BORRADOR EXACTO
if btn_generar:
    texto_comparecientes = []
    lista_firmas = []

    if m_nombre:
        texto_comparecientes.append(f"LA MADRE: {m_nombre}, de nacionalidad peruana, identificada con Documento Nacional de Identidad número {m_doc}, con domicilio para estos efectos en {m_domicilio}, quien interviene por su propio derecho. " + "⎯" * 10)
        lista_firmas.append((m_nombre, m_doc, "MADRE"))
    if p_nombre:
        texto_comparecientes.append(f"EL PADRE: {p_nombre}, de nacionalidad peruana, identificado con Documento Nacional de Identidad número {p_doc}, con domicilio para estos efectos en {p_domicilio}, quien interviene por su propio derecho. " + "⎯" * 10)
        lista_firmas.append((p_nombre, p_doc, "PADRE"))

    comp_str = "\n".join(texto_comparecientes)
    
    fecha_hoy = datetime.datetime.now()
    meses_es = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Setiembre", "Octubre", "Noviembre", "Diciembre"]
    f_emision_str = f"Ciudad de Pisco, {fecha_hoy.day:02d} de {meses_es[fecha_hoy.month - 1]} del {fecha_hoy.year}."

    doc_final = f"""DOCUMENTO NOTARIAL EXTRAPROTOCOLAR

SERIE D N° 02752989

Autorización para Viaje de Menores al
Interior del País
{num_kardex}

**************************************************Kathy**************************************************
En la ciudad de Pisco, al Primer día del mes de Agosto del año Dos Mil Veinticinco, Yo: {notario_nom}, Abogado – Notario de la Provincia de Pisco, con Oficio Notarial en {notario_dir}, extiendo la presente acta de Autorización de Viaje de Menor en la que comparece: ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
{comp_str}
De conformidad con lo señalado en el artículo 111° del Código de los Niños y Adolescentes, Ley número 27337, autorizo el viaje de mi menor {hijo_genero.lower()}: {hijo_nombre}, con {hijo_edad_num} ({hijo_edad_texto}) años de edad, identificada con Documento Nacional de Identidad número {hijo_doc}. ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
Ruta de Viaje: {ruta} ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
Vía: {via_transporte} ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
Motivo: {motivo} ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
Fecha de viaje: ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
    •   SALIDA: {f_salida} ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
    •   RETORNO: {f_retorno} ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
Observaciones: ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
{acomp_info}
Este permiso no autoriza la adopción de la menor, ni tiene valor para iniciar trámite judicial alguno. ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
La compareciente lee este documento, y declara bajo juramento que la información proporcionada al Notario es verdadera y que se asume toda la responsabilidad que de él emane, se ratifica en su contenido y lo firma en mi presencia, de todo cuanto doy fe. ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯

                                                                                 1
                                                    {f_emision_str}

"""
    for nom, doc, rol in lista_firmas:
        doc_final += f"\n________________________________________\n{nom}\nDNI. N° {doc}\n"

    st.session_state.texto_doc = doc_final
    st.session_state.cliente_nombre = hijo_nombre if hijo_nombre else "Trámite_Nuevo"
    st.session_state.borrador_generado = True

# VISTA DE BORRADOR Y CONFIRMACIÓN POR EL CLIENTE
if st.session_state.borrador_generado:
    st.divider()
    st.subheader("📜 REVISIÓN DE BORRADOR - VISTA DEL CLIENTE")
    st.info("Por favor, revise detenidamente los datos del borrador antes de confirmar.")
    
    st.text_area("Borrador del Documento Notarial:", value=st.session_state.texto_doc, height=450)

    c_btn1, c_btn2 = st.columns(2)
    with c_btn1:
        btn_confirmar = st.button("✅ CONFIRMAR Y ENVIAR A NOTARÍA")
    with c_btn2:
        st.download_button(
            label="⬇️ Descargar Borrador TXT",
            data=st.session_state.texto_doc,
            file_name=f"Borrador_Autorizacion_{st.session_state.cliente_nombre}.txt",
            mime="text/plain"
        )

    # ACCIÓN AL CONFIRMAR
    if btn_confirmar:
        hora_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        registro_alerta = f"[{hora_actual}] ¡NUEVO TRÁMITE CONFIRMADO! - Menor: {st.session_state.cliente_nombre} - Kardex: {num_kardex}\n"
        
        with open("alertas_notaria.txt", "a", encoding="utf-8") as f:
            f.write(registro_alerta)

        st.balloons()
        st.success(f"🔔 **¡AVISO ENVIADO A LA PC DE LA NOTARÍA!**\n\nEl cliente ha verificado y aceptado el borrador correctamente ({hora_actual}).")
        st.toast("🚨 ¡Alerta enviada a la terminal del sistema notarial!", icon="🔔")