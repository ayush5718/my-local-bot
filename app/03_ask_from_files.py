import sqlite3
import numpy as np
from sentence_transformers import SentenceTransformer
from llama_cpp import Llama

# ================== PATHS ==================
DB_PATH = r"E:\React projects\local-ai-assistant\embeddings\embeddings.db"
MODEL_PATH = r"E:\React projects\local-ai-assistant\model\phi-2.Q4_K_M.gguf"

# ================== LOAD MODELS ==================
# Embedding model (for searching your files)
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# Local AI model (Phi-2)
llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048,
    n_threads=6,
    verbose=False
)

# ================== UTILS ==================
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def search_chunks(question, top_k=2):
    """Find most relevant chunks for the question"""
    question_vec = embed_model.encode(question)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT chunk_text, vector FROM embeddings")

    scored = []
    for text, vec_blob in cursor.fetchall():
        vec = np.frombuffer(vec_blob, dtype=np.float32)
        score = cosine_similarity(question_vec, vec)
        scored.append((score, text))

    conn.close()

    scored.sort(key=lambda x: x[0], reverse=True)
    return [text for _, text in scored[:top_k]]

# ================== ASK QUESTION ==================
question = "What is my name?"

relevant_chunks = search_chunks(question)

context = "\n".join(relevant_chunks)

prompt = f"""
You are a local AI assistant.
You must answer ONLY using the context provided.
Do not explain.
Do not write code.
If the answer is not found, say "Not found".

Context:
{context}

Question:
{question}

Answer:
"""

response = llm(prompt, max_tokens=80)
print(response["choices"][0]["text"].strip())
