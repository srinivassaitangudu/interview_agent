import streamlit as st
import os, tempfile

import time
import backend.resume_parser as barepa


def save_uploaded_to_temp(uploaded_file) -> str:
    # Preserve the extension so downstream libs behave (e.g., .pdf, .docx)
    ext = os.path.splitext(uploaded_file.name)[1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
        tmp.write(uploaded_file.getbuffer())
        return tmp.name

st.title("Welcome to the Interview Agent App")
st.write("This is a simple Streamlit app for the Interview Agent.")

# --- IGNORE ---
uploaded_file = st.file_uploader("Upload your resume"+ ":red[*]", type=["pdf", "docx"], help="This field is required")
job_description = st.text_input("Enter your job description" + ":red[*]", help="This field is required")
instructions =st.text_input("Enter your Instructions", key="instructions", help="This field is optional")

is_clicked = st.button("Start!", key="start_button")

if is_clicked:
    if not uploaded_file:
        st.error("Please upload your resume file.")
        st.stop()
    if not job_description:
        st.error("Please enter the job description.")
        st.stop()
    # st.write("Processing your inputs...")
    with st.spinner("Parsing resume..."):

        resume_parser = barepa.ResumeParser()
        path = save_uploaded_to_temp(uploaded_file)
        file_content = resume_parser.parse_resume(path)
        st.write(file_content)
            
            # Here you would add the logic to process the uploaded file and job description
            # For example, you might call a function like:
            # response = process_inputs(st.uploaded_file, job_description, st.session_state.instructions)
        # st.write(response)
    st.success("Questions generated successfully!")