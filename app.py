import os
import streamlit as st
from openai import OpenAI
import pandas as pd

# Leer API key del entorno
#api_key = os.getenv("OPENAI_API_KEY")
# Leer API key del entorno
api_key = OPENAI_API_KEY

if not api_key:
    st.error("❌ No se encontró la clave de API. Asegúrate de configurarla en GitHub o Streamlit.")
else:
    client = OpenAI(api_key=api_key)

    # Cargar datos
    df = pd.read_csv('vgsales.csv')
    df_subset = df.head(100)
    df_string = df_subset.to_string()

    st.title("🎮 Asistente de Videojuegos")

    pregunta = st.text_input("Haz una pregunta sobre los videojuegos:")

    if pregunta:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": (
                    "Eres un asistente experto en videojuegos. "
                    "Usa ÚNICAMENTE los siguientes datos para responder preguntas. "
                    "Si la pregunta no está relacionada con los datos, responde: "
                    "'Lo siento, esa pregunta no está relacionada con los datos disponibles.'\n\n"
                    + df_string
                )},
                {"role": "user", "content": pregunta}
            ]
        )

        st.subheader("Respuesta:")
        st.write(response.choices[0].message.content)
