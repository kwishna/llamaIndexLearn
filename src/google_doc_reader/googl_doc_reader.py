from llama_index import GPTVectorStoreIndex
from llama_hub.google_docs.base import GoogleDocsReader
from llama_index.indices.base import BaseIndex

gdoc_ids = ['1wf-y2pd9C878Oh-FmLH7Q_BQkljdm6TQal-c1pUfrec']
loader = GoogleDocsReader()
documents = loader.load_data(document_ids=gdoc_ids)
index: BaseIndex = GPTVectorStoreIndex.from_documents(documents)
print(index.as_query_engine().query('Where did the author go to school?'))