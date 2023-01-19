import openai
import streamlit as st
import os
import requests
from bs4 import BeautifulSoup


openai.api_key = os.environ.get("OPENAI_API_KEY")


def analyze_case():
    case_info = st.text_input("Enter the information about the legal case you want to analyze")
    query = st.text_input("Enter the search query")
    if st.button("Analyze"):
        if query:
            try:
                google_url = f"https://www.google.com/search?q={query}"
                page = requests.get(google_url)
                soup = BeautifulSoup(page.content, "html.parser")
                links = soup.find_all("a")
                links = [link.get("href") for link in links if link.get("href").startswith("/url?q=")]
                if links:
                    doc = requests.get(links[0]).text
                else:
                    st.warning("No results found")
                    return
            except:
                st.error("An error occurred while searching the query")
                return
            prompt = f'Analyze a legal case according to Guatemalan legislation using the following search query: {doc}. {case_info}'
            response = openai.Completion.create(
                engine="text-davinci-003",
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
                st.error("Please enter a search query")

    st.title("Legal case analyzer")
    st.write("Enter information about the legal case you want to analyze and enter the search query, then press the 'Analyze' button")
    analyze_case()
