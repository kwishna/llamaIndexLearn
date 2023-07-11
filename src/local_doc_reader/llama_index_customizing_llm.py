from langchain.chat_models import ChatOpenAI
from llama_index import LLMPredictor, ServiceContext, VectorStoreIndex, SimpleDirectoryReader, Prompt

# Load documents from a directory
documents = SimpleDirectoryReader('book').load_data()

# Create a predictor using a custom model
llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo"))

# Create a service context with the custom predictor
service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

# Create an index using the service context
custom_llm_index = VectorStoreIndex.from_documents(documents, service_context=service_context)

custom_llm_query_engine = custom_llm_index.as_query_engine()
response = custom_llm_query_engine.query("who is this text about?")
print(response)

# -------------------- -------------------- -------------------- -------------------- --------------------

# Define a custom prompt
template = (
    "We have provided context information below. \n"
    "---------------------\n"
    "{context_str}"
    "\n---------------------\n"
    "Given this information, please answer the question and each answer should start with code word AI Demos: {query_str}\n"
)
qa_template = Prompt(template)

# Use the custom prompt when querying
query_engine = custom_llm_index.as_query_engine(text_qa_template=qa_template)
response = query_engine.query("who is this text about?")
print(response)
