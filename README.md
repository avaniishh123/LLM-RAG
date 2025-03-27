# LLM-RAG-based Automation System

This project implements a **Retrieval-Augmented Generation (RAG)** model for automating various tasks through a REST API. The system retrieves functions based on user prompts and dynamically generates Python code to execute them. The functions include basic system operations, such as opening apps, checking system information, running shell commands, and more.

## Features
- **Function Registry**: A collection of predefined automation functions (e.g., open Chrome, get system info, etc.).
- **RAG Model**: Uses **Sentence Transformers** and **FAISS** for efficient retrieval of the most relevant function based on the user's input.
- **Dynamic Code Generation**: Automatically generates Python code to execute the selected function.
- **API Service**: Exposes a REST API to interact with the system and execute functions remotely.

---

## Installation

### Prerequisites

- Python 3.7 or higher
- Git

### Steps to Run the Project Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/avaniishh123/LLM-RAG.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd LLM-RAG
   ```

3. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment**:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On Mac/Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

6. **Run the FAISS index generation script**:
   ```bash
   python embed_and_index.py
   ```

7. **Start the FastAPI server**:
   ```bash
   uvicorn app:app --reload
   ```

The API will be available at `http://127.0.0.1:8000`.

---

## API Endpoints

The system exposes three main endpoints:

### 1. **`POST /execute`**
Retrieves the most relevant function based on the user’s prompt and returns the Python code to invoke the function.

#### Request Example
```json
{
  "prompt": "Tell me a joke",
  "session_id": "fun123"
}
```

#### Response Example
```json
{
  "function": "random_joke",
  "code": "from function_registry import random_joke\n\ndef main():\n    try:\n        result = random_joke()\n        if result:\n            print(result)\n        else:\n            print(\"random_joke executed successfully.\")\n    except Exception as e:\n        print(\"Error:\", e)\n\nif __name__ == \"__main__\":\n    main()"
}
```

### 2. **`POST /execute_and_run`**
Retrieves and executes the function based on the prompt, then returns the result.

#### Request Example
```json
{
  "prompt": "Tell me the current time",
  "session_id": "time123"
}
```

#### Response Example
```json
{
  "function": "say_time",
  "code": "from function_registry import say_time\n\ndef main():\n    try:\n        result = say_time()\n        if result:\n            print(result)\n        else:\n            print(\"say_time executed successfully.\")\n    except Exception as e:\n        print(\"Error:\", e)\n\nif __name__ == \"__main__\":\n    main()",
  "result": "Current time is 14:30:45"
}
```

### 3. **`POST /add_function`**
Adds a new function to the function registry. The function will then be available for future execution.

#### Request Example
```json
{
  "name": "say_hello",
  "code": "return 'Hello from your automation assistant!'"
}
```

#### Response Example
```json
{
  "message": "Function 'say_hello' added successfully."
}
```

---

## Function Registry

The **function_registry.py** file contains predefined automation functions that can be executed through the API. Some of the key functions include:
- **System Info**: `get_cpu_usage`, `get_memory_usage`
- **App Operations**: `open_chrome`, `open_calculator`, `open_notepad`, etc.
- **Custom Functions**: You can add custom functions using the `/add_function` endpoint.

---

## Logging

The system logs each function execution for monitoring purposes. Logs are saved in the `function_logs.txt` file.

---

## How to Contribute

1. Fork the repository.
2. Clone your forked repository to your local machine.
3. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature-name
   ```
4. Make your changes and commit them.
5. Push to your forked repository:
   ```bash
   git push origin feature-name
   ```
6. Open a pull request from your branch to the main repository.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Screenshots

Here are some example screenshots of the Swagger UI and responses:

![Swagger UI](sample_requests/screenshot_1.png)

---

Let me know if you need any further details, adjustments, or additional sections! 😄
