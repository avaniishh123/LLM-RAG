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

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/f8d48f28-ca14-47ff-93c0-09ded01b3862" />

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

📸 Visual Results & UI Demonstration

This section demonstrates how the LLM-RAG Automation System transforms natural-language queries into executable code and real system actions through an interactive API interface.

🔹 1. LLM-RAG API Interface

<img width="1234" height="950" alt="image" src="https://github.com/user-attachments/assets/14aa2c36-5c34-448b-b649-3f74ab418835" />


The main interface allows users to:

Enter natural-language queries

Use quick-action prompts (e.g., CPU usage, memory usage, open apps)

Execute queries with a single click

The UI clearly separates:

Generated Code (left panel)

Execution Result (right panel)

This ensures transparency and trust in LLM-driven automation.

🔹 2. System Monitoring Automation (CPU Usage)

<img width="1358" height="644" alt="image" src="https://github.com/user-attachments/assets/ee7581ae-e52b-46e5-80f9-1c2ca7aa5923" />


When the user submits a query like “get cpu usage”:

The RAG pipeline retrieves the correct system function

The LLM generates valid Python code using psutil

The execution engine runs the code safely

The real-time CPU usage is displayed in the result panel

This showcases live system interaction, not simulated responses.

🔹 3. Memory Usage Automation

<img width="1358" height="644" alt="image" src="https://github.com/user-attachments/assets/b45af185-a670-4b1d-8cdf-47dd2e06945d" />


For queries such as “get memory usage”:

The system generates structured Python code

Reports total, used, and available memory

Displays results in a human-readable format

This demonstrates accurate resource monitoring via natural language.

🔹 4. Real-World Automation (Job Search Example)

For higher-level queries like “give me jobs in Hyderabad in real life”:

The system retrieves relevant automation templates

Generates web-scraping / data-processing code

Executes the workflow

Displays extracted job listings

Exports results to CSV and JSON files

This highlights the system’s ability to handle multi-step, real-world automation tasks.

<img width="1358" height="644" alt="image" src="https://github.com/user-attachments/assets/5f480be7-0d89-4600-9292-2d8ee9f4b1bc" />


✅ Key Takeaways from Visual Results

Natural language → executable automation

Transparent code generation (no black box)

Safe execution with real outputs

Supports both system-level and application-level tasks

Scales from simple commands to complex workflows

These visual results validate the system as a practical LLM-RAG automation platform, not just a chatbot.

📸 API Visual Results & Demonstration

Here’s a **concise, GitHub-README–ready “API Visual Results Explanation”** that explains **all the screenshots together**, clearly and professionally, without going too deep.

You can paste this directly under a **“API Demonstration / Visual Results”** section.

---

## 📸 API Visual Results & Demonstration

These demonstrate how the **LLM-RAG Automation System** works end-to-end through its REST API using the **FastAPI Swagger UI**.

---

### 🔹 1. Function Retrieval & Code Generation (`/execute`)

<img width="923" height="396" alt="image" src="https://github.com/user-attachments/assets/2ff66ad1-2a38-4b14-8723-9343199edb94" />

The first response shows the `/execute` endpoint in action:

* The system retrieves the most relevant function (`random_joke`) using RAG.
* The LLM dynamically generates **executable Python code**.
* The response returns both:

  * Selected function name
  * Generated code (fully transparent)

This validates that the system performs **retrieval + generation**, not hard-coded execution.

---

### 🔹 2. Dynamic Function Registration (`/add_function`)

<img width="1788" height="649" alt="image" src="https://github.com/user-attachments/assets/a040931f-81c5-454c-a30a-a52c34d52418" />


The `/add_function` endpoint demonstrates **runtime extensibility**:

* A new function (`say_os`) is added via API.
* The function is automatically **indexed into the vector database**.
* A success message confirms availability for future queries.

This proves the system can **grow its automation capabilities without redeployment or retraining**.

---

### 🔹 3. Retrieval + Execution Pipeline (`/execute_and_run`)

<img width="911" height="727" alt="image" src="https://github.com/user-attachments/assets/91740cc2-744c-4ef0-8033-ce60b6cfc0db" />


The `/execute_and_run` endpoint shows the complete pipeline:

* Function retrieval (`say_time`)
* Code generation
* Safe execution
* Real output returned (`Current time is 14:53:15`)

The response includes:

* Generated code
* Execution result
* HTTP 200 success confirmation

This confirms **real system interaction**, not simulated outputs.

---

## ✅ Key Takeaways from API Results

* Natural language → function retrieval → code generation → execution
* Fully transparent LLM behavior (code is visible)
* Runtime-extensible automation via API
* Secure, production-ready FastAPI interface

These results validate the system as a **practical LLM-RAG automation platform**, capable of powering real-world applications beyond chatbots.

## 🛠️ Tech Stack

- **Backend**: Python, FastAPI, Uvicorn  
- **RAG & Embeddings**: Sentence Transformers, FAISS  
- **LLM**: Gemini / OpenAI (pluggable)  
- **Database**: PostgreSQL(Cloud)
- **Execution**: Python subprocess (sandboxed)

## 🎥 Demo Video

▶️ https://drive.google.com/file/d/1rppTtUJz0tXGZt95PRyjaP7JH1Hb9mhL/view


## 👨‍💻 Contributors

* **Avanish Cowkur** – System architecture, RAG pipeline, execution engine
* **Rishi Kuimil Nambiar** – Backend integration, API logic
* **Rohan Kuimil Nambiar** – Testing, validation, documentation

---

## 📌 Use Cases

* System monitoring via natural language
* Developer productivity automation
* Research and data extraction workflows
* Safe LLM-driven task execution

