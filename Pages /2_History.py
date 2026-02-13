import streamlit as st
import pandas as pd

st.title("Prediction History")

if "history" in st.session_state and st.session_state.history:
    df = pd.DataFrame(st.session_state.history)

    # Convert time column
    df["time"] = pd.to_datetime(df["time"])

    # Filters
    col1, col2 = st.columns(2)
    with col1:
        result_filter = st.selectbox(
            "Filter by Result",
            ["All", "Duplicate", "Not Duplicate"]
        )
    with col2:
        search = st.text_input("Search question text")

    # Apply filters
    filtered_df = df.copy()

    if result_filter != "All":
        filtered_df = filtered_df[filtered_df["result"] == result_filter]

    if search:
        filtered_df = filtered_df[
            filtered_df["question1"].str.contains(search, case=False) |
            filtered_df["question2"].str.contains(search, case=False)
        ]

    # Metrics
    total = len(df)
    dup = len(df[df["result"] == "Duplicate"])
    nondup = len(df[df["result"] == "Not Duplicate"])

    m1, m2, m3 = st.columns(3)
    m1.metric("Total Predictions", total)
    m2.metric("Duplicates", dup)
    m3.metric("Not Duplicates", nondup)

    st.divider()

    # Show table
    st.dataframe(filtered_df.sort_values("time", ascending=False),
                 use_container_width=True)

    # Download option
    csv = filtered_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        "Download History",
        csv,
        "prediction_history.csv",
        "text/csv"
    )

else:
    st.info("No predictions yet.")
