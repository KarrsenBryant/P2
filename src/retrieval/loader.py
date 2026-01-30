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


if __name__ == "__main__":
    print("Run the main.py")
