import streamlit as st
import json
import hashlib
import os
def password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c in "!@#$%^&*()" for c in password):
        score += 1

    if score <= 1:
        return "Weak", "red"
    elif score == 2:
        return "Medium", "orange"
    else:
        return "Strong", "green"

st.set_page_config(page_title="AI Platform", layout="wide")


# -----------------------------
# UI THEME (floating card)
# -----------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #e0f2ff, #cfe9ff, #b9dcff);
    font-family: 'Segoe UI', sans-serif;
}

.login-card {
    background: white;
    padding: 40px;
    border-radius: 18px;
    width: 380px;
    margin: auto;
    margin-top: 100px;
    box-shadow: 0 20px 60px rgba(0, 120, 255, 0.15);
    text-align: center;
}

.card-title {
    font-size: 26px;
    font-weight: 600;
    color: #0a2540;
    margin-bottom: 5px;
}

.card-subtitle {
    font-size: 14px;
    color: #5f6b7a;
    margin-bottom: 25px;
}

.stButton>button {
    background: linear-gradient(90deg, #4facfe, #00c6ff);
    color: white;
    border-radius: 10px;
    border: none;
    padding: 0.6em 1.2em;
    font-weight: bold;
    width: 100%;
}

.stTextInput>div>div>input {
    border-radius: 10px;
    border: 1px solid #d0d7e2;
}
</style>
""", unsafe_allow_html=True)


# -----------------------------
# Helper functions
# -----------------------------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def load_users():
    if not os.path.exists("users.json"):
        with open("users.json", "w") as f:
            json.dump({}, f)
    with open("users.json") as f:
        return json.load(f)


def save_users(users):
    with open("users.json", "w") as f:
        json.dump(users, f)


users = load_users()


# -----------------------------
# Session state
# -----------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "landing"


# -----------------------------
# LANDING PAGE
# -----------------------------
# -----------------------------
# LANDING PAGE
# -----------------------------
# -----------------------------
# LANDING PAGE
# -----------------------------
if st.session_state.page == "landing" and not st.session_state.logged_in:

    st.markdown("""
    <div style="text-align:center; margin-top:60px;">
        <h1 style="color:#0a2540; font-size:42px;">
            AI Duplicate Detection Platform
        </h1>
        <p style="color:#5f6b7a; font-size:18px;">
            Detect duplicate questions using advanced semantic AI.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Buttons row
    left, center, right = st.columns([2,2,2])
    with center:
        b1, b2 = st.columns(2)
        with b1:
            if st.button(" Sign Up", use_container_width=True):
                st.session_state.page = "signup"
                st.rerun()
        with b2:
            if st.button(" Login", use_container_width=True):
                st.session_state.page = "login"
                st.rerun()

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Feature section
    st.markdown("### Platform Features")

    f1, f2, f3 = st.columns(3)

    with f1:
        st.markdown("""
        <div class="login-card">
            <h4>⚡ Fast AI Predictions</h4>
            <p>Instant duplicate detection using SBERT embeddings.</p>
        </div>
        """, unsafe_allow_html=True)

    with f2:
        st.markdown("""
        <div class="login-card">
            <h4> Analytics Dashboard</h4>
            <p>Visualize predictions, accuracy, and trends.</p>
        </div>
        """, unsafe_allow_html=True)

    with f3:
        st.markdown("""
        <div class="login-card">
            <h4>🔐 Secure Authentication</h4>
            <p>Password hashing and session-based login.</p>
        </div>
        """, unsafe_allow_html=True)



# -----------------------------
# LOGIN PAGE
# -----------------------------
# -----------------------------
# LOGIN PAGE
# -----------------------------
# -----------------------------
# LOGIN PAGE
# -----------------------------
elif st.session_state.page == "login" and not st.session_state.logged_in:

    st.markdown('<div class="login-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">Login</div>', unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    remember = st.checkbox("Remember me")

    col1, col2 = st.columns(2)

    with col1:
        login_clicked = st.button(" Login", use_container_width=True)

    with col2:
        back_clicked = st.button("⬅ Back", use_container_width=True)

    if login_clicked:
        if username in users and users[username] == hash_password(password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.remember = remember
            st.rerun()
        else:
            st.error("Invalid credentials")

    if back_clicked:
        st.session_state.page = "landing"
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# SIGNUP PAGE
# -----------------------------
# -----------------------------
# SIGNUP PAGE
# -----------------------------
elif st.session_state.page == "signup" and not st.session_state.logged_in:

    st.markdown('<div class="login-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">Create Account</div>', unsafe_allow_html=True)

    new_user = st.text_input("Choose Username")
    new_pass = st.text_input("Choose Password", type="password")

    if new_pass:
        strength, color = password_strength(new_pass)
        st.markdown(
            f"<p style='color:{color};'>Password Strength: {strength}</p>",
            unsafe_allow_html=True
        )

    col1, col2 = st.columns(2)

    with col1:
        signup_clicked = st.button(" Sign Up", use_container_width=True)

    with col2:
        back_clicked = st.button("⬅ Back", use_container_width=True)

    if signup_clicked:
        if new_user in users:
            st.error("Username already exists")
        elif new_user and new_pass:
            users[new_user] = hash_password(new_pass)
            save_users(users)
            st.success("Account created! Please login.")
        else:
            st.warning("Enter username and password")

    if back_clicked:
        st.session_state.page = "landing"
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# MAIN APP (after login)
# -----------------------------
elif st.session_state.logged_in:

    st.sidebar.success(f"Logged in as {st.session_state.username}")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.page = "landing"
        st.rerun()

    st.markdown("""
    <div style="
        background: white;
        padding: 30px;
        border-radius: 16px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.08);
        text-align: center;
        margin-top: 40px;
    ">
        <h2>Welcome to AI Platform</h2>
        <p>Use the sidebar to navigate between prediction, history, and analytics.</p>
    </div>
    """, unsafe_allow_html=True)
