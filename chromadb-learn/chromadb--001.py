import json

import chromadb
from chromadb.config import Settings

settings = Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory="./persistent_dir" # Optional, defaults to .chromadb/ in the current directory,
)

# Create a ChromaClient object.
# This will connect to the Chroma database.
chroma_client = chromadb.Client(settings)

# Create a collection named "my_collection".
# This will create a new collection in the Chroma database.
collection = chroma_client.create_collection(name="my_collection", get_or_create=True)

# Add two documents to the collection:
#   - "This is a document"
#   - "This is another document"
# The `documents` parameter is a list of strings.
# The `meta-datas` parameter is a list of dictionaries.
# The `ids` parameter is a list of strings.
collection.add(
    documents=["This is a document", "This is another document"],
    metadatas=[{"source": "my_source"}, {"source": "my_source"}],
    ids=["id1", "id2"]
)

# Query the collection for documents that match the query text "This is a query document".
# The `query_texts` parameter is a list of strings.
# The `n_results` parameter specifies the number of results to return.
results = collection.query(
    query_texts=["This is a query document"],
    n_results=2
)

# Print the results.
print(json.dumps(results, indent=4))
