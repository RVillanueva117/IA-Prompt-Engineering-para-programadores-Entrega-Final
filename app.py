import streamlit as st
import requests

# ----------------------------
# Configuración general
# ----------------------------
st.set_page_config(
    page_title="VegStart",
    page_icon="🥗",
    layout="centered"
)

st.title("🥗 VegStart")
st.caption("Asistente con IA local (Ollama) para dar los primeros pasos en alimentación vegetariana")

# ----------------------------
# Configuración Ollama
# ----------------------------
OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2:3b"

SYSTEM_PROMPT = """
Actuá como un acompañante/nutricionista para personas que quieren comenzar
una alimentación vegetariana.

Tu enfoque:
- Simple
- Práctico
- Accesible
- Sin tecnicismos

Usá lenguaje claro, comidas fáciles y alternativas económicas.
Al final agregá siempre:
"Esto no reemplaza la consulta con un profesional de la salud."
""".strip()


def ollama_chat(messages, model=MODEL, num_predict=300):
    """
    Llama a Ollama /api/chat. Ajusta num_predict para evitar respuestas truncadas.
    """
    payload = {
        "model": model,
        "messages": messages,
        "stream": False,
        "options": {
            "temperature": 0.3,
            "top_p": 0.9,
            "num_predict": num_predict,
        },
    }

    r = requests.post(OLLAMA_URL, json=payload, timeout=300)  # 5 min por seguridad
    r.raise_for_status()
    return r.json()["message"]["content"]


# ----------------------------
# Formulario de usuario
# ----------------------------
with st.form("perfil"):
    col1, col2 = st.columns(2)

    with col1:
        edad = st.number_input("Edad", min_value=10, max_value=100, value=30)
        actividad = st.selectbox("Nivel de actividad", ["Baja", "Media", "Alta"])
        experiencia = st.selectbox(
            "Experiencia vegetariana",
            ["Cero (recién empiezo)", "Algo (a veces)", "Ya vegetariano/a"]
        )

    with col2:
        objetivo = st.selectbox(
            "Objetivo principal",
            ["Empezar sin complicarme", "Comer más saludable", "Ahorrar", "Subir proteínas", "Bajar ultraprocesados"]
        )
        presupuesto = st.selectbox("Presupuesto", ["Bajo", "Medio", "Alto"])
        horizonte = st.selectbox("Qué querés recibir", ["Plan diario", "Plan semanal"])

    gustos = st.text_input("Gustos / comidas que te gustan (ej: pastas, empanadas, ensaladas...)")
    restricciones = st.text_input("Restricciones (ej: sin gluten, sin lácteos, alergias...)")
    extras = st.text_area("Extras (tiempo para cocinar, cocina simple, horarios, etc.)", height=90)

    submit = st.form_submit_button("Generar plan con IA (local)")


# ----------------------------
# Generación del plan
# ----------------------------
if submit:
    # num_predict dinámico: semanal necesita más tokens para no truncar
    num_predict = 300 if horizonte == "Plan diario" else 1200

    # Formato dinámico
    if horizonte == "Plan semanal":
        formato_plan = """
2) Plan semanal (OBLIGATORIO: incluir los 7 días completos: lunes, martes, miércoles, jueves, viernes, sábado, domingo).
   Formato compacto por día:
   - Día: Desayuno | Almuerzo | Merienda | Cena
"""
    else:
        formato_plan = """
2) Plan diario:
   - Desayuno
   - Almuerzo
   - Merienda
   - Cena
"""

    user_msg = f"""
DATOS DEL USUARIO
- Edad: {edad}
- Actividad: {actividad}
- Experiencia: {experiencia}
- Objetivo: {objetivo}
- Presupuesto: {presupuesto}
- Horizonte: {horizonte}
- Gustos: {gustos or "No especificado"}
- Restricciones: {restricciones or "No especificado"}
- Extras: {extras or "No especificado"}

FORMATO DE RESPUESTA (obligatorio)
1) Resumen en 3 líneas (simple)
{formato_plan}
3) 5 proteínas vegetales + cómo usarlas
4) Lista de compras corta (10-15 items)
5) Aclaración final: no reemplaza consulta profesional
""".strip()

    with st.spinner("Generando tu plan con IA local (Ollama)..."):
        try:
            answer = ollama_chat(
                [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_msg},
                ],
                num_predict=num_predict
            )

            st.success("Listo ✅")
            st.subheader("🍽️ Tu plan generado con IA")
            st.markdown(answer)

        except requests.exceptions.ConnectionError:
            st.error("No pude conectarme a Ollama (localhost:11434).")
            st.info("Asegurate de que Ollama esté instalado y corriendo. Probá en otra terminal: `ollama run llama3.2:3b`.")
        except requests.exceptions.ReadTimeout:
            st.error("La respuesta tardó demasiado y se agotó el tiempo de espera.")
            st.info("Probá de nuevo, o usá un modelo más liviano / reducí el nivel de detalle.")
        except Exception as e:
            st.error("Error inesperado al generar respuesta.")
            st.code(str(e))



