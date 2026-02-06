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


class DocumentLoader:
    def load_documents(self, directory: str) -> list[dict]:
        documents = []
        path = Path(directory)
        if not path.is_dir() or not path.exists():
            raise FileNotFoundError(f"Directory {directory} does not exist")
        for filepath in path.glob("*.txt"):
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    text = f.read().strip()
                if text:
                    documents.append(
                        {"id": filepath.stem, "text": text, "metadata": {"filename": filepath.name}}
                    )
            except Exception as e:
                logging.error(e)
        return documents


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
