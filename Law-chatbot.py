import os
import traceback
import gradio as gr
from concurrent.futures import ThreadPoolExecutor
from typing import List, Any

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM
from langchain.chains import RetrievalQA

# ---------------- CONFIG ----------------
DB_DIR = "chroma_db"
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"  
LLM_MODEL = "llama2:7b-chat"   
CHUNK_SIZE = 2500
CHUNK_OVERLAP = 100
MAX_WORKERS = 8
RETRIEVER_K = 3
# ----------------------------------------

embeddings = HuggingFaceEmbeddings(
    model_name=EMBED_MODEL,
    model_kwargs={"device": "cpu"}  
)
llm = OllamaLLM(model=LLM_MODEL)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)

_vectordb = None
_qa_chain = None

def _normalize_file_paths(files: List[Any]) -> List[str]:
    paths = []
    if not files:
        return []
    for f in files:
        if isinstance(f, str):
            paths.append(f)
            continue
        if isinstance(f, dict):
            for k in ("name", "file", "tmp_path", "tempfile", "path"):
                if k in f and isinstance(f[k], str):
                    paths.append(f[k])
                    break
            continue
        if hasattr(f, "name"):
            paths.append(getattr(f, "name"))
            continue
        try:
            s = str(f)
            paths.append(s)
        except Exception:
            pass
    return [p for p in paths if p]

def _load_and_split(pdf_path: str):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    return text_splitter.split_documents(docs)

def process_pdfs(files):
    global _vectordb, _qa_chain
    try:
        file_paths = _normalize_file_paths(files)
        if not file_paths:
            return " No files found. Please upload PDFs."

        chunks_all = []
        workers = min(MAX_WORKERS, max(1, len(file_paths)))
        with ThreadPoolExecutor(max_workers=workers) as ex:
            results = list(ex.map(_load_and_split, file_paths))
        for sub in results:
            chunks_all.extend(sub)

        if not chunks_all:
            return "No chunks extracted from PDFs."

        _vectordb = Chroma.from_documents(chunks_all, embedding=embeddings, persist_directory=DB_DIR)
        try:
            if hasattr(_vectordb, "persist"):
                _vectordb.persist()
        except Exception:
            pass

        retriever = _vectordb.as_retriever(search_kwargs={"k": RETRIEVER_K})
        _qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, chain_type="stuff")

        return f"Indexed {len(chunks_all)} chunks from {len(file_paths)} file(s)."
    except Exception as e:
        traceback.print_exc()
        return f"Error during processing: {str(e)}"

def answer_query(query: str):
    global _vectordb, _qa_chain
    try:
        if _qa_chain is None:
            if os.path.isdir(DB_DIR):
                _vectordb = Chroma(persist_directory=DB_DIR, embedding_function=embeddings)
                retriever = _vectordb.as_retriever(search_kwargs={"k": RETRIEVER_K})
                _qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, chain_type="stuff")
            else:
                return "No vector DB found. Please upload & process PDFs first."
        out = _qa_chain.invoke({"query": query})
        if isinstance(out, dict):
            return out.get("result") or out.get("answer") or str(out)
        return str(out)
    except Exception as e:
        traceback.print_exc()
        return f"Error while answering: {str(e)}"

with gr.Blocks() as demo:
    gr.Markdown("Pakistan Law Chatbot — Fast mode")

    try:
        pdf_upload = gr.Files(file_types=[".pdf"], type="filepath", label="Upload PDFs (select many)")
    except Exception:
        pdf_upload = gr.File(file_types=[".pdf"], file_count="multiple", type="filepath", label="Upload PDFs (select many)")

    process_btn = gr.Button("Process & Index PDFs")
    status = gr.Textbox(label="Status", interactive=False)

    q = gr.Textbox(label="Ask a question", placeholder="e.g. inheritance law me daughter ka hissa?")
    a = gr.Textbox(label="Answer")

    process_btn.click(fn=process_pdfs, inputs=pdf_upload, outputs=status)
    q.submit(fn=answer_query, inputs=q, outputs=a)

demo.launch()










