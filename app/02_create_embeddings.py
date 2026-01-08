import os
import sqlite3
from sentence_transformers import SentenceTransformer

CHUNKS_DIR = r"E:\React projects\local-ai-assistant\chunks"
DB_PATH = r"E:\React projects\local-ai-assistant\embeddings\embeddings.db"

os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

# Load embedding model (small & CPU-friendly)
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS embeddings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chunk_text TEXT,
    vector BLOB
)
""")

# Process chunks
for filename in os.listdir(CHUNKS_DIR):
    if not filename.endswith(".txt"):
        continue

    path = os.path.join(CHUNKS_DIR, filename)

    with open(path, "r", encoding="utf-8") as f:
        text = f.read().strip()

    if not text:
        continue

    embedding = model.encode(text)

    cursor.execute(
        "INSERT INTO embeddings (chunk_text, vector) VALUES (?, ?)",
        (text, embedding.tobytes())
    )

    print(f"Embedded {filename}")

conn.commit()
conn.close()

print("\nAll chunks converted to embeddings and stored.")
