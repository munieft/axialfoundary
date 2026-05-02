from __future__ import annotations

import json
from pathlib import Path

from django.conf import settings


def _embed_texts(texts: list[str], task_type: str) -> list[list[float]]:
    """Call Gemini's embedding endpoint for a batch of texts."""
    import google.generativeai as genai

    api_key = getattr(settings, 'GEMINI_API_KEY', '') or ''
    if not api_key:
        raise RuntimeError('GEMINI_API_KEY is not configured.')
    genai.configure(api_key=api_key)

    model = getattr(settings, 'CHATBOT_EMBED_MODEL', 'models/text-embedding-004')
    if not model.startswith('models/'):
        model = 'models/' + model

    out: list[list[float]] = []
    # The API accepts a list, but we loop one-by-one for resilience: a single bad
    # chunk will not poison the whole batch.
    for text in texts:
        result = genai.embed_content(
            model=model,
            content=text,
            task_type=task_type,
        )
        out.append(list(result['embedding']))
    return out


def embed_query(text: str) -> list[float]:
    return _embed_texts([text], task_type='retrieval_query')[0]


def build_vector_store(filepath: str | None = None) -> int:
    """Embed every chunk of the knowledge base and write the result to a JSON file.

    Output: data/embeddings.json — a single dict { "chunks": [...], "embeddings": [...] }.
    Run after setup, and again whenever data/knowledge_base.md changes:
        python manage.py build_vectorstore
    """
    from .chunker import load_and_chunk

    path = filepath or settings.KNOWLEDGE_BASE_PATH
    chunks = load_and_chunk(path)
    if not chunks:
        raise RuntimeError(f'No usable chunks produced from {path}.')

    print(f'Embedding {len(chunks)} chunks via Gemini…')
    embeddings = _embed_texts(chunks, task_type='retrieval_document')

    out_path = Path(settings.CHROMA_DB_PATH) / 'embeddings.json'
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump({'chunks': chunks, 'embeddings': embeddings}, f)

    print(f'Vector store built: {len(chunks)} chunks stored at {out_path}.')
    return len(chunks)
