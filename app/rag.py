# rag.py
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load LLM
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")

def generate_answer(question, retrieved_text):
    input_text = f"Answer the question based on the context below.\nContext: {retrieved_text}\nQuestion: {question}"
    inputs = tokenizer(input_text, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=200)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer