import openai
import streamlit as st
import os
import requests

openai.api_key = os.environ.get("OPENAI_API_KEY")

def analyze_case():
    case_info = st.text_input("Enter the information about the legal case you want to analyze")
    url = st.text_input("Enter the URL of the webpage you want to analyze")
    if st.button("Analyze"):
        if url:
            try:
                page = requests.get(url)
                doc = page.text
            except:
                st.error("An error occurred while reading the webpage")
                return
            prompt = f'Analyze a legal case according to Guatemalan legislation using the following webpage: {doc}. {case_info}'
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.7,
            )
            if 'unable to cite the law' in response["choices"][0]["text"]:
                st.warning(response["choices"][0]["text"])
            else:
                st.success(response["choices"][0]["text"])
            if st.button("Success"):
                st.success("The case has been successfully analyzed")
        else:
            st.error("Please enter the URL of the webpage")

st.title("Legal case analyzer")
st.write("Enter information about the legal case you want to analyze and enter the URL of the webpage, then press the 'Analyze' button")
analyze_case()
