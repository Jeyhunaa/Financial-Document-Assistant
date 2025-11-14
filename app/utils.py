# utils.py
import PyPDF2
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

# PDF extraction
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text()
    return text

# Embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text(chunks):
    embeddings = model.encode(chunks)
    return embeddings.astype("float32")

# FAISS index creation
def create_faiss_index(embeddings):
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return index
