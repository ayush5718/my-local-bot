import os

DATA_DIR = r"E:\React projects\local-ai-assistant\data"
CHUNKS_DIR = r"E:\React projects\local-ai-assistant\chunks"

os.makedirs(CHUNKS_DIR, exist_ok=True)

chunk_size = 100  # characters
chunk_count = 0

for filename in os.listdir(DATA_DIR):
    if not filename.endswith(".txt"):
        continue

    file_path = os.path.join(DATA_DIR, filename)

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size].strip()
        if chunk:
            chunk_count += 1
            chunk_filename = f"chunk_{chunk_count}.txt"
            chunk_path = os.path.join(CHUNKS_DIR, chunk_filename)

            with open(chunk_path, "w", encoding="utf-8") as cf:
                cf.write(chunk)

            print(f"Created {chunk_filename}")

print("\nDone. Total chunks created:", chunk_count)
