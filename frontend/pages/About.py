import streamlit as st
import os, tempfile
import utils.theme as theme_utils

def about_page():
    theme_utils.apply_theme(st.session_state.get('theme', 'Light'))

    st.title("About the Interview Agent")
    st.write("This is a simple Streamlit app for the Interview Agent.")
    st.write("## Features")
    st.write("- Resume parsing")
    st.write("- Job description analysis")
    st.write("- Question generation")
    st.write("## Technologies Used")
    st.write("- Streamlit")
    st.write("- OpenAI API")
    st.write("- Pinecone")      
    st.write("## Author")
    st.write("Developed by Nivas")              
    st.write("## Contact")
    st.write("For any queries, reach out at")
    st.write("Email: nivas@example.com     GitHub: [nivas](https://github.com/nivas).       LinkedIn: [nivas](https://www.linkedin.com/in/nivas/)")
    st.write("## Acknowledgements")
    st.write("- Thanks to the Streamlit community for their support.")
    st.write("- Inspired by the work of others in the field.")

if __name__ == "__main__":
    about_page()