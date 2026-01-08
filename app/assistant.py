import sqlite3
import numpy as np
from sentence_transformers import SentenceTransformer
from llama_cpp import Llama

DB_PATH = r"E:\React projects\local-ai-assistant\embeddings\embeddings.db"
MODEL_PATH = r"E:\React projects\local-ai-assistant\model\phi-2.Q4_K_M.gguf"

# Load models ONCE
print("Loading models... please wait")

embed_model = SentenceTransformer("all-MiniLM-L6-v2")

llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048,
    n_threads=6,
    verbose=False
)

print("Assistant ready. Type 'exit' to quit.\n")

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def search_chunks(question, top_k=2):
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


def ask_ai(question):
    relevant_chunks = search_chunks(question)
    context = "\n".join(relevant_chunks)

    prompt = f"""
You are a local AI assistant.
Answer ONLY from the context.
Do not explain.
Do not write code.
If not found, say "Not found".

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm(prompt, max_tokens=100)
    return response["choices"][0]["text"].strip()

# ================= INTERACTIVE LOOP =================
if __name__ == "__main__":
    print(" ready. Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("AI: Bye ")
            break

        answer = ask_ai(user_input)
        print("AI:", answer)
