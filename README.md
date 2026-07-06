# llm-zoomcamp-2026

Personal work for [LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp) by DataTalks.Club

## Modules

| Folder | Type | Description |
|--------|------|-------------|
| [`01_course_agentic_rag`](01_course_agentic_rag/) | Course | Module 1 lessons: FAQ RAG with minsearch and sqlitesearch |
| [`01_proj_agentic_rag`](01_proj_agentic_rag/) | Project | Module 1 project: static RAG over course lessons, then agentic RAG |
| [`02_course_vector_search`](02_course_vector_search/) | Course | Module 2 lessons: embeddings, vector search, pgvector |
| [`02_proj_vector_search`](02_proj_vector_search/) | Project | Module 2 project: ONNX embeddings and vector search over lessons |

## Getting started

Each module is a standalone [uv](https://docs.astral.sh/uv/) project with its own `pyproject.toml` and virtual environment.

```bash
cd <module-folder>
uv sync
```

Most modules need an OpenAI API key. Create a `.env` file in the module folder:

```env
OPENAI_API_KEY=sk-...
```

See each module's README for setup details, notebooks, and how to run the code.

## Repository layout

```
llm-zoomcamp-2026/
├── 01_course_agentic_rag/   # Module 1 course work
├── 01_proj_agentic_rag/     # Module 1 project
├── 02_course_vector_search/ # Module 2 course work
└── 02_proj_vector_search/   # Module 2 project
```
