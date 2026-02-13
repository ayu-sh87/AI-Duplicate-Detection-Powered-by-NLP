import streamlit as st
import json

st.set_page_config(page_title="AI Platform", layout="wide")

# Load users
with open("users.json") as f:
    users = json.load(f)

# Theme toggle
theme = st.sidebar.toggle("Dark Mode", value=True)

if theme:
    st.markdown("""
        <style>
        .stApp { background-color: #0e1117; color: white; }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        .stApp { background-color: white; color: black; }
        </style>
    """, unsafe_allow_html=True)

# Login state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Login screen
if not st.session_state.logged_in:
    st.title("AI Duplicate Detection Platform")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in users and users[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Login successful")
            st.rerun()
        else:
            st.error("Invalid credentials")

# After login
else:
    st.sidebar.success(f"Logged in as {st.session_state.username}")
    st.title("Welcome to AI Platform")
    st.write("Use the sidebar to navigate.")
