import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection("android_project")

def get_context(query):

    results = collection.query(
        query_texts=[query],
        n_results=3
    )

    return "\n\n".join(results["documents"][0])
