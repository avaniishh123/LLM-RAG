from sentence_transformers import SentenceTransformer
import faiss
import pickle

# Function name : Short description for embedding
function_metadata = {
    # OPEN
    "open_chrome": "Open Google Chrome browser",
    "open_calculator": "Launch calculator app",
    "open_notepad": "Open Notepad text editor",
    "open_paint": "Open Microsoft Paint",
    "open_word": "Open Microsoft Word",

    # SYSTEM INFO
    "get_cpu_usage": "Get current CPU usage",
    "get_memory_usage": "Get current memory usage",
    "say_os": "Tell which operating system the user is on",

    # SHELL & CUSTOM
    "run_shell_command_from_prompt": "Execute shell command based on user input",
    "greet": "Return a greeting message",
    "say_date": "Return today's date using datetime",
    "say_time": "Return current time in hours, minutes, and seconds",
    "say_year": "Return current year using datetime",
    "random_joke": "Return a random developer joke",

    # VOICE
    "listen_command": "Capture user input using microphone"
}

# Create embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Convert descriptions to embeddings
descriptions = list(function_metadata.values())
embeddings = model.encode(descriptions)

# Create FAISS index and add embeddings
index = faiss.IndexFlatL2(embeddings[0].shape[0])
index.add(embeddings)

# Save index and metadata
faiss.write_index(index, "functions.index")
with open("metadata.pkl", "wb") as f:
    pickle.dump(list(function_metadata.keys()), f)

print("Index and metadata saved successfully.")
