Lab 3: Document Retrieval System

Semantic search system using ChromaDB and sentence transformers  
for **ARIN 5360 at Seattle University**

 ---

Setup

```bash
# Install dependencies
uv sync

Running the Server
uv run uvicorn src.retrieval.main:app --reload


Server starts at:
http://localhost:8000

Usage
Web Interface

Visit:
http://localhost:8000

API
Health Check
curl http://localhost:8000/health

Search
curl -X POST http://localhost:8000/search \
  -H "Content-Type: application/json" \
  -d '{"query": "machine learning", "n_results": 5}'

Testing
# Run all tests with coverage
uv run pytest

# Run with coverage report
uv run pytest --cov=src/retrieval --cov-report=html

# Smoke test only
uv run pytest tests/test_smoke.py

Code Quality
# Check formatting
uv run ruff format --check .

# Format code
uv run ruff format .

# Lint
uv run ruff check .

Project Structure
lab3/
├── src/retrieval/          # Source code
│   ├── embeddings.py      # Document embedder
│   ├── loader.py          # Document loader
│   ├── store.py           # Vector store
│   ├── retriever.py       # Main retriever
│   └── main.py             # FastAPI application
├── tests/                 # Test files
├── static/                # Web interface
├── documents/             # Sample documents
└── pyproject.toml         # Project configuration

Architecture

Loader: Reads .txt files from documents/

Embedder: Converts text to vectors using sentence-transformers

Store: Manages ChromaDB collection for similarity search

Retriever: Coordinates components for end-to-end retrieval

API: FastAPI endpoints for health checks and search

Adding Documents

Place .txt files in the documents/ directory and restart the server.
Documents are indexed automatically on startup.