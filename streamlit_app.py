import openai
import streamlit as st
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")


def analyze_case():
    case_info = st.text_input("Enter the information about the legal case you want to analyze")
    document1 = st.file_uploader("Upload first document")
    document2 = st.file_uploader("Upload second document")
    document3 = st.file_uploader("Upload third document")
    if st.button("Analyze"):
        if document1 and document2 and document3:
            try:
                doc1 = open(document1, 'r').read()
                doc2 = open(document2, 'r').read()
                doc3 = open(document3, 'r').read()
            except:
                st.error("Some error occurred while reading the document")
                return
            prompt = f'Analyze a legal case according to Guatemalan legislation using the following documents: {doc1}, {doc2}, {doc3}. {case_info}'
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
            st.error("Please upload all the required documents")

st.title("Legal case analyzer")
st.write("Enter information about the legal case you want to analyze and upload the required documents, then press the 'Analyze' button")
analyze_case()
