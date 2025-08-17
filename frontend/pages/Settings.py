from dotenv import load_dotenv, set_key

load_dotenv()
import streamlit as st
import os, tempfile 
import utils.theme as theme_utils

def settings_page():
    theme_utils.apply_theme(st.session_state.get('theme', 'Light'))
    st.title("Settings")
    st.write("Adjust your application settings here.")
    st.write("## Theme")
    theme = st.selectbox("Select Theme", ["Light", "Dark"])
    theme_utils.apply_theme(theme)
    st.write(f"Current theme: {theme}")
    st.write("## API Keys")
    openai_key = st.text_input("OpenAI API Key", type="password")
    claude_key = st.text_input("Claude API Key", type="password")
    pinecone_key = st.text_input("Pinecone API Key", type="password")
    if st.button("Save Settings"):
        # Save keys and theme to .env in project root
        env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".env")
        env_path = os.path.abspath(env_path)
        set_key(env_path, "OPENAI_API_KEY", openai_key or os.getenv("OPENAI_API_KEY"))
        set_key(env_path, "CLAUDE_API_KEY", claude_key or os.getenv("CLAUDE_API_KEY"))
        set_key(env_path, "PINECONE_API_KEY", pinecone_key or os.getenv("PINECONE_API_KEY"))
        set_key(env_path, "APP_THEME", theme or os.getenv("APP_THEME"))
        st.write("Settings saved!")

    # st.write("## Notifications")
    # notifications = st.checkbox("Enable Email Notifications", value=True)
    # st.write(f"Email Notifications: {'Enabled' if notifications else 'Disabled'}")
    # st.write("## Account")
    # if st.button("Logout"):
    #     st.write("You have been logged out.")
    # return openai_key, claude_key, pinecone_key, theme

if __name__ == "__main__":
    settings_page()  