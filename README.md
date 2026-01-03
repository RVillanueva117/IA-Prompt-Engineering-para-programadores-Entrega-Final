# 🥗 VegStart — App de IA para iniciar una alimentación vegetariana

VegStart es una aplicación web desarrollada con **Streamlit** que utiliza **IA local** (mediante **Ollama**) para generar planes de alimentación vegetariana simples, prácticos y accesibles para personas que están dando sus primeros pasos.

Este proyecto fue desarrollado como **entrega final** del módulo  
**“IA Prompt Engineering para programadores”**.

---

## 🎯 Objetivo del proyecto

Demostrar el uso práctico de herramientas de **Inteligencia Artificial** en una aplicación real, integrando:

- Prompt Engineering
- Modelos de lenguaje (LLM)
- Aplicaciones web simples
- IA ejecutándose de forma **local**, sin depender de APIs de pago

---

## 🚀 Funcionalidades

La app permite generar:

- ✅ **Plan diario** o **plan semanal**
- 🍽️ Desayuno, almuerzo, merienda y cena
- 💰 Opciones económicas y simples
- 🥬 Recomendaciones según:
  - Edad
  - Nivel de actividad
  - Experiencia vegetariana
  - Presupuesto
  - Gustos personales
  - Restricciones alimentarias (ej. sin gluten)

Además incluye:
- Lista de compras
- Fuentes de proteínas vegetales
- Aclaración profesional de salud

---

## 🧠 Tecnologías utilizadas

- **Python 3**
- **Streamlit** (interfaz web)
- **Ollama** (IA local)
- **Modelo LLM**: `llama3.2:3b`
- **Requests** (comunicación HTTP)

---

## 🖥️ Requisitos previos

Antes de ejecutar la app necesitás:

1. **Python 3.10+**
2. **Ollama instalado y funcionando**
   - https://ollama.com
3. Descargar el modelo:
   ```bash
   ollama pull llama3.2:3b


⚙️ Instalación y ejecución
1️⃣ Clonar el repositorio
git clone https://github.com/RVillanueva17/IA-Prompt-Engineering-para-programadores-Entrega-Final.git
cd IA-Prompt-Engineering-para-programadores-Entrega-Final

2️⃣ Crear y activar entorno virtual
python -m venv .venv


Windows (PowerShell):

.venv\Scripts\Activate.ps1

3️⃣ Instalar dependencias
pip install -r requirements.txt

4️⃣ Ejecutar la aplicación
streamlit run app.py


La app se abrirá automáticamente en el navegador en:

http://localhost:8501

🧪 Ejecución local con IA

VegStart no utiliza APIs externas.
Toda la inferencia se realiza localmente a través de Ollama, lo que permite:

No depender de cuotas

No usar claves privadas

Ejecutar el proyecto sin conexión a servicios pagos

⚠️ Aclaración importante

Esta aplicación no reemplaza la consulta con un/a profesional de la salud o nutrición.
Su objetivo es educativo y orientativo.

👨‍💻 Autor

Rodrigo Villanueva
CoderHouse — Diplomatura en Data Science
IA Prompt Engineering para programadores
