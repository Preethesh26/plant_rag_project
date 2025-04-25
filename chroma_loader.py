import pandas as pd
import chromadb
from sentence_transformers import SentenceTransformer
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

def load_data_to_chroma():
    df = pd.read_excel("plant.xlsx")

    embedding_func = SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )

    client = chromadb.Client()
    collection = client.get_or_create_collection(
        name="plant_rag_local",
        embedding_function=embedding_func
    )

    for i, row in df.iterrows():
        doc = f"Name: {row['Name']}\nUses: {row['Uses']}\nMedicinal: {row['Medicinal']}"
        collection.add(documents=[doc], ids=[str(i)])
    
    print("✅ Plant data loaded into ChromaDB!")

if __name__ == "__main__":
    load_data_to_chroma()
