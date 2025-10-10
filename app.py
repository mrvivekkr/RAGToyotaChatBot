import streamlit as st
from src.session_states import initialize_params

# Set the Streamlit page parameters
st.set_page_config(layout="wide",
                   initial_sidebar_state='expanded',
                   page_icon="👻",
                   page_title='GPT Document Analyzer')

############################# Function for displaying the introduction page ##################################
def display_intro():
    #  # Section 1: Logo and Introductory Text
    st.image("https://upload.wikimedia.org/wikipedia/commons/e/e7/Toyota.svg", width=300)
    st.title("TOYOTA USER MANUEL")
    st.subheader("Got questions about the Toyota Highlander?")
    st.write("Interact with our chatbot by using the side menu...")

    # Section 2 => Image and video
    col_left, col_right = st.columns([0.50, 0.50])

    with col_left:
        video_path = "https://www.youtube.com/watch?v=N-EQ_08Ptu4"
        st.video(video_path)

    with col_right:
        image_path = "https://tmna.aemassets.toyota.com/is/image/toyota/toyota/vehicles/2025/highlander/gallery/HLH_MY25_0001_V001.png?wid=2000&fmt=jpg"
        st.image(image_path, use_container_width=True)

initialize_params()
display_intro()