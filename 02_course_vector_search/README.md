# 02: Course - Vector Search

Course exercises for **Module 2** of [LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp). Explores embeddings, vector similarity search, and RAG with vector backends.

## What this module covers

- Text embeddings with [sentence-transformers](https://www.sbert.net/)
- Vector search with minsearch and sqlitesearch
- PostgreSQL + [pgvector](https://github.com/pgvector/pgvector) for production-style vector retrieval
- Combining vector search with RAG (`rag_helper.py`)

## Project structure

| File | Purpose |
|------|---------|
| `notebook.ipynb` | Core vector search concepts and exercises |
| `notebook_RAG.ipynb` | RAG pipeline with vector retrieval |
| `notebook_pgvector.ipynb` | pgvector setup and vector queries |
| `notebook_pgvector_RAG.ipynb` | Full RAG with pgvector backend |
| `noteboook_VS_RAG.ipynb` | Vector search vs. RAG comparison |
| `ingest.py` | Load FAQ data from DataTalks.Club |
| `rag_helper.py` | `RAGBase` with minsearch and pgvector search paths |

## Setup

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```bash
cd 02_course_vector_search
uv sync
```

Create `.env` with your credentials:

```env
OPENAI_API_KEY=sk-...

# Required for pgvector notebooks
DATABASE_URL=postgresql://user:password@localhost:5432/zoomcamp
```

For pgvector notebooks, you need a running PostgreSQL instance with the `vector` extension enabled. The course uses Docker; see the [module 2 materials](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/02-vector-search) for the exact setup.

## Usage

Start Jupyter and open the notebooks in order:

```bash
uv run jupyter notebook
```

Suggested flow:

1. `notebook.ipynb`: embeddings and basic vector search
2. `notebook_RAG.ipynb`: RAG with vector retrieval
3. `notebook_pgvector.ipynb`: migrate to PostgreSQL/pgvector
4. `notebook_pgvector_RAG.ipynb`: end-to-end pgvector RAG

## Dependencies

- `sentence-transformers`: embedding models
- `minsearch` / `sqlitesearch`: search indexes
- `psycopg`: PostgreSQL driver (pgvector notebooks)
- `openai`: LLM API client
- `jupyter`: interactive notebooks
