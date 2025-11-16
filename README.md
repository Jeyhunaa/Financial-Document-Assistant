<<<<<<< HEAD
# RAG-Based Financial Document Assistant

## Project Overview
This project implements a **Retrieval-Augmented Generation (RAG)** system to extract information from financial documents such as invoices and contracts. Users can upload a PDF, and the system answers questions based on the document content using embeddings, FAISS, and a language model.  

**Key Features:**
- PDF text extraction with `PyPDF2`
- Text embedding using `SentenceTransformers`
- Retrieval of relevant chunks via `FAISS`
- Question answering using a small LLM (`Flan-T5-small`)
- FastAPI backend for API endpoints
- Dockerized for easy deployment  

---

## Project Structure
rag_financial_assistant/
├─ app/
│   ├─ main.py           # FastAPI app
│   ├─ utils.py          # PDF extraction & embeddings
│   ├─ rag.py            # RAG pipeline with LLM
│   ├─ requirements.txt  # Python dependencies
├─ data/
│   └─ sample_pdf.pdf    # Sample financial document
├─ Dockerfile            # Docker container
└─ README.md


=======
# Financial-Document-Assistant
>>>>>>> 1be61b5711159b1e0f097288cab24949ffb0acca
