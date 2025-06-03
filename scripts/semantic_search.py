# scripts/semantic_search.py
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

def search(query: str, k=3):
    model = SentenceTransformer('paraphrase-multilingual-mpnet-base-v2')
    index = faiss.read_index('../data/faiss_index.bin')
    
    # Поиск похожих чанков
    query_embed = model.encode([query])
    distances, indices = index.search(query_embed, k)
    
    with open('../data/chunks.json') as f:
        chunks = json.load(f)
    
    return [chunks[i] for i in indices[0]]