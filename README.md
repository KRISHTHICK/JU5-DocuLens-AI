# JU5-DocuLens-AI
GEN AI

:

🧾 DocuLens AI – Legal & Compliance Document Analyzer
🧠 What It Does
DocuLens AI helps legal, compliance, and audit teams by:

Analyzing contracts, terms of service, NDAs, or policy documents

Extracting key clauses and obligations

Detecting risky or missing clauses using LLMs

Flagging non-compliance or unusual terms

⚙️ Key Features
Feature	Description
📄 Upload Contract / Legal Document	Accepts PDF/DOCX
📚 Clause Extraction	Extracts key clauses (Jurisdiction, Liability, Termination, Confidentiality, Force Majeure, etc.)
⚠️ Risk Detection	Flags clauses with vague language or excessive liability
🔍 Clause Comparison	Compares uploaded doc to company template
📊 Clause Summary Table	Presents extracted data in a table
💬 Natural Language QA	Ask “What is the governing law in this contract?” or “Who is liable for delays?”

📘 README.md
markdown
Copy
Edit
# 🧾 DocuLens AI – Legal & Compliance Document Analyzer

DocuLens AI is an LLM-powered tool to analyze contracts, NDAs, and compliance documents. It extracts legal clauses, identifies missing or risky terms, and outputs a structured summary.

## 🚀 Features

- Upload legal documents (PDF)
- Extract clauses: Termination, Confidentiality, Liability, etc.
- Detect missing sections (e.g., Force Majeure)
- Highlight vague or risky phrases using LLM
- Show everything in structured JSON format

## 🛠️ Setup Instructions

1. Clone the repo:
```bash
git clone https://github.com/yourusername/doculens-ai.git
cd doculens-ai
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Pull LLaMA model with Ollama:

bash
Copy
Edit
ollama pull llama3
Run the app:

bash
Copy
Edit
streamlit run app.py
🧪 Sample Test
Use the sample_docs/nda_sample.pdf to try it out.
