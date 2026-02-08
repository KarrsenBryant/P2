# Lab 3: Document Retrieval System

Semantic search system using ChromaDB and sentence transformers  
for **ARIN 5360 at Seattle University**

 ---

## Setup

```bash
git clone https://github.com/KarrsenBryant/P2
# Install dependencies
uv sync
```

## Running the Server
```
uv run uvicorn src.retrieval.main:app --reload
```

Server starts at:
http://localhost:8000

---

## Usage
Web Interface

![Alt text](images/HomePageImage)

Visit:
http://localhost:8000

API
Health Check
curl http://localhost:8000/health

Search
curl -X POST http://localhost:8000/search \
  -H "Content-Type: application/json" \
  -d '{"query": "machine learning", "n_results": 5}'

---

## Testing
### Run all tests with coverage
uv run pytest

### Run with coverage report
uv run pytest --cov=src/retrieval --cov-report=html

### Smoke test only
uv run pytest tests/test_smoke.py

Code Quality
### Check formatting
uv run ruff format --check .

### Format code
uv run ruff format .

### Lint
uv run ruff check .

## Project Structure
```
P2/
├── documents/
│   ├── dracula_by_bram_stoker.txt
│   ├── sample1.txt
│   ├── sample2.txt
│   ├── sample3.txt
│   └── sample4.txt
├── images/
│   └── HomePageImage
├── pyproject.toml
├── README.md
├── src/
│   └── retrieval/
│       ├── __init__.py
│       ├── embeddings.py
│       ├── loader.py
│       ├── main.py
│       ├── retriever.py
│       └── store.py
├── static/
│   ├── index.html
│   └── style.css
├── tests/
│   ├── __init__.py
│   ├── data/
│   │   ├── dracula_by_bram_stoker.txt
│   │   └── MSAI-courses.pdf
│   ├── test_chunking.py
│   ├── test_embeddings.py
│   ├── test_integration.py
│   ├── test_loader.py
│   ├── test_retriever.py
│   ├── test_smoke.py
│   └── test_store.py
└── uv.lock

```

## Architecture

Loader: Reads .txt files from documents/

Embedder: Converts text to vectors using sentence-transformers

Store: Manages ChromaDB collection for similarity search

Retriever: Coordinates components for end-to-end retrieval

API: FastAPI endpoints for health checks and search

Adding Documents

Place .txt files in the documents/ directory and restart the server.
Documents are indexed automatically on startup.