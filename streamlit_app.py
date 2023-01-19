import openai
import streamlit as st
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")



def analizar_caso():
    informacion_caso = st.text_input("Ingrese la información sobre el caso legal que desea analizar")
    if st.button("Analizar"):
        respuesta = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f'Analizar un caso legal de acuerdo con la legislación guatemalteca, incluyendo la cita de la ley violada y la pena merecida. Si no se puede citar la ley, indicar que el análisis no se puede realizar. {informacion_caso}',
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )
        if 'no se puede citar la ley' in respuesta["choices"][0]["text"]:
            st.warning(respuesta["choices"][0]["text"])
        else:
            st.success(respuesta["choices"][0]["text"])
        if st.button("Exito"):
            st.success("El caso ha sido analizado con éxito")

st.title("Analizador de casos legales")
st.write("Ingrese información sobre el caso legal que desea analizar y presione el botón 'Analizar'")
analizar_caso()
