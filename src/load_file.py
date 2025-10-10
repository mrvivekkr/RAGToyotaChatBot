import requests
import streamlit as st
from tempfile import NamedTemporaryFile
from langchain_community.document_loaders import PyPDFLoader


# Function for loading and caching the content of the PDF file
@st.cache_data
def load_pdf_content(user_manual_url):
    # Download the PDF from the URL and save it temporarily
    with NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        response = requests.get(user_manual_url)
        tmp_file.write(response.content)
        tmp_file_path = tmp_file.name

    # Load the PDF content using PyPDFLoader
    pdf_loader = PyPDFLoader(tmp_file_path)
    pdf_reader = pdf_loader.load()

    # Extract and format the content
    content = [(page.page_content.replace('\n', '\n\n')
                if page.page_content else '...') for page in pdf_reader]
    return content


# Function for displaying the PDF file and the images
def load_file():
    user_manual_url = 'https://raw.githubusercontent.com/mrvivekkr/project-assets/main/toyota-interactive-bot/car-manual/Toyota-Highlander-2024.pdf'

    with st.spinner('Loading PDF content. Please wait around a minute...'):
        content = load_pdf_content(user_manual_url)

    if content:

        with st.container(height=600, border=False):
            col_left, col_right = st.columns(2)

            # Display the images
            with col_left:
                image_path = "https://raw.githubusercontent.com/mrvivekkr/project-assets/main/toyota-interactive-bot/images/Toyota_3.jpg"
                st.image(image_path, use_container_width=True)

                image_path = "https://raw.githubusercontent.com/mrvivekkr/project-assets/main/toyota-interactive-bot/images/Toyota_4.jpg"
                st.image(image_path, use_container_width=True)

            with col_right:
                image_path = "https://raw.githubusercontent.com/mrvivekkr/project-assets/main/toyota-interactive-bot/images/Toyota_5.jpg"
                st.image(image_path, use_container_width=True)

                image_path = "https://raw.githubusercontent.com/mrvivekkr/project-assets/main/toyota-interactive-bot/images/Toyota_6.jpg"
                st.image(image_path, use_container_width=True)

        return content

    else:
        st.error('User Manual not found')
        return None