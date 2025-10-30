from collections import defaultdict

session_memory = defaultdict(list)

def add_to_memory(session_id: str, prompt: str):
    session_memory[session_id].append(prompt)

def get_memory(session_id: str) -> str:
    return " ".join(session_memory[session_id])
