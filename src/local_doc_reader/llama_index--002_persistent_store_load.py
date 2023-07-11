import os

import dotenv
import openai
from llama_index import StorageContext, load_index_from_storage

dotenv.load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]

# Rebuild storage context
storage_context = StorageContext.from_defaults(persist_dir="persistent_db_index")

# Load index from the storage context
new_index = load_index_from_storage(storage_context)

new_query_engine = new_index.as_query_engine()
response = new_query_engine.query("who is this text about?")
print(response)
