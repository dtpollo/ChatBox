import streamlit as st
from openai import OpenAI
import pandas as pd
import os

# --- Campo para ingresar la API Key ---
api_key = st.text_input("🔑 Ingresa tu OpenAI API Key:", type="password")

if api_key:
    os.environ["OPENAI_API_KEY"] = api_key
    client = OpenAI()
else:
    st.warning("Por favor, ingresa tu API Key para continuar.")
    st.stop()

# --- Cargar dataset ---
df = pd.read_csv("vgsales.csv")

# Tomar solo los primeros 100 registros
df_subset = df.head(100)
df_string = df_subset.to_string()

# --- Interfaz principal ---
st.title("🎮 Asistente de Videojuegos")

# Campo de pregunta
user_input = st.text_input("Escribe tu pregunta sobre los videojuegos:")

# --- Lógica principal ---
if user_input:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "Eres un asistente experto en videojuegos. "
                    "Usa ÚNICAMENTE la información del siguiente dataset para responder preguntas. "
                    "Si la pregunta no está relacionada con los datos, responde con: "
                    "'Lo siento, esa pregunta no está relacionada con los datos disponibles.'\n\n"
                    "Aquí están los primeros 100 registros del dataset:\n" + df_string
                )
            },
            {"role": "user", "content": user_input}
        ]
    )

    # Mostrar respuesta
    answer = response.choices[0].message.content
    st.subheader("Respuesta:")
    st.write(answer)
