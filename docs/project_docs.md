# Project Documentation: Local AI Assistant

## What is this project?
This is a **Local RAG (Retrieval-Augmented Generation) Assistant**. It allows you to chat with an AI about your own private text files without needing an internet connection or sending data to the cloud.

The entire system runs locally on your computer using Python.

## Key Concepts Explained

To understand how this works, here are the simple definitions of the technical terms used:

### 1. RAG (Retrieval-Augmented Generation)
RAG is a technique used to give an AI "memory" of data it hasn't seen before. Instead of just asking the AI a question directly, we first search your documents for the answer, and then give both the **question** AND the **search results** to the AI.

**The Formula:**
> User Question + Relevant Book Pages = Smart Answer

### 2. LLM (Large Language Model)
The "brain" of the AI. In this project, we are using **Phi-2**, a small but powerful model from Microsoft that can run on a standard laptop CPU.

### 3. Chunking
Breaking down large text files into smaller, manageable pieces (e.g., 500 characters). This makes it easier to find specific information rather than reading an entire book to answer a simple question.

### 4. Embeddings
Converting text into numbers (lists of decimals). Computers don't understand words, they understand numbers.
- "Dog" and "Puppy" will have very similar number lists.
- "Dog" and "Car" will have very different number lists.
This allows us to find "similar" meanings mathematically.

### 5. Vector Database
A special storage system for these "Embeddings". We use **SQLite** here to store the numbers so we can quickly search through them.

---

## How It Works (Step-by-Step)

1.  **Ingestion (Pre-processing)**:
    - You place text files in the `data/` folder.
    - `01_chunk_files.py` reads them and chops them into small chunks.

2.  **Indexing**:
    - `02_create_embeddings.py` takes those chunks and converts them into "embeddings" (number lists).
    - It saves these numbers into `embeddings/embeddings.db`.

3.  **Chatting (The Loop)**:
    - You ask a question in `assistant.py`.
    - The system converts your question into numbers.
    - It searches the database for the most similar chunks (most relevant text).
    - It sends your question + the relevant chunks to the Phi-2 model.
    - The model answers using that information.

---

## Future Possibilities

Here is what we can build next to improve this project:

### 1. Web Interface (UI)
Currently, it runs in a black text terminal. We could build a website using **Streamlit** or **React** so it looks like ChatGPT.

### 2. Support More File Types
Right now it only reads `.txt` files. We can add support for:
- **PDFs** (using `pypdf`)
- **Word Docs**
- **Websites** (scraping URLs)

### 3. Chat History (Memory)
Currently, the AI forgets the previous question immediately. We can add a "memory list" so you can have a back-and-forth conversation (e.g., "Tell me more about that").

### 4. Better Models
We can swap Phi-2 for Llama-3 or Mistral for smarter reasoning, though they might require a more powerful computer.
