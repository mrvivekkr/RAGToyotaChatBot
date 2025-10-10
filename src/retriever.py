import os
import streamlit as st
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.schema import Document

# Suppress warnings
import warnings

from langchain_text_splitters import RecursiveCharacterTextSplitter

warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Function for retrieving the vector store
@st.cache_resource
def build_vector_store(content):
    if content:
        # If the vector store is not already present in the session state
        if not st.session_state.vector_store:

            with st.spinner(text=":red[Please wait while we fetch the information...]"):

                # Content is a list of strings (pages with double line breaks)
                # Prepare documents for LangChain
                # Each page is converted into a document with 'page_content' field
                docs = [Document(page_content=page) for page in content]

                # Split text into chunks
                text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
                split_docs = text_splitter.split_documents(docs)

                # Initialize embeddings
                embedding = HuggingFaceEmbeddings()

                persist_dir = "chroma_persist_dir"

                if os.path.exists(persist_dir) and os.listdir(persist_dir):
                    vector_store = Chroma(embedding_function=embedding,
                                          persist_directory=persist_dir,
                                          collection_name="car_manual")
                    print("Loaded persisted Chroma vector store.")
                else:
                    vector_store = Chroma.from_documents(
                        split_docs,
                        embedding,
                        persist_directory=persist_dir,
                        collection_name="car_manual"
                    )
                    vector_store.persist()
                    print("Built and persisted Chroma vector store.")

                st.session_state.vector_store = vector_store

                return vector_store
        else:
            # Load the vector store from the cache
            return st.session_state.vector_store

    else:
        st.error('No content was found...')


# Function for retrieving the relevant chunks from the vector store
def retrieve_chunks_from_vector_store(vector_store, re_written_query, min_score = 0.6):

    # Perform a similarity search with relevance scores
    with st.spinner(text=":red[Please wait while we fetch the relevant information...]"):
        relevant_documents = vector_store.similarity_search_with_score(query=re_written_query, k=5)
        if not relevant_documents or relevant_documents[0][1] < min_score:
            return None
        return relevant_documents

# Function for retrieving the chat history
def retrieve_history():
    # Go through all the chat messages in the history
    for message in st.session_state.messages:
        with st.container(border=True):
            with st.chat_message(message['role']):
                st.markdown(message['content'])