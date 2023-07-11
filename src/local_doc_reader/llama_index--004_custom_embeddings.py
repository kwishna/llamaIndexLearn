from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from llama_index import LangchainEmbedding, ServiceContext, VectorStoreIndex, SimpleDirectoryReader

# Load in a specific embedding model
embed_model = LangchainEmbedding(HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2'))

# Create a service context with the custom embedding model
service_context = ServiceContext.from_defaults(embed_model=embed_model)

documents = SimpleDirectoryReader('book').load_data()

# Create an index using the service context
new_index = VectorStoreIndex.from_documents(documents, service_context=service_context)

query_engine = new_index.as_query_engine()

response = query_engine.query("list 5 important points from the text")
print(response)
