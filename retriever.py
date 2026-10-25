from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

index_name = "aman-info-db"
embedding = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

vector_store = PineconeVectorStore(
    embedding=embedding,
    index_name=index_name
)
retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={"k":6, "fetch_k":20,"lambda_mult": 0.8}  # value from 0 to 1 (1 as similarity search and 0 for very diverse)
)
