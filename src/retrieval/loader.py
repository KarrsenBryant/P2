"""
Lab 3 FastAPI API.
@author: Karrsen Bryant, Sarah Ruhl
Seattle University, ARIN 5360
@see: https://catalog.seattleu.edu/preview_course_nopop.php?catoid=55&coid
=190380
@version: 0.1.0+w26
"""

import logging
from pathlib import Path

import pypdf


class DocumentLoader:
    def __init__(self, chunker=None):
        """Initialize the document loader with optitional chunker"""
        self.chunker = chunker

    def load_documents(self, directory: str) -> list[dict]:
        documents = []
        path = Path(directory)
        if not path.is_dir() or not path.exists():
            raise FileNotFoundError(f"Directory {directory} does not exist")
        for filepath in path.glob("*.txt"):
            try:
                logging.info(f"Loading document: {filepath}")
                docs = self._load_text_file(filepath)
                documents.extend(docs)

            except Exception as e:
                logging.error(e)

        for filepath in path.glob("*.pdf"):
            logging.info(f"Loading document: {filepath}")
            docs = self._load_pdf_file(filepath)
            documents.extend(docs)

        return documents

    def _load_pdf_file(self, filepath: Path) -> list[dict]:
        """Load a single PDF file."""
        try:
            reader = pypdf.PdfReader(filepath)

            # Extract text from all pages
            text_parts = []
            for page in reader.pages:
                text_parts.append(page.extract_text())

            text = "\n\n".join(text_parts).strip()

            if not text:
                return []

            doc_id = filepath.stem
            metadata = {"filename": filepath.name, "type": "pdf", "num_pages": len(reader.pages)}

            if self.chunker:
                chunks = self.chunker.chunk_text(text, doc_id)
                # Add PDF metadata to each chunk
                for chunk in chunks:
                    chunk["metadata"].update(metadata)
                return chunks
            else:
                return [{"id": doc_id, "text": text, "metadata": metadata}]

        except Exception as e:
            print(f"Warning: Failed to load {filepath}: {e}")
            return []

    def _load_text_file(self, filePath: Path):
        try:
            with open(filePath, "r", encoding="utf-8") as f:
                text = f.read().strip()

            if not text:
                return []

            doc_id = filePath.stem
            metadata = {"filename": filePath.name, "type": "txt"}

            if self.chunker:
                chunks = self.chunker.chunk_text(text, doc_id)
                for chunk in chunks:
                    chunk["metadata"].update(metadata)
                return chunks
            else:
                return [{"id": doc_id, "text": text, "metadata": metadata}]

        except Exception as e:
            logging.warning(f"Warning: file {filePath} could not be loaded:{e}")


class DocumentChunker:
    """Chunk documents into smaller pieces for better retrieval."""

    def __init__(self, chunk_size: int = 300, overlap: int = 30):
        if overlap < 0 or overlap > chunk_size:
            raise ValueError()

        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk_text(self, text: str, doc_id: str) -> list[dict]:
        """Split the given text into overlapping chunks...."""

        try:
            words = text.split()  # pull out words from text

            if len(words) <= self.chunk_size:
                return [
                    {"id": f"{doc_id}_0", "text": text, "metadata": {"chunk": 0, "doc_id": doc_id}}
                ]

            chunks, start, chunk_num = [], 0, 0

            while start < len(words):
                end = start + self.chunk_size

                chunk_text = " ".join(words[start:end])

                chunks.append(
                    {
                        "id": f"{doc_id}_{chunk_num}",
                        "text": chunk_text,
                        "metadata": {"chunk": chunk_num, "doc_id": doc_id},
                    }
                )

                start = end - self.overlap
                chunk_num += 1

            return chunks
        except Exception as e:
            raise Exception(f"{doc_id} is invalid; {e}")


if __name__ == "__main__":
    print("Run the main.py")
