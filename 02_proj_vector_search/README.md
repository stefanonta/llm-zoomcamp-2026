# 02: Project - Vector Search

**Module 2 project** for [LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp). Vector search over course lesson content using a local ONNX embedding model, with no GPU or PyTorch required at runtime.

## What this module covers

- Downloading and running an ONNX embedding model (`Xenova/all-MiniLM-L6-v2`)
- Encoding text to 384-dimensional vectors with `onnxruntime`
- Fetching lesson markdown from GitHub via `gitsource`
- Building a minsearch index with precomputed embeddings
- Homework questions on embedding values and nearest-neighbor search

## Project structure

| File | Purpose |
|------|---------|
| `notebook.ipynb` | Main project notebook and homework |
| `embedder.py` | `Embedder` class: tokenize, run ONNX model, mean-pool, normalize |
| `download.py` | Download ONNX model and tokenizer from Hugging Face Hub |
| `models/` | Downloaded model files (gitignored; run `download.py` after cloning) |

## Setup

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```bash
cd 02_proj_vector_search
uv sync
```

Download the embedding model (not tracked in git):

```bash
uv run python download.py
```

This saves `tokenizer.json` and `model.onnx` under `models/Xenova/all-MiniLM-L6-v2/`.

## Usage

Open the notebook and run cells in order:

```bash
uv run jupyter notebook notebook.ipynb
```

Quick sanity check from the command line:

```bash
uv run python -c "
from embedder import Embedder
e = Embedder()
v = e.encode('How does approximate nearest neighbor search work?')
print(v.shape, v[0])
"
```

## Dependencies

- `onnxruntime`: run the ONNX embedding model on CPU
- `tokenizers`: fast tokenization
- `numpy`: vector math
- `minsearch`: search index with vector support
- `gitsource`: fetch course lessons from GitHub
- `huggingface-hub` (dev): model download
- `jupyter` (dev): interactive notebook
