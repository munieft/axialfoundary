from __future__ import annotations

import re
from typing import List


def load_and_chunk(filepath: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    """Load a markdown / plain-text file and split it into overlapping word-window chunks.

    The text is lightly cleaned (markdown headings and emphasis stripped) before chunking
    so embeddings are computed over content rather than syntax.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Strip basic markdown syntax for cleaner embeddings.
    text = re.sub(r'#+\s*', '', text)         # headings
    text = re.sub(r'\*+', '', text)            # bold / italic markers
    text = re.sub(r'`+', '', text)             # inline code markers
    text = re.sub(r'^\s*[-*]\s+', '', text, flags=re.MULTILINE)  # bullet markers
    text = re.sub(r'\n{3,}', '\n\n', text)     # collapse excessive blank lines

    words = text.split()
    chunks: List[str] = []
    i = 0
    step = max(1, chunk_size - overlap)
    while i < len(words):
        chunk = ' '.join(words[i:i + chunk_size]).strip()
        if chunk:
            chunks.append(chunk)
        i += step

    # Drop very small fragments that would produce noisy embeddings.
    return [c for c in chunks if len(c) > 50]
