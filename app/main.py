# main.py
from fastapi import FastAPI, UploadFile
from utils import extract_text_from_pdf, embed_text, create_faiss_index
from rag import generate_answer

app = FastAPI()

# Example: store embeddings and FAISS index globally for demo
FAISS_INDEX = None
CHUNKS = []

@app.post("/upload_pdf/")
async def upload_pdf(file: UploadFile):
    content = await file.read()
    with open(f"data/{file.filename}", "wb") as f:
        f.write(content)
    text = extract_text_from_pdf(f"data/{file.filename}")
    
    # Split text into chunks
    global CHUNKS, FAISS_INDEX
    CHUNKS = [text[i:i+500] for i in range(0, len(text), 500)]
    print(f"Number of chunks: {len(CHUNKS)}")
    print(f"First chunk preview:\n{CHUNKS[0]}")

    embeddings = embed_text(CHUNKS)
    FAISS_INDEX = create_faiss_index(embeddings)
    
    return {"text_preview": text[:300]}

@app.post("/ask_question/")
async def ask_question(question: str):
    global CHUNKS, FAISS_INDEX
    if FAISS_INDEX is None:
        return {"answer": "No document uploaded yet."}

    # Retrieve top chunk
    query_embedding = embed_text([question])
    D, I = FAISS_INDEX.search(query_embedding, k=1)
    top_chunk = CHUNKS[I[0][0]]

    # Generate answer using LLM
    answer = generate_answer(question, top_chunk)
    return {"answer": answer}
