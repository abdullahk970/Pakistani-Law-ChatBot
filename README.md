# ⚖️ Pakistan Law Chatbot (RAG System)

> An AI-powered legal assistant built using **LangChain, HuggingFace Embeddings, ChromaDB, and Ollama LLaMA 2**, designed to answer questions from uploaded Pakistani law PDFs using Retrieval-Augmented Generation (RAG).

![Python](https://img.shields.io/badge/Python-3.x-blue)
![LangChain](https://img.shields.io/badge/LangChain-RAG-orange)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20DB-purple)
![HuggingFace](https://img.shields.io/badge/Embeddings-MiniLM-green)
![Ollama](https://img.shields.io/badge/Ollama-LLaMA2-black)
![Gradio](https://img.shields.io/badge/Gradio-UI-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# 🚀 Overview

Pakistan Law Chatbot is a **Retrieval-Augmented Generation (RAG)** system that allows users to upload legal PDF documents and ask questions in natural language.

The system extracts text from uploaded documents, converts them into embeddings, stores them in a local vector database, and uses a lightweight LLM to generate context-aware legal answers.

This makes it a **local, offline, and privacy-friendly legal assistant**.

---

# ✨ Features

### 📄 Document Handling

* Upload multiple Pakistani law PDFs
* Automatic text extraction
* Intelligent chunking (configurable size & overlap)

### 🧠 AI-Powered Search

* Semantic search using embeddings
* Context-aware retrieval
* Accurate legal information extraction

### 📦 Vector Database

* Persistent storage using ChromaDB
* Fast similarity search
* Local storage (no cloud dependency)

### 🤖 LLM Integration

* LLaMA 2 (via Ollama)
* Retrieval-Augmented Generation (RAG)
* Context-based answers only from uploaded PDFs

### 🖥️ User Interface

* Simple Gradio-based UI
* Easy file upload system
* Chat-style Q&A interface

---

# 🏗️ Tech Stack

* Python 3
* LangChain
* HuggingFace Transformers
* sentence-transformers/all-MiniLM-L6-v2
* ChromaDB (Persistent Vector Store)
* Ollama (LLaMA 2 7B Chat Model)
* Gradio

---

# ⚙️ How It Works (RAG Pipeline)

```text id="law-rag-flow"
User Uploads PDFs
        │
        ▼
PDF Text Extraction
        │
        ▼
Text Chunking (LangChain Splitter)
        │
        ▼
HuggingFace Embeddings (MiniLM)
        │
        ▼
ChromaDB Vector Storage
        │
        ▼
User Question
        │
        ▼
Semantic Retrieval (Top-K Chunks)
        │
        ▼
LLaMA 2 (Ollama) Generates Answer
        │
        ▼
Final Legal Response (Gradio UI)
```

---

# 📂 Project Structure

```text id="law-structure"
pakistan-law-chatbot/
│
├── app/
│   ├── ingest.py
│   ├── retriever.py
│   ├── chains.py
│   ├── utils.py
│
├── data/
│   ├── pdfs/
│   └── chroma_db/
│
├── models/
│
├── ui/
│   └── gradio_app.py
│
├── requirements.txt
├── .env.example
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash id="law-clone"
git clone https://github.com/yourusername/pakistan-law-chatbot.git

cd pakistan-law-chatbot
```

---

## Create Virtual Environment

```bash id="law-venv"
python -m venv venv
```

Activate:

**Windows**

```bash id="law-win"
venv\Scripts\activate
```

**Linux / Mac**

```bash id="law-linux"
source venv/bin/activate
```

---

## Install Dependencies

```bash id="law-install"
pip install -r requirements.txt
```

---

## Install & Run Ollama

```bash id="law-ollama"
ollama serve
```

Pull model:

```bash id="law-model"
ollama pull llama2
```

---

# 🚀 Run Application

```bash id="law-run"
python ui/gradio_app.py
```

Gradio will open a local link like:

```text id="law-url"
http://127.0.0.1:7860
```

---

# 📊 Features in Detail

### 📄 Multi-PDF Upload

* Upload multiple legal documents at once
* Automatically processed and indexed

### 🧠 Smart Chunking

* Splits legal text into meaningful sections
* Configurable chunk size for accuracy

### 🔍 Semantic Search

* Finds most relevant legal sections
* Uses MiniLM embeddings for speed

### 🤖 AI Answering

* Uses LLaMA 2 (Ollama)
* Answers strictly based on retrieved context

### 🖥️ Gradio Interface

* Simple UI for non-technical users
* Chat-like experience

---

# 📁 Data Source

Legal PDFs can be loaded from:

```text id="law-pdf"
Uploaded via Gradio UI
```

Example dataset link:

👉 https://drive.google.com/file/d/1tQTdQ3e2KqhznRyLRhtZ0VsdRKqwVBbM/view?usp=drive_link

---

# ⚡ Performance Notes

* Lightweight embedding model (MiniLM)
* Fully local vector database (ChromaDB)
* No cloud API dependency
* Optimized for CPU-based systems
* Fast retrieval with top-K search

---

# 🔮 Future Improvements

* ⚖️ Urdu language support for legal queries
* 📜 Citation-based answers (exact law sections)
* 🔐 Authentication system
* ☁️ Cloud deployment (AWS / HuggingFace Spaces)
* 📊 Admin dashboard for document management
* 🤖 Multi-model support (Mistral / GPT / Claude)

---

# 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push branch
5. Open Pull Request

---


# 👨‍💻 Author

**Muhammad Abdullah Khan**


## ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub. It helps improve visibility and supports future development.
