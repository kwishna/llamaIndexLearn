import chromadb
from chromadb.config import Settings

settings = Settings(chroma_api_impl="rest",
                    chroma_server_host="localhost",
                    chroma_server_http_port="8000"
                    )
chroma_client = chromadb.Client(settings)

# list all collections
print(chroma_client.list_collections())

# # make a new collection
# collection = chroma_client.create_collection("testname")
#
# # get an existing collection
# collection = chroma_client.get_collection("testname")

# get a collection or create if it doesn't exist already
collection = chroma_client.get_or_create_collection("testname")

# delete a collection
# chroma_client.delete_collection("testname")

# resets entire database - this *cant* be undone!
# chroma_client.reset()

# returns timestamp to check if service is up
chroma_client.heartbeat()

# change the name or metadata on a collection
collection.modify(name="testname2")

# get the number of items in a collection
print(collection.count())

# add new items to a collection
# either one at a time
collection.add(
    embeddings=[1.5, 2.9, 3.4],
    metadatas={"uri": "img9.png", "style": "style1"},
    documents="doc1000101",
    ids="uri9",
)
# or many, up to 100k+!
# collection.add(
#     embeddings=[[1.5, 2.9, 3.4], [9.8, 2.3, 2.9]],
#     metadatas=[{"style": "style1"}, {"style": "style2"}],
#     ids=["uri9", "uri10"],
# )
# collection.add(
#     documents=["doc1000101", "doc288822"],
#     metadatas=[{"style": "style1"}, {"style": "style2"}],
#     ids=["uri9", "uri10"],
# )

# update items in a collection
# collection.update()

# upsert items. new items will be added, existing items will be updated.
collection.upsert(
    ids=["id1", "id2", "id3", ...],
    embeddings=[[1.1, 2.3, 3.2], [4.5, 6.9, 4.4], [1.1, 2.3, 3.2], ...],
    metadatas=[{"chapter": "3", "verse": "16"}, {"chapter": "3", "verse": "5"}, {"chapter": "29", "verse": "11"}, ...],
    documents=["doc1", "doc2", "doc3", ...],
)

# get items from a collection
print(collection.get())

# convenience, get first 5 items from a collection
print(collection.peek())

# do nearest neighbor search to find similar embeddings or documents, supports filtering
result = collection.query(
    query_embeddings=[[1.1, 2.3, 3.2], [5.1, 4.3, 2.2]],
    n_results=2,
    where={"style": "style2"}
)

print(result)

# delete items
collection.delete()
