# Axial Foundry Chatbot — Installation Guide

This package adds a RAG-powered chatbot (Gemini + ChromaDB) to the existing
`axialfoundry` Django project. **Nothing in the existing codebase is removed**;
three files are extended (`settings.py`, `axialfoundry/urls.py`, `templates/base.html`)
and a new `chatbot/` Django app is added.

---

## 1. What is in this package

```
chatbot_delivery/
├── chatbot/                       ← NEW Django app — copy as-is to project root
│   ├── __init__.py
│   ├── apps.py
│   ├── admin.py
│   ├── models.py                  ← Session, Message, Log, ContactLead
│   ├── serializers.py
│   ├── services.py                ← orchestrator
│   ├── views.py                   ← 4 DRF endpoints
│   ├── urls.py
│   ├── retry_queue.py             ← background retry on Gemini failure
│   ├── funnel_handler.py          ← contact-funnel state machine
│   ├── engine/
│   │   ├── chunker.py
│   │   ├── embedder.py
│   │   ├── retriever.py
│   │   ├── prompt_builder.py      ← system prompt + foolproofing rules
│   │   └── gemini_client.py
│   ├── management/commands/
│   │   └── build_vectorstore.py   ← python manage.py build_vectorstore
│   ├── templates/chatbot/
│   │   └── widget.html            ← floating chat widget (dark + light theme)
│   └── migrations/__init__.py     ← empty; makemigrations will create 0001
│
├── data/
│   └── knowledge_base.md          ← cleaned RAG knowledge document
│
└── _modified_existing_files/      ← drop-in replacements for these files
    ├── axialfoundry/settings.py
    ├── axialfoundry/urls.py
    ├── templates/base.html
    ├── requirements.txt
    └── .env.chatbot.example       ← keys to append to your .env
```

---

## 2. Install (copy & paste)

From the project root (where `manage.py` lives):

```bash
# 1. Copy the new app and data directory in.
cp -r chatbot_delivery/chatbot ./
cp -r chatbot_delivery/data ./

# 2. Replace the three modified files (BACK THEM UP FIRST IF YOU LIKE).
cp chatbot_delivery/_modified_existing_files/axialfoundry/settings.py axialfoundry/settings.py
cp chatbot_delivery/_modified_existing_files/axialfoundry/urls.py     axialfoundry/urls.py
cp chatbot_delivery/_modified_existing_files/templates/base.html      templates/base.html
cp chatbot_delivery/_modified_existing_files/requirements.txt         requirements.txt

# 3. Append the new env keys to your .env (see _modified_existing_files/.env.chatbot.example).
cat chatbot_delivery/_modified_existing_files/.env.chatbot.example >> .env
# Then open .env and set GEMINI_API_KEY=<your key from https://aistudio.google.com/apikey>

# 4. Install the new Python dependencies.
pip install -r requirements.txt

# 5. Apply migrations (creates chatbot_session, chatbot_message, chatbot_log, chatbot_contactlead).
python manage.py makemigrations chatbot
python manage.py migrate

# 6. Build the ChromaDB vector store (first run will download a ~90 MB embedding model).
python manage.py build_vectorstore

# 7. Add chroma_db/ to .gitignore so the local index isn't committed.
echo "chroma_db/" >> .gitignore

# 8. Run the dev server.
python manage.py runserver
```

That's it. The bubble appears on every page; click it to chat. On `/contact/`
the bot automatically switches to contact-funnel mode.

---

## 3. What was actually changed in existing files

### `axialfoundry/settings.py`
Three new apps (`rest_framework`, `corsheaders`, `chatbot`), one new middleware
entry (`corsheaders.middleware.CorsMiddleware`), and an appended block:

- Chatbot config (`GEMINI_API_KEY`, `CHATBOT_GEMINI_MODEL`, `CHROMA_DB_PATH`,
  `KNOWLEDGE_BASE_PATH`, `CHATBOT_MAX_HISTORY_TURNS`, etc.)
