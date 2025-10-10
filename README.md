# RAGToyotaChatBot

This project is a Retrieval-Augmented Generation (RAG) chatbot designed to help Toyota Highlander owners quickly find answers from their official 2024 user manual. It combines a semantic search over the PDF manual with a large language model, providing step-by-step, easy-to-follow answers through a modern chat interface.

---

## Key Features

- Conversational chat UI (built with Streamlit)
- RAG pipeline: vector search + LLM for reliable, referenced answers
- PDF loader and chunker (adapts Toyota manuals into a searchable format)
- Handles context, chat memory, and real streaming
- Modular design: easy to extend for other manuals/domains

---

## Technologies Used

- Python 3 (core language)
- Streamlit (web UI)
- LangChain (chains, prompts, orchestration)
- Groq API (LLM backend, can swap with others)
- Chroma DB (vector database for fast embedding-based retrieval)
- dotenv (local environment config)
- PyPDFLoader (PDF parsing)

---

## How It Works

1. The Toyota manual PDF is loaded, split into chunks, and converted into embeddings.
2. These embeddings are stored in a vector store for fast semantic retrieval.
3. When a user asks a question, the app:
   - Finds the most relevant manual snippets using vector search
   - Feeds these, along with the question and chat history, into an LLM using a prompt template
   - Streams the answer to the chat UI, referencing the manual
4. All chat history is remembered for the session.

---


## Getting Started

1. **Clone the repo**

- git clone https://github.com/mrvivekkr/RAGToyotaChatBot.git
- cd RAGToyotaChatBot

2. **Install dependencies**

- pip install -r requirements.txt


3. **Set up environment variables**

- fill in your API keys in `.env` 

4. **Run the chatbot**
- streamlit run app.py

Then visit [http://localhost:8501](http://localhost:8501) in your browser.

---

## Example Questions to Try

- How do I enable lane departure alert?
- What does the yellow triangle warning light mean?
- How do I reset the tire pressure light?
- Can you explain the child seat installation steps?

---

## Running this on your own manual?

Replace the PDF URL inside `load_file.py` with your desired manual, and you’ll have a RAG chatbot for that domain with minimal changes.

---

Feel free to open issues or PRs if you see improvements, bugs, or want to port this to other domains!
