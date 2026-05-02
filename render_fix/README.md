# Render Free-Tier Patch

Replaces local sentence-transformers + ChromaDB with Gemini's embedding API +
a numpy-style cosine search over a JSON file. RAM footprint drops from ~2 GB
to ~50 MB so the chatbot fits in Render's free 512 MB tier.

## Files in this patch

| File | What it replaces | Why |
|------|------------------|-----|
| `chatbot/engine/embedder.py` | same | Uses Gemini `text-embedding-004`; writes `chroma_db/embeddings.json` |
| `chatbot/engine/retriever.py` | same | Loads JSON, pure-Python cosine similarity |
| `chatbot/views.py` | same | `switch_mode` now auto-recreates stale sessions instead of returning 404 |
| `requirements.txt` | same | Removes torch, sentence-transformers, transformers, chromadb |

## Apply the patch

From your project root:

```bash
unzip render_fix.zip -d /tmp/renderfix
cp /tmp/renderfix/chatbot/engine/embedder.py    chatbot/engine/embedder.py
cp /tmp/renderfix/chatbot/engine/retriever.py   chatbot/engine/retriever.py
cp /tmp/renderfix/chatbot/views.py              chatbot/views.py
cp /tmp/renderfix/requirements.txt              requirements.txt
```

## Update your environment

Add or change one line in `.env` (or in Render's environment-variable settings):

```
CHATBOT_EMBED_MODEL=models/text-embedding-004
```

(The previous default `all-MiniLM-L6-v2` no longer applies — that was for
sentence-transformers. If `CHATBOT_EMBED_MODEL` is unset, the code falls back
to `models/text-embedding-004` automatically.)

## Locally

```bash
pip uninstall -y torch sentence-transformers transformers chromadb \
    nvidia-cublas-cu12 nvidia-cuda-cupti-cu12 nvidia-cuda-nvrtc-cu12 \
    nvidia-cuda-runtime-cu12 nvidia-cudnn-cu12 nvidia-cufft-cu12 \
    nvidia-curand-cu12 nvidia-cusolver-cu12 nvidia-cusparse-cu12 \
    nvidia-nccl-cu12 nvidia-nvtx-cu12 triton 2>/dev/null

pip install -r requirements.txt
rm -rf chroma_db/
python manage.py build_vectorstore
python manage.py runserver
```

## On Render

After pushing the changes, Render will rebuild with the slim `requirements.txt`.
On first deploy, run the build-vectorstore step (Render shell or a one-off job):

```bash
python manage.py build_vectorstore
```

This writes `chroma_db/embeddings.json` (~30 KB for a small KB). For most Render
setups this directory persists across deploys; if yours doesn't, add a
`postdeploy` hook in `render.yaml` to run the command on every deploy.

## Verify

```bash
curl -X POST https://www.axialfoundary.com/api/chat/start/ -H "Content-Type: application/json" -d '{}'
# Should return {"session_id":"<uuid>","mode":"chat"}

curl -X POST https://www.axialfoundary.com/api/chat/message/ \
    -H "Content-Type: application/json" \
    -d '{"session_id":"<that uuid>","message":"What services do you offer?"}'
# Should return a coherent reply, no 500.
```

## Why the 404 on /api/chat/mode/ was happening

The previous build returned `404 session not found` whenever the browser sent
a `session_id` from localStorage that did not exist in the production database
(e.g. UUIDs created during local development before deployment). The new
`switch_mode` view silently creates a fresh session in that case and returns
the new UUID so the client updates its cache. The widget already persists any
`session_id` it sees in API responses, so no widget changes are required.
