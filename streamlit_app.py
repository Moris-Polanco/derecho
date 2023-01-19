import openai
import streamlit as st
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

def analyze_case():
    case_info = st.text_input("Enter the information about the legal case you want to analyze")
    document = st.file_uploader("Upload document")
    if st.button("Analyze"):
        if document:
            try:
                doc = open(document, 'r').read()
            except:
                st.error("An error occurred while reading the document")
                return
            prompt = f'Analyze a legal case according to Guatemalan legislation using the following document: {doc}. {case_info}'
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
            st.error("Please upload the required document")

st.title("Legal case analyzer")
st.write("Enter information about the legal case you want to analyze and upload the required document, then press the 'Analyze' button")
analyze_case()
