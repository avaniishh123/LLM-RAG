from fastapi import FastAPI
from pydantic import BaseModel
from retrieve_function import retrieve_function
from code_generator import generate_code
from memory import add_to_memory, get_memory
from function_registry import *
from logger import log_event
import importlib
import os

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str
    session_id: str = "default"

@app.post("/execute")
def execute_function(req: PromptRequest):
    memory = get_memory(req.session_id)
    context_prompt = f"{memory} {req.prompt}"
    fn_name = retrieve_function(context_prompt)
    code = generate_code(fn_name)
    add_to_memory(req.session_id, req.prompt)
    return {"function": fn_name, "code": code}

@app.post("/execute_and_run")
def execute_and_run(req: PromptRequest):
    memory = get_memory(req.session_id)
    context_prompt = f"{memory} {req.prompt}"
    fn_name = retrieve_function(context_prompt)
    add_to_memory(req.session_id, req.prompt)
    code = generate_code(fn_name)

    try:
        module = importlib.import_module("function_registry")
        func = getattr(module, fn_name)
        # Pass prompt only for shell-like functions
        result = func(req.prompt) if "prompt" in fn_name else func()
    except Exception as e:
        result = str(e)

    log_event(req.prompt, fn_name, str(result), req.session_id)

    return {"function": fn_name, "code": code, "result": result}

class AddFunctionRequest(BaseModel):
    name: str
    code: str  # Code as raw string: print("Hello")

import subprocess

@app.post("/add_function")
def add_function(req: AddFunctionRequest):
    try:
        with open("function_registry.py", "a") as f:
            f.write(f"\n\ndef {req.name}():\n")
            for line in req.code.split("\\n"):
                f.write(f"    {line}\n")

        # Auto-reload FAISS index after function added
        subprocess.run(["python", "embed_and_index.py"], check=True)

        return {"message": f"Function '{req.name}' added and indexed successfully."}
    except Exception as e:
        return {"error": str(e)}
