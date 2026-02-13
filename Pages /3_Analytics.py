import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# -------------------------------
# Custom Glass Header
# -------------------------------
st.markdown("""
<div style="
    background: linear-gradient(135deg, rgba(0,114,255,0.25), rgba(0,198,255,0.15));
    padding: 25px;
    border-radius: 16px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.15);
    margin-bottom: 25px;
">
    <h2 style="margin:0;">AI Analytics Dashboard</h2>
    <p style="margin:0; opacity:0.8;">
        Real-time insights into model predictions and performance
    </p>
</div>
""", unsafe_allow_html=True)


# -------------------------------
# Check history
# -------------------------------
if "history" in st.session_state and st.session_state.history:

    df = pd.DataFrame(st.session_state.history)
    df["time"] = pd.to_datetime(df["time"])

    # -------------------------------
    # KPI Calculations
    # -------------------------------
    total = len(df)
    dup = len(df[df["result"] == "Duplicate"])
    nondup = len(df[df["result"] == "Not Duplicate"])
    avg_conf = df["confidence"].mean()
    accuracy = df["correct"].mean() * 100 if "correct" in df else 0

    # -------------------------------
    # Custom KPI Cards
    # -------------------------------
    st.markdown("### Key Metrics")

    k1, k2, k3, k4, k5 = st.columns(5)

    def kpi_card(title, value):
        st.markdown(f"""
        <div style="
            background: rgba(255,255,255,0.08);
            padding: 18px;
            border-radius: 14px;
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255,255,255,0.12);
            text-align: center;
        ">
            <div style="font-size:13px; opacity:0.7;">{title}</div>
            <div style="font-size:26px; font-weight:600;">{value}</div>
        </div>
        """, unsafe_allow_html=True)

    with k1:
        kpi_card("Total Predictions", total)
    with k2:
        kpi_card("Duplicates", dup)
    with k3:
        kpi_card("Not Duplicates", nondup)
    with k4:
        kpi_card("Avg Confidence", f"{avg_conf:.1f}%")
    with k5:
        kpi_card("Model Accuracy", f"{accuracy:.1f}%")

    st.markdown("<br>", unsafe_allow_html=True)

    # -------------------------------
    # Row 1: Distribution
    # -------------------------------
    st.markdown("### Prediction Distribution")

    col1, col2 = st.columns(2)

    counts = df["result"].value_counts().reset_index()
    counts.columns = ["Type", "Count"]

    with col1:
        bar = px.bar(
            counts,
            x="Type",
            y="Count",
            color="Type",
            title="Prediction Count",
            text_auto=True
        )
        bar.update_layout(showlegend=False)
        st.plotly_chart(bar, use_container_width=True)

    with col2:
        donut = px.pie(
            counts,
            names="Type",
            values="Count",
            hole=0.55,
            title="Distribution"
        )
        st.plotly_chart(donut, use_container_width=True)

    # -------------------------------
    # Row 2: Time & Accuracy
    # -------------------------------
    st.markdown("### Activity & Performance")

    col3, col4 = st.columns(2)

    with col3:
        df["date"] = df["time"].dt.date
        daily = df.groupby(["date", "result"]).size().reset_index(name="count")

        line = px.line(
            daily,
            x="date",
            y="count",
            color="result",
            markers=True,
            title="Predictions Over Time"
        )
        st.plotly_chart(line, use_container_width=True)

    with col4:
        if "correct" in df:
            df["accuracy_step"] = df["correct"].expanding().mean() * 100

            acc_line = px.line(
                df,
                x="time",
                y="accuracy_step",
                title="Accuracy Trend",
                markers=True
            )
            st.plotly_chart(acc_line, use_container_width=True)
        else:
            st.info("Accuracy data not available.")

    # -------------------------------
    # Row 3: Confidence
    # -------------------------------
    st.markdown("### Confidence Analysis")

    col5, col6 = st.columns(2)

    with col5:
        hist = px.histogram(
            df,
            x="confidence",
            nbins=20,
            title="Confidence Distribution"
        )
        st.plotly_chart(hist, use_container_width=True)

    with col6:
        gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=avg_conf,
            title={'text': "Average Confidence"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "#00c6ff"},
                'steps': [
                    {'range': [0, 50], 'color': "#ff4d4d"},
                    {'range': [50, 75], 'color': "#ffb84d"},
                    {'range': [75, 100], 'color': "#66ff99"}
                ]
            }
        ))
        st.plotly_chart(gauge, use_container_width=True)

    # -------------------------------
    # Row 4: Advanced Insights
    # -------------------------------
    st.markdown("### Advanced Insights")

    col7, col8 = st.columns(2)

    with col7:
        conf_class = df.groupby("result")["confidence"].mean().reset_index()

        conf_bar = px.bar(
            conf_class,
            x="result",
            y="confidence",
            color="result",
            title="Avg Confidence per Class",
            text_auto=".1f"
        )
        st.plotly_chart(conf_bar, use_container_width=True)

    with col8:
        df["hour"] = df["time"].dt.hour
        hourly = df.groupby("hour").size().reset_index(name="count")

        hour_bar = px.bar(
            hourly,
            x="hour",
            y="count",
            title="Predictions by Hour"
        )
        st.plotly_chart(hour_bar, use_container_width=True)

else:
    st.info("No data available yet.")
