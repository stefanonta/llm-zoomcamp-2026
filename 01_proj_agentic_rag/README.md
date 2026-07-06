# 01: Project - Agentic RAG

**Module 1 project** for [LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp). A FAQ chatbot for prospective students, built in two phases: static RAG first, then agentic RAG with tool calling.

## What this module covers

- **Phase 1 (Static RAG):** fetch course lesson markdown from GitHub, index with minsearch, answer questions with OpenAI
- **Phase 2 (Agentic RAG):** extend the assistant with function calling so the LLM can search the knowledge base on demand ([toyaikit](https://github.com/alexeygrigorev/toyaikit))

## Project structure

| File | Purpose |
|------|---------|
| `hw.ipynb` | Main project notebook: static RAG, then agentic RAG |
| `rag_helper.py` | `RAGBase` class for search, prompt building, and generation |
| `rag_schema.py` | Tool/function schemas for the agentic assistant |
| `test_script.py` | Small utility script for quick checks |

## Setup

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```bash
cd 01_proj_agentic_rag
uv sync
```

Create `.env` with your OpenAI API key:

```env
OPENAI_API_KEY=sk-...
```

## Usage

Open the project notebook and run cells in order:

```bash
uv run jupyter notebook hw.ipynb
```

The notebook walks through:

1. Retrieving lesson markdown from the [llm-zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp) GitHub repo via `gitsource`
2. Chunking and indexing content with `minsearch`
3. Building a static RAG pipeline with `RAGBase`
4. Converting to an agentic assistant with `toyaikit` and structured tool schemas

## Dependencies

- `gitsource`: fetch course lessons from GitHub
- `minsearch`: in-memory full-text search over lesson chunks
- `openai`: LLM API client
- `toyaikit`: lightweight agent framework with tool calling
- `jupyter`: interactive notebook
