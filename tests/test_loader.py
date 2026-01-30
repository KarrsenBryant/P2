"""
Lab 3 FastAPI API.
@author: Karrsen Bryant, Sarah Ruhl
Seattle University, ARIN 5360
@see: https://catalog.seattleu.edu/preview_course_nopop.php?catoid=55&coid
=190380
@version: 0.1.0+w26
"""

import pytest

from src.retrieval.loader import DocumentLoader


def test_loader_loads_documents(tmp_path):
    """Test loading documents."""
    (tmp_path / "file1.txt").write_text("This is test file 1")
    (tmp_path / "file2.txt").write_text("This is test file 2")

    loader = DocumentLoader()

    documents = loader.load_documents(str(tmp_path))
    assert len(documents) == 2

    assert all("id" in doc for doc in documents)
    assert all("text" in doc for doc in documents)
    assert all("metadata" in doc for doc in documents)


def test_loader_skips_empty_documents(tmp_path):
    """Test skipping empty documents."""

    (tmp_path / "not_empty.txt").write_text("This is test file 1")
    (tmp_path / "empty_document.txt").write_text("   ")
    loader = DocumentLoader()

    documents = loader.load_documents(str(tmp_path))

    assert len(documents) == 1
    assert documents[0]["text"] == "This is test file 1"
    assert documents[0]["metadata"]["filename"] == "not_empty.txt"


def test_loader_skips_nonexistent_directory(tmp_path):
    """Test skipping non-existent directory."""
    loader = DocumentLoader()

    nonexistent_dir = tmp_path / "does_not_exist"

    with pytest.raises(FileNotFoundError):
        loader.load_documents(nonexistent_dir)
