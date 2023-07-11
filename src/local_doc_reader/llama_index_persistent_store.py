import os
import openai
import dotenv
from llama_index import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage

dotenv.load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]

# Load documents from a directory
documents = SimpleDirectoryReader('book').load_data()

# Create an index from the documents
index = VectorStoreIndex.from_documents(documents)

# Create a query engine from the index
query_engine = index.as_query_engine()

# Query the engine
response = query_engine.query("What is this text about?")
print(response)

# Persist index to disk
index.storage_context.persist("persistent_db_index")