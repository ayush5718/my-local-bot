# Local AI Assistant (Offline RAG)

A beginner-friendly local AI assistant that runs completely offline and answers questions using your own files.

This project demonstrates how a real **Retrieval-Augmented Generation (RAG)** system works using a local language model.

👉 **[Read the Full Documentation & Explanations](docs/project_docs.md)** to learn what RAG is and how this works.

---

## Features

- **100% Offline**: No internet required.
- **Private**: Your data never leaves your computer.
- **Custom Knowledge**: Answers questions from your own `.txt` files.
- **CPU Friendly**: Runs on standard laptops using the Phi-2 model.

## Tech Stack

- **Python 3.11**
- **llama-cpp-python**: Runs the AI model locally.
- **sentence-transformers**: Converts text to numbers (embeddings).
- **SQLite**: Stores the data for quick searching.
- **Phi-2**: The AI model (GGUF format).

---

## Project Structure

```text
local-ai-assistant/
│
├── data/             # Put your text files here
├── chunks/           # Generated text chunks
├── embeddings/       # embeddings.db (vector memory)
├── model/            # [Download phi-2.Q4_K_M.gguf here]
├── docs/             # Documentation
└── app/
    ├── 01_chunk_files.py       # Step 1: Chop text
    ├── 02_create_embeddings.py # Step 2: Save to DB
    └── assistant.py            # Step 3: Chat
```

## 📥 Download the Model (Required)
Since the AI model file is large, it is not included in this repository. 

1. **Download**: [phi-2.Q4_K_M.gguf](https://huggingface.co/TheBloke/Phi-2-GGUF/resolve/main/phi-2.Q4_K_M.gguf) (approx. 1.7GB)
2. **Place it**: inside the `model/` folder.
   - Filesystem path should be: `local-ai-assistant/model/phi-2.Q4_K_M.gguf`


---

## How to Run

Follow these steps in order:

### 1. Prepare Data
Add your text files (e.g., `notes.txt`) into the `data/` folder.

### 2. Process Files
Run the chunking script to break texts into small pieces:
```bash
py -3.11 app/01_chunk_files.py
```

### 3. Build Memory
Convert chunks into searchable numbers (embeddings):
```bash
py -3.11 app/02_create_embeddings.py
```

### 4. Chat
Start the AI assistant:
```bash
py -3.11 app/assistant.py
```

---

## Future Roadmap

See [docs/project_docs.md](docs/project_docs.md) for ideas on how to extend this project (e.g., adding a Web UI, PDF support).
