# app.py – DocuLens AI: Legal & Compliance Document Analyzer

import streamlit as st
from PyPDF2 import PdfReader
import ollama
import re

# --- Extract text from uploaded PDF ---
def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

# --- Create LLM Prompt ---
def create_prompt(document_text):
    prompt = f"""
You are a legal and compliance document analyzer AI. Given the following content, do the following:
1. Extract key clauses: Governing Law, Termination, Liability, Confidentiality, Force Majeure, Indemnity
2. Identify and list missing clauses
3. Highlight any risky or vague terms
4. Output the result in JSON format with fields: Governing Law, Termination, Liability, Confidentiality, Force Majeure, Indemnity, Missing Clauses, Risky Terms

Document:
{document_text[:4000]}
"""
    return prompt

# --- Query Ollama with LLaMA3 ---
def analyze_with_llm(prompt):
    response = ollama.chat(model="llama3", messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

# --- Streamlit UI ---
st.set_page_config(page_title="DocuLens AI", layout="wide")
st.title("🧾 DocuLens AI – Legal & Compliance Document Analyzer")

uploaded_file = st.file_uploader("Upload Legal Document (PDF)", type=["pdf"])
if uploaded_file:
    with st.spinner("Extracting text from document..."):
        document_text = extract_text_from_pdf(uploaded_file)
        st.success("Document text extracted successfully.")

    if st.button("🔍 Analyze Legal Document"):
        with st.spinner("Analyzing with Legal LLM Agent..."):
            prompt = create_prompt(document_text)
            result = analyze_with_llm(prompt)
            st.markdown("### 📋 Clause Summary & Risk Report")
            st.code(result, language='json')
else:
    st.info("Please upload a PDF document to begin analysis.")
