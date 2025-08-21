from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

# Load reviews
df = pd.read_csv("realistic_restaurant_reviews.csv")

# Initialize embeddings
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

# Database location
db_location = "./chroma_langchain_db"
add_documents = not os.path.exists(db_location)

# Prepare documents
if add_documents:
    documents = []
    ids = []
    for i, row in df.iterrows():
        document = Document(
            page_content=row["Title"] + " " + row["Review"],
            id=str(i)
        )
        documents.append(document)
        ids.append(str(i))

# Initialize Chroma vector store
vector_store = Chroma(
    collection_name="restaurant_reviews",
    persist_directory=db_location,
    embedding_function=embeddings
)

# Add documents if first time
if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)

# Initialize retriever
retriever_store = vector_store.as_retriever(search_kwargs={"k": 3})

# Helper function to get clean reviews
def get_clean_reviews(query):
    docs = retriever_store.get_relevant_documents(query)
    reviews_text = ""
    for doc in docs:
        reviews_text += doc.page_content + "\n\n"  # add line breaks
    return reviews_text.strip()
