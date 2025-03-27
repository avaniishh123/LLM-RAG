from sentence_transformers import SentenceTransformer
import faiss
import pickle

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("functions.index")

with open("metadata.pkl", "rb") as f:
    function_names = pickle.load(f)

def retrieve_function(user_prompt):
    embedding = model.encode([user_prompt])
    _, I = index.search(embedding, k=1)
    return function_names[I[0][0]]
