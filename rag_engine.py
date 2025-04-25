import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

embedding_func = SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

client = chromadb.Client()
collection = client.get_collection(name="plant_rag_local", embedding_function=embedding_func)

def get_plant_response(query: str):
    results = collection.query(query_texts=[query], n_results=1)

    if results["documents"] and results["documents"][0]:
        return results["documents"][0][0]
    else:
        return "No relevant plant info found."
