from datetime import datetime

def log_event(prompt: str, function_name: str, result: str, session_id: str = "default"):
    with open("function_logs.txt", "a") as f:
        f.write(f"[{datetime.now()}] Session: {session_id} | Prompt: {prompt} | Function: {function_name} | Result: {result}\n")
