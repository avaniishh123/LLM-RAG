# LLM-RAG-Based Automation System

This project implements an **LLM + Retrieval-Augmented Generation (RAG)**–based automation platform that converts **natural-language prompts into real system actions** through a secure REST API.

Instead of responding with text only, the system **retrieves the most relevant predefined automation function**, **generates executable Python code**, and **executes it in a controlled environment**, returning both the code and the result transparently.

---

## ✨ Key Features

- **RAG-Driven Function Retrieval**
  - Uses **Sentence Transformers + FAISS** to semantically match user prompts to automation functions.
- **Dynamic Code Generation**
  - Automatically generates clean, executable Python code for the selected function.
- **Secure Execution Engine**
  - Executes generated code with validation, exception handling, and logging.
- **REST API (FastAPI)**
  - Interact programmatically with the automation system.
- **Extensible Function Registry**
  - Easily add new automation capabilities via API.
- **Transparent Outputs**
  - Returns generated code **and** execution results for user trust.

---

## 🧠 How It Works (High-Level)

1. User submits a natural-language prompt
2. Prompt is embedded and matched against function embeddings (RAG)
3. Most relevant function is selected
4. Python code is dynamically generated
5. Code is executed securely
6. Result + code are returned to the user

---

Got it 👍 — here’s a **clean, concise, README-perfect architecture explanation**.
It’s **brief**, **clear**, and still **technically impressive**.

You can paste this **directly under an “Architecture” section** in your GitHub README.

---

## 🏗️ System Architecture (Brief)

The system follows a **Retrieval-Augmented Generation (RAG)** architecture to convert **natural-language user queries** into **executable automation code** in a safe and controlled manner.

### 🔹 Workflow Overview

1. **Knowledge Preparation**
   Automation scripts, templates, and documents are preprocessed, chunked, embedded, and stored in a **Vector Database** for semantic search.

2. **Query & Retrieval**
   The user query is embedded and matched against the vector database to retrieve the **most relevant automation context**.

3. **Prompt Augmentation**
   Retrieved context is combined with the user query to form a **context-aware prompt**.

4. **LLM Code Generation**
   The LLM generates **structured Python automation code** instead of plain text responses.

5. **Execution Engine**
   The generated code is executed via a **Python-based execution engine** with validation, logging, and monitoring.

6. **Response Delivery**
   The system returns the **execution result and generated code** to the user through a REST API.

---

### 🔑 Key Architectural Benefits

* Prevents LLM hallucination using **retrieval-based grounding**
* Enables **extensible automation** without retraining models
* Ensures **safe and transparent code execution**
* Scales easily by adding new functions to the RAG knowledge base

<img width="481" height="297" alt="image" src="https://github.com/user-attachments/assets/ce4dfae2-e1de-48fd-8697-230d1a215ade" /> <img width="483" height="315" alt="image" src="https://github.com/user-attachments/assets/940608bc-3d57-4a41-9bda-f64bbbef5ad0" />




## 🛠️ Tech Stack

- **Backend**: Python, FastAPI, Uvicorn  
- **RAG & Embeddings**: Sentence Transformers, FAISS  
- **LLM**: Gemini / OpenAI (pluggable)  
- **Database**: PostgreSQL(Cloud)
- **Execution**: Python subprocess (sandboxed)

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7+
- Git

### Run Locally

```bash
git clone https://github.com/avaniishh123/LLM-RAG.git
cd LLM-RAG
python -m venv venv
