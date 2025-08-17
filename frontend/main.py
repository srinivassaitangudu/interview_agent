import streamlit as st
import os, tempfile

import backend.resume_parser as barepa
import utils.theme as theme_utils

IS_DISABLED = True


def save_uploaded_to_temp(uploaded_file) -> str:
    # Preserve the extension so downstream libs behave (e.g., .pdf, .docx)
    ext = os.path.splitext(uploaded_file.name)[1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
        tmp.write(uploaded_file.getbuffer())
        return tmp.name

def resume_parser():
    with st.spinner("Parsing resume..."):
        resume_parser = barepa.ResumeParser()
        path = save_uploaded_to_temp(uploaded_file)
        file_content = resume_parser.parse_resume(path)
        st.write(file_content)
    st.success("Questions generated successfully!")
    
    
# Streamlit App
st.set_page_config(page_title="Interview Agent", page_icon="utils/images/icon.png", layout="centered", menu_items={"About": "This is a simple Streamlit app for the Interview Agent."})

theme_utils.apply_theme(st.session_state.get('theme', 'Light'))

st.title("Welcome to the Interview Agent App")
st.write("This is a simple Streamlit app for the Interview Agent.")


# --- IGNORE ---
uploaded_file = st.file_uploader("Upload your resume"+ ":red[*]", type=["pdf", "docx"], help="This field is required")
job_description = st.text_input("Enter your job description" + ":red[*]", help="This field is required")
instructions =st.text_input("Enter your Instructions", key="instructions", help="This field is optional")

if uploaded_file and job_description:
    IS_DISABLED = False
is_clicked = st.button(
    "Start!",
    key="start_button",
    disabled=IS_DISABLED,
    help="Click to start processing",
    use_container_width=True,
    on_click=resume_parser
   )


    


