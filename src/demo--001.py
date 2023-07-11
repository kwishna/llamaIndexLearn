from dotenv import load_dotenv
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, StorageContext

load_dotenv()

documents = SimpleDirectoryReader('../news').load_data()
index = GPTVectorStoreIndex.from_documents(documents)

index.storage_context.persist(persist_dir='simple_index.json')

query_engine = index.as_query_engine()
r = query_engine.query("what is langchain?")
print(r)
