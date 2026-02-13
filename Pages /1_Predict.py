import streamlit as st
import helper
import datetime

st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.title("🤖 Duplicate Question Detection")
st.write("AI-powered semantic similarity engine.")
st.markdown('</div>', unsafe_allow_html=True)

# Input fields
q1 = st.text_input("Enter Question 1")
q2 = st.text_input("Enter Question 2")

# Predict button
if st.button("Predict"):
    if q1 and q2:
        features = helper.create_features(q1, q2)
        pred = helper.model.predict(features)[0]
        prob = helper.model.predict_proba(features)[0][1]

        result = "Duplicate" if pred else "Not Duplicate"

        if result == "Duplicate":
            st.success("Duplicate Questions")
        else:
            st.error("Not Duplicate")

        # Store history
        # Store history
        if "history" not in st.session_state:
            st.session_state.history = []

        # For demo accuracy tracking
        # (You can later replace this with real labels)
        import random

        actual = random.choice(["Duplicate", "Not Duplicate"])

        correct = (actual == result)

        st.session_state.history.append({
            "question1": q1,
            "question2": q2,
            "result": result,
            "actual": actual,
            "correct": correct,
            "confidence": round(prob * 100, 2),
            "time": datetime.datetime.now()
        })


    else:
        st.warning("Please enter both questions.")
