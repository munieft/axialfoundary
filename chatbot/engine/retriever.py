from __future__ import annotations

from typing import List

from django.conf import settings

# Lazily-initialised singletons so the embedding model and Chroma client are loaded only
# once per worker process — and only when the chatbot is actually used.
_model = None
_collection = None


def _init() -> None:
    global _model, _collection
    if _model is not None and _collection is not None:
        return

    import chromadb
    from sentence_transformers import SentenceTransformer

    model_name = getattr(settings, 'CHATBOT_EMBED_MODEL', 'all-MiniLM-L6-v2')
    _model = SentenceTransformer(model_name)
    client = chromadb.PersistentClient(path=str(settings.CHROMA_DB_PATH))
    _collection = client.get_or_create_collection('knowledge')


def retrieve(query: str, top_k: int = 4) -> List[str]:
    """Return the top_k most relevant chunks for the given query (empty list if none)."""
    _init()
    if _collection is None or _model is None:
        return []
    embedding = _model.encode([query]).tolist()
    results = _collection.query(query_embeddings=embedding, n_results=top_k)
    documents = results.get('documents') or [[]]
    return documents[0] if documents else []