- `CORS_ALLOWED_ORIGINS` (open in DEBUG, restricted in production)
- `REST_FRAMEWORK` settings with a 60/min anonymous throttle
- `LOGGING.loggers.chatbot` for separate chatbot log control

No existing setting is removed or modified in meaning.

### `axialfoundry/urls.py`
A single new line:
```python
path('api/chat/', include('chatbot.urls')),
```

### `templates/base.html`
A single new line right before `</body>`:
```html
{% include 'chatbot/widget.html' %}
```

### `requirements.txt`
Five new dependencies appended.

---

## 4. Configuration knobs

Set these in `.env`:

| Var | Default | Purpose |
|-----|---------|---------|
| `GEMINI_API_KEY` | _(empty)_ | Required for chat replies |
| `CHATBOT_GEMINI_MODEL` | `gemini-2.5-flash` | Model name |
| `CHATBOT_EMBED_MODEL` | `all-MiniLM-L6-v2` | sentence-transformers model |
| `CHATBOT_MAX_HISTORY_TURNS` | `10` | History sent to Gemini per turn |
| `CHATBOT_RETRY_DELAY_SECONDS` | `30` | Delay before background retry |
| `CHATBOT_STATIC_FALLBACK_MSG` | _(see settings)_ | Shown when Gemini fails |
| `CORS_ALLOWED_ORIGINS` | `https://axialfoundary.com,...` | Production origins |

If your knowledge base ever changes, edit `data/knowledge_base.md` and re-run
`python manage.py build_vectorstore` — the existing index is wiped and rebuilt
in place.

---

## 5. API surface

Public endpoints (no auth, anonymous-throttled at 60/min):

| Method | Path | Body / Query | Purpose |
|--------|------|--------------|---------|
| POST | `/api/chat/start/` | _(none)_ | Create session → `{ session_id }` |
| POST | `/api/chat/message/` | `{ session_id, message, mode? }` | Send message → `{ reply, ... }` |
| GET  | `/api/chat/history/` | `?session_id=<uuid>` | Full conversation |
| POST | `/api/chat/mode/` | `{ session_id, mode }` | Switch chat ↔ contact_funnel |

The frontend widget hits all four automatically — you don't need to call them
yourself.

---

## 6. Test checklist

- [ ] `python manage.py build_vectorstore` completes; `chroma_db/` appears.
- [ ] `python manage.py migrate` creates the four new tables.
- [ ] `POST /api/chat/start/` returns a UUID.
- [ ] Asking "what services do you offer?" returns a coherent grounded answer.
- [ ] Asking "what model are you?" returns the canned identity reply (no Gemini mention).
- [ ] Asking "what's the capital of France?" returns the off-topic refusal.
- [ ] Clearing or invalidating `GEMINI_API_KEY` returns the static fallback (not a 500).
- [ ] `/contact/` page opens the widget in funnel mode and walks through all 6 fields.
- [ ] After completion, `ContactLead.completed = True` is visible in `/admin/`.
- [ ] A session UUID persists across page refreshes.
- [ ] Conversation history loads from `/api/chat/history/` on widget open.

---

## 7. Operational notes

- **The retry queue uses daemon threads.** This is fine for single-process dev
  servers and gunicorn. For multi-worker setups the queue lives per-worker —
  for higher reliability, swap `retry_queue.py` for Celery or RQ later.
- **First chat request is slow** because `sentence-transformers` and the Chroma
  client are lazily loaded. After that, retrieval is ~50 ms per query.
- **No raw SQL.** Every DB write goes through Django ORM.
- **No model-name leakage.** The system prompt forbids it; the bot will only
  ever identify as the "Axial Foundary Assistant".
- **Existing `leads.Lead` is untouched.** `chatbot.ContactLead` is a separate,
  chatbot-specific funnel capture. If you want to merge them later, treat
  `ContactLead` as the staging table and copy completed rows to `leads.Lead`.
