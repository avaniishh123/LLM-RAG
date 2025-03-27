# 💡 LLM-RAG-Automation-API

## 🤖 Objective
Dynamically retrieve and execute Python functions using user natural language prompts, powered by RAG (Retrieval-Augmented Generation) and an open-source LLM.

## 🚀 Features
- Automation Function Registry (Chrome, Notepad, System Info, etc)
- FAISS-based vector search for function retrieval
- Dynamic Python code generation
- Optional real-time function execution
- Session memory for prompt context
- Logging of every call

## 📦 Setup
```bash
pip install -r requirements.txt
python embed_and_index.py
uvicorn app:app --reload
