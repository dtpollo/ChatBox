import streamlit as st
from openai import OpenAI
import pandas as pd
import os

# API
os.environ['OPENAI_API_KEY'] = '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'

# Init
client = OpenAI()

# Import dataset
df = pd.read_csv('vgsales.csv')

# Keep only first 100 rows
df_subset = df.head(100)

# Convert those 100 rows to string
df_string = df_subset.to_string()

# Tittle
st.title("🎮 Asistente de Videojuegos")

# Questions
user_input = st.text_input("Escribe tu pregunta sobre los videojuegos:")

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
