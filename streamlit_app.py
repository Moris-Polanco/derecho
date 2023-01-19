import openai
import streamlit as st
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

def analyze_case():
    case_info = st.text_input("Enter the information about the legal case you want to analyze")
    if st.button("Analyze"):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f'Analyze a legal case according to Guatemalan legislation {case_info}',
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )
        st.success(response["choices"][0]["text"])
        if st.button("Success"):
            st.success("The case has been successfully analyzed")

st.title("Legal case analyzer")
st.write("Enter information about the legal case you want to analyze and press the 'Analyze' button")
analyze_case()
