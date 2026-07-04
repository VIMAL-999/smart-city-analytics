import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="NYC Smart City Dashboard", layout="wide")
st.title("🏙️ NYC Smart City Predictive Dashboard")
st.caption("Real data from OpenAQ, NYC DOT, and EIA — predicting pollution and energy demand")

# ---------- Load everything once ----------
master = pd.read_csv("data/processed/master_dataset.csv")
forecast = pd.read_csv("data/processed/energy_forecast.csv", parse_dates=["ds"])
model = joblib.load("pm25_model.pkl")

tab1, tab2, tab3 = st.tabs(["📊 Air Quality Patterns", "⚡ Energy Forecast", "🔮 Pollution Predictor"])

# ---------- TAB 1: Air Quality Patterns ----------
with tab1:
    st.subheader("Pollution levels by hour and day of week")
    day_names = {0: "Mon", 1: "Tue", 2: "Wed", 3: "Thu", 4: "Fri", 5: "Sat", 6: "Sun"}
    master_display = master.copy()
    master_display["day_name"] = master_display["day_of_week"].map(day_names)

    pollutant = st.selectbox("Choose a pollutant", ["pm25", "o3", "no2"])
    fig = px.line(
        master_display.sort_values("hour"),
        x="hour", y=pollutant, color="day_name",
        title=f"{pollutant.upper()} by hour, split by day of week"
    )
    st.plotly_chart(fig, use_container_width=True)

# ---------- TAB 2: Energy Forecast ----------
with tab2:
    st.subheader("48-hour energy demand forecast")

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=forecast["ds"], y=forecast["yhat"], name="Forecast", line=dict(color="blue")))
    fig.add_trace(go.Scatter(x=forecast["ds"], y=forecast["yhat_upper"], name="Upper bound", line=dict(width=0), showlegend=False))
    fig.add_trace(go.Scatter(x=forecast["ds"], y=forecast["yhat_lower"], name="Confidence range", fill="tonexty", line=dict(width=0), fillcolor="rgba(0,0,255,0.1)"))
    fig.update_layout(title="Energy Demand Forecast (MWh)", xaxis_title="Date", yaxis_title="Demand (MWh)")
    st.plotly_chart(fig, use_container_width=True)

    st.caption("Shaded area = Prophet's confidence interval (how uncertain the model is)")

# ---------- TAB 3: Pollution Predictor ----------
with tab3:
    st.subheader("Predict PM2.5 pollution level")
    col1, col2, col3 = st.columns(3)

    with col1:
        hour = st.slider("Hour of day", 0, 23, 12)
    with col2:
        day = st.selectbox("Day of week", options=list(day_names.keys()), format_func=lambda x: day_names[x])
    with col3:
        energy = st.slider("Energy demand (MWh)", 15000, 30000, 20000)

    input_df = pd.DataFrame([[hour, day, energy]], columns=["hour", "day_of_week", "avg_energy_demand"])
    prediction = model.predict(input_df)[0]
    st.metric("Predicted PM2.5", f"{prediction:.2f}")

    if prediction > 12:
        st.warning("This is a relatively high predicted pollution level for this pattern.")
    else:
        st.success("This is within a normal predicted range.")

    st.divider()
    st.subheader("🔄 What-If: Reduce City Activity Level")
    st.caption("Using energy demand as a proxy for overall city activity (traffic data will replace this once enough history is collected)")

    reduction_pct = st.slider("Reduce activity level by (%)", 0, 50, 10)
    adjusted_energy = energy * (1 - reduction_pct / 100)

    baseline_df = pd.DataFrame([[hour, day, energy]], columns=["hour", "day_of_week", "avg_energy_demand"])
    adjusted_df = pd.DataFrame([[hour, day, adjusted_energy]], columns=["hour", "day_of_week", "avg_energy_demand"])

    baseline_pred = model.predict(baseline_df)[0]
    adjusted_pred = model.predict(adjusted_df)[0]
    change = adjusted_pred - baseline_pred

    col_a, col_b, col_c = st.columns(3)
    col_a.metric("Current predicted PM2.5", f"{baseline_pred:.2f}")
    col_b.metric("After reduction", f"{adjusted_pred:.2f}", delta=f"{change:.2f}")
    col_c.metric("Adjusted energy demand", f"{adjusted_energy:.0f} MWh")

    if change < 0:
        st.success(f"Reducing activity by {reduction_pct}% is predicted to lower PM2.5 by {abs(change):.2f}")
    else:
        st.info(f"At this hour/day pattern, reducing activity by {reduction_pct}% shows minimal or no predicted pollution benefit")