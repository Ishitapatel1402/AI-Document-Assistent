import json
import os

METADATA_PATH = "vectorstore/metadata.json"


def save_metadata(document_name, chunk_count, file_hash):

    metadata = {
        "document_name": document_name,
        "chunk_count": chunk_count,
        "file_hash": file_hash
    }

    os.makedirs("vectorstore", exist_ok=True)

    with open(METADATA_PATH, "w") as f:
        json.dump(metadata, f, indent=4)


def load_metadata():

    if os.path.exists(METADATA_PATH):

        with open(METADATA_PATH, "r") as f:
            return json.load(f)

    return None