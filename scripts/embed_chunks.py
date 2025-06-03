# scripts/embed_chunks.py
from sentence_transformers import SentenceTransformer
import json
import faiss
import numpy as np

def embed_data():
    model = SentenceTransformer('paraphrase-multilingual-mpnet-base-v2')
    chunks = []
    
    # Загрузка данных
    with open('../data/catalog.json') as f:
        catalog = json.load(f)
        chunks.extend([item['text'] for item in catalog])
    
    with open('../data/sales_book.json') as f:
        sales_book = json.load(f)
        chunks.extend([item['text'] for item in sales_book])
    
    # Генерация эмбеддингов
    embeddings = model.encode(chunks, convert_to_tensor=True)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings.cpu().numpy())
    
    # Сохранение индекса
    faiss.write_index(index, '../data/faiss_index.bin')
    with open('../data/chunks.json', 'w') as f:
        json.dump(chunks, f)