"""
Embedding functions for document retrieval.

@author: Sarah Ruhl and Karrsen Bryant
Seattle University, ARIN 5360
@see: https://catalog.seattleu.edu/preview_course_nopop.php?catoid=55&coid
=190380
@version: 1.0.0+w26
"""

import numpy as np
from sentence_transformers import SentenceTransformer


class DocumentEmbedder:
    """
    Object for embedding documents.
    """

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """Initialize embedder with the specified model."""
        self.model_name = model_name
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, texts: list[str]) -> np.ndarray:
        """Generate embeddings for multiple documents."""
        return self.model.encode(texts, show_progress_bar=False)

    def embed_query(self, queries: str | list[str]) -> np.ndarray:
        """Generate embedding for a single query."""
        if isinstance(queries, str):
            queries = [queries]
            results = self.embed_documents(queries)
            return results[0]
        else:
            return self.embed_documents(queries)
