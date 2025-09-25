Pakistan Law Chatbot – Description:

1.This is a Pakistan Law Chatbot built in Python using LangChain, HuggingFace Embeddings, ChromaDB and Gradio.

2.It allows users to upload multiple PDF documents (e.g., Pakistani laws or acts).

3.The app automatically extracts, splits and indexes the content into a vector database using sentence-transformers/all-MiniLM-L6-v2 for fast embeddings.

4.It uses a lightweight LLaMA 2 model (through Ollama) for retrieval-augmented generation (RAG) so that it can answer questions based on the uploaded PDFs.

5.The interface is built with Gradio, making it very simple to upload files.

Features:

1.Upload multiple PDF law documents at once.

2.Automatic text splitting into chunks (configurable chunk_size & chunk_overlap).

3.Fast embeddings using HuggingFace.

4.Persistent local vector store with ChromaDB.

5.Simple Q&A interface powered by LLaMA 2 via Ollama.

6.Gradio GUI for non-technical users.

Tech Stack:

1.Python 3

2.LangChain + HuggingFace Embeddings

3.ChromaDB (persistent vector store)

(Pdfs link)
{https://drive.google.com/file/d/1tQTdQ3e2KqhznRyLRhtZ0VsdRKqwVBbM/view?usp=drive_link}

4.Ollama LLaMA2 7B chat model

5.Gradio UI
