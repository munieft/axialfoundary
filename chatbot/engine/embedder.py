from __future__ import annotations

from django.conf import settings


def build_vector_store(filepath: str | None = None) -> int:
    """Build (or rebuild) the persistent ChromaDB vector store from the knowledge base.

    Run once after setup, and again any time data/knowledge_base.md changes:
        python manage.py build_vectorstore
    """
    # Imports are local so importing this module does not pull heavy deps at app start.
    import chromadb
    from sentence_transformers import SentenceTransformer

    from .chunker import load_and_chunk

    path = filepath or settings.KNOWLEDGE_BASE_PATH
    chunks = load_and_chunk(path)
    if not chunks:
        raise RuntimeError(f'No usable chunks produced from {path}.')

    model_name = getattr(settings, 'CHATBOT_EMBED_MODEL', 'all-MiniLM-L6-v2')
    model = SentenceTransformer(model_name)
    client = chromadb.PersistentClient(path=str(settings.CHROMA_DB_PATH))
    col = client.get_or_create_collection('knowledge')

    # Clear any prior contents so rebuilds replace rather than append.
    existing_ids = col.get().get('ids') or []
    if existing_ids:
        col.delete(ids=existing_ids)

    embeddings = model.encode(chunks, show_progress_bar=True).tolist()
    col.add(
        documents=chunks,
        embeddings=embeddings,
        ids=[f'chunk_{i}' for i in range(len(chunks))],
    )
    print(f'Vector store built: {len(chunks)} chunks stored at {settings.CHROMA_DB_PATH}.')
    return len(chunks)
