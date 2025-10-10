import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

# Function for rewriting the user query
def rewrite_user_query(user_query):
    # Write down the original user query
    with st.container(border=True):
        st.markdown(user_query)

    # Define the LLM parameters
    groq_api_key = os.environ["GROQ_API_KEY"]
    model_name = "llama-3.1-8b-instant"
    llm = ChatGroq(temperature=0.5, groq_api_key=groq_api_key, model_name=model_name)

    # Define the re-writing query template with few shot examples
    template = f"""
    You are a smart assistant helping to rewrite user queries for a Toyota car manual chatbot.
    
    If the user's input is a greeting (e.g., "hello", "hi"), strictly respond politely with a greeting such as:
    "Hello! How can I help you with your Toyota Highlander?"
    
    If the user's input is unrelated to Toyota Highlander queries, respond politely:
    "I'm here to answer questions about the Toyota Highlander. Please ask a specific question about your vehicle or its manual."
    
    Otherwise, provide three better search queries as examples that relate to the Toyota Highlander manual.
    
    Example 1:
    User query:
    I have a red light on my dashboard
    
    Answer:
    1. Red dashboard light meaning.
    2. Car dashboard red light symptoms.
    3. Red warning light on dashboard diagnosis
    
    Example 2:
    User query:
    hello
    
    Answer:
    Hello! How can I help you with your Toyota Highlander?
    
    Example 3:
    User query:
    What is the weather outside?
    
    Answer:
    I'm here to answer questions about the Toyota Highlander. Please ask a specific question about your vehicle or its manual.

    {user_query}
    Answer:"""
    rewrite_prompt = ChatPromptTemplate.from_template(template)

    # Construct the LLM chain
    rewriter = rewrite_prompt | llm | StrOutputParser()
    # Invoke the LLM with the user query
    with st.spinner('Generating queries...'):
        rewritten_query = rewriter.invoke({'user_query': user_query})

    return rewritten_query