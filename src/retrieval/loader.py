from pathlib import Path

class DocumentLoader(object):
    def __init__(self, documents):
        self.documents = self.load_documents(documents)

    def load_documents(self, directory: str) -> list[dict]:
        documents = []
        path = Path(directory)
        for filepath in path.glob("*.txt"):
            with open(filepath, 'r', encoding='utf-8') as f:
                text = f.read().strip()
            if text:
                documents.append({
                    'id': filepath.stem,
                    'text': text,
                    'metadata': {'filename': filepath.name}
                })
        return documents

if __name__ == "__main__":
    print("Run the main.py")
