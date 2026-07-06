# 01: Course - Agentic RAG

Course exercises for **Module 1** of [LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp). Builds a FAQ chatbot that answers questions about the course using retrieval-augmented generation (RAG).

## What this module covers

- Fetching FAQ data from the DataTalks.Club API
- Building a searchable index with [minsearch](https://github.com/alexeygrigorev/minsearch) (in-memory BM25)
- Persisting and querying FAQs with [sqlitesearch](https://github.com/alexeygrigorev/sqlitesearch) (SQLite FTS)
- Prompt construction and LLM generation with the OpenAI API

## Project structure

| File | Purpose |
|------|---------|
| `ingest.py` | Load FAQ JSON from DataTalks.Club and build a minsearch index |
| `ingest_sql.py` | Ingest llm-zoomcamp FAQs into a persistent SQLite index (`faqs.db`) |
| `persistent_rag.py` | Query the SQLite index directly |
| `rag_helper.py` | `RAGbase` class: search, context building, and LLM call |
| `main.py` | End-to-end demo: load index, run sample questions |
| `notebook-main.ipynb` | Jupyter walkthrough (course notes) |

## Setup

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```bash
cd 01_course_agentic_rag
uv sync
```

Create `.env` with your OpenAI API key:

```env
OPENAI_API_KEY=sk-...
```

## Usage

**Build the persistent SQLite index** (first time, or to refresh data):

```bash
uv run python ingest_sql.py
```

**Run the demo script:**

```bash
uv run python main.py
```

**Explore interactively:**

```bash
uv run jupyter notebook
```

## Dependencies

- `minsearch`: in-memory full-text search
- `sqlitesearch`: persistent SQLite FTS index
- `openai`: LLM API client
- `gitsource`: fetch files from GitHub (used in course notebooks)
- `jupyter`: interactive notebooks
