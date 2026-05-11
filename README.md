# Local AI PDF Chatbot

A local AI-powered PDF chatbot built using Flask, Ollama, ChromaDB, and Sentence Transformers.

This application allows users to upload PDF documents and ask questions based on the document content using Retrieval-Augmented Generation (RAG).

---

# Features

- PDF Upload
- PDF Text Extraction
- Text Chunking
- Embedding Generation
- Semantic Search
- ChromaDB Vector Database
- Local AI using Ollama
- Question Answering from PDFs
- RAG Architecture

---

# Technologies Used

- Python
- Flask
- Ollama
- Mistral AI
- ChromaDB
- Sentence Transformers
- PyPDF
- LangChain Text Splitters

---

# How It Works

1. User uploads PDF
2. PDF text is extracted
3. Text is split into chunks
4. Embeddings are generated
5. Chunks are stored in ChromaDB
6. User asks questions
7. Relevant chunks are retrieved
8. Ollama generates final answer using retrieved context

---

# RAG Architecture

```text
PDF
 ↓
Text Extraction
 ↓
Chunking
 ↓
Embeddings
 ↓
Vector Database
 ↓
Semantic Retrieval
 ↓
LLM (Mistral via Ollama)
 ↓
Final Answer
```

---

# Installation

## Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

## Open Project

```bash
cd pdf_chatbot
```

## Create Virtual Environment

```bash
python3 -m venv venv
```

## Activate Virtual Environment

### Mac/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Install Ollama

Download Ollama:

https://ollama.com/download

Pull Mistral Model:

```bash
ollama pull mistral
```

Run Ollama:

```bash
ollama run mistral
```

---

# Run Application

```bash
python3 app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

# Future Improvements

- Better UI
- Multiple PDF Support
- Chat History
- User Authentication
- Streaming Responses
- Citation Support
- PDF Page References

---

# Technologies Demonstrated

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Embeddings
- Vector Databases
- Local LLM Inference
- NLP Concepts
- AI Application Development

---

# Author

Ashish Sajeev
