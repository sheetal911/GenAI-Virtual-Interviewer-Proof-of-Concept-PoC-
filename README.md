# GenAI Virtual Interviewer - Proof of Concept

This POC demonstrates a GenAI-based virtual interviewer that:
- Conducts adaptive interviews using LLMs.
- Scores candidates.
- Extracts structured data from PDF resumes/tables.
- Supports a modular architecture for future multimodal integrations.

## Folders
- `src/`: Source code for AI agents and PDF processing.
- `docs/`: Contains PDF documentation and system diagram.

## Tech Stack
- Python
- LangChain
- OpenAI / Cohere / Claude APIs
- PyMuPDF / pdfplumber / camelot (PDF parsing)
- Streamlit / Flask (optional UI)
- GitHub for version control

## Instructions
1. Fill in the `API_KEY` in environment variables.
2. Run `agent_chain.py` to simulate a mock interview.
3. Use `table_extraction.py` to parse structured data from a PDF.

langchain
openai
pdfplumber
camelot-py[cv]
PyMuPDF
flask
streamlit

