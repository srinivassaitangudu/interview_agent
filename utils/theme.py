import streamlit as st

THEMES ={
    "Light": {
        "bg": "#FFFFFF",
        "bg2": "#F5F7FB",
        "text": "#0E1117",
        "primary": "#4B8AFF",
        "muted": "#6B7280",
        "card_shadow": "0 10px 30px rgba(0,0,0,.06)",
    },
    "Dark": {
        "bg": "#0E1117",
        "bg2": "#1A1D23",
        "text": "#FFFFFF",
        "primary": "#4B8AFF",
        "muted": "#9CA3AF",
        "card_shadow": "0 10px 30px rgba(0,0,0,.3)",
    }
}

def apply_theme(theme_name: str):
    theme = THEMES.get(theme_name, THEMES["Light"])
    st.session_state['theme'] = theme_name
    st.markdown(
        f"""
        <style>
        :root {{
          --app-bg: {theme['bg']};
          --app-bg2: {theme['bg2']};
          --text: {theme['text']};
          --primary: {theme['primary']};
          --muted: {theme['muted']};
          --shadow: {theme['shadow']};
          --border: {theme['border']};
        }}

        /* App background (whole page) */
        [data-testid="stAppViewContainer"] {{
          background: var(--app-bg) !important;
          color: var(--text) !important;
        }}

        /* Header bar */
        [data-testid="stHeader"] {{
          background: var(--app-bg) !important;
          color: var(--text) !important;
          border-bottom: var(--border);
        }}

        /* Main content card */
        .block-container {{
          background: var(--app-bg) !important;
          color: var(--text) !important;
        }}

        /* Sidebar panel */
        [data-testid="stSidebar"] > div:first-child {{
          background: var(--app-bg2) !important;
          color: var(--text) !important;
          border-right: var(--border);
        }}

        /* Text elements */
        h1, h2, h3, h4, h5, h6,
        .stMarkdown, .stText, p, li, span, label {{
          color: var(--text) !important;
        }}

        /* Links */
        a, a:visited {{
          color: var(--primary) !important;
        }}

        /* Buttons */
        .stButton > button {{
          background: var(--primary) !important;
          color: #fff !important;
          border: 0 !important;
          border-radius: 10px !important;
          box-shadow: var(--shadow) !important;
        }}
        .stButton > button:hover {{ filter: brightness(0.95); }}

        /* Inputs */
        .stTextInput input, .stNumberInput input, .stTextArea textarea,
        .stDateInput input, .stFileUploader label, .stSlider > div {{
          background: var(--app-bg2) !important;
          color: var(--text) !important;
          border: var(--border) !important;
          border-radius: 10px !important;
        }}

        /* Selectbox / multiselect (BaseWeb) */
        div[data-baseweb="select"] > div {{
          background: var(--app-bg2) !important;
          color: var(--text) !important;
          border: var(--border) !important;
          border-radius: 10px !important;
        }}

        /* Expander */
        details {{
          background: var(--app-bg2) !important;
          color: var(--text) !important;
          border: var(--border) !important;
          border-radius: 10px !important;
          padding: .25rem .5rem !important;
        }}

        /* Tabs */
        .stTabs [role="tablist"] button {{
          color: var(--text) !important;
          border-bottom: 2px solid transparent !important;
        }}
        .stTabs [role="tab"][aria-selected="true"] {{
          border-bottom: 2px solid var(--primary) !important;
        }}

        /* Tables / DataFrames (best-effort) */
        .stDataFrame, .stTable {{
          color: var(--text) !important;
        }}
        .stDataFrame [role="grid"], .stTable table {{
          background: var(--app-bg2) !important;
          border: var(--border) !important;
        }}

        /* Metrics */
        [data-testid="stMetricValue"], [data-testid="stMetricDelta"] {{
          color: var(--text) !important;
        }}

        /* Code blocks */
        pre, code, .stCodeBlock {{
          background: var(--app-bg2) !important;
          color: var(--text) !important;
          border: var(--border) !important;
          border-radius: 10px !important;
        }}

        /* Scrollbars (WebKit) */
        ::-webkit-scrollbar {{ width: 10px; height: 10px; }}
        ::-webkit-scrollbar-thumb {{
          background: rgba(128,128,128,.35);
          border-radius: 10px;
        }}
        ::-webkit-scrollbar-track {{ background: transparent; }}
        </style>
        """,
        unsafe_allow_html=True,
    )