<div align="center">

# 🏙️ NYC Smart City Predictive Analytics

### Machine Learning for Air Quality & Energy Demand Forecasting

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)](https://streamlit.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?logo=scikit-learn)](https://scikit-learn.org/)
[![Prophet](https://img.shields.io/badge/Prophet-Time%20Series-green)](https://facebook.github.io/prophet/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

**An end-to-end machine learning platform that analyzes New York City's air quality and energy demand using public real-world datasets.**

[🚀 Live Demo](https://smart-city-analytics-jexzhpr9k7vb97morgl7app.streamlit.app)

</div>

---

## 📊 Project Overview

NYC Smart City Predictive Analytics combines **air quality, energy demand, and traffic data** to explore how city activity relates to pollution and electricity consumption.

The project uses machine learning and time-series forecasting to:

- Predict **PM2.5 pollution levels**
- Forecast **energy demand 48 hours ahead**
- Analyze pollution patterns by **hour and day of week**
- Simulate **what-if city activity scenarios**
- Collect live traffic data for future model improvements

---

## 🎯 What This Project Does

### 🌫️ PM2.5 Prediction

A machine learning model predicts PM2.5 pollution levels using:

- Hour of day
- Day of week
- Energy demand

Two models were evaluated:

| Model | Purpose | Metric |
|---|---|---:|
| Random Forest | PM2.5 Prediction | **MAE ≈ 2.5** |
| Linear Regression | Baseline | Higher MAE |

Random Forest was selected based on the model comparison.

---

### ⚡ Energy Demand Forecasting

The project uses **Prophet time-series forecasting** to predict electricity demand for the next:

**48 hours**

This helps visualize expected demand patterns and provides a foundation for future smart-city forecasting applications.

---

### 🔮 What-If Pollution Simulator

The dashboard includes an interactive simulator that allows users to explore scenarios involving reduced city activity.

The simulator estimates how changes in activity-related energy demand could affect predicted PM2.5 levels.

> The current simulator uses energy demand as a proxy for city activity because live traffic data has not yet been integrated into the trained prediction model.

---

## 📈 Key Finding

### Day of Week is the strongest predictor

Feature importance from the Random Forest model:

| Feature | Importance |
|---|---:|
| **Day of Week** | **42%** |
| Energy Demand | **37%** |
| Hour of Day | **21%** |

This suggests that **weekly activity patterns** have a stronger relationship with predicted pollution levels than the time of day alone within this dataset.

---

## 🏆 Model Performance

| Model | Task | Result |
|---|---|---|
| Random Forest | PM2.5 Prediction | **MAE ≈ 2.5** |
| Linear Regression | Baseline Comparison | Higher MAE |
| Prophet | Energy Forecasting | **48-hour horizon** |

---

## 🗃️ Data Sources

The project combines data from multiple public sources.

### 🌫️ Air Quality

**OpenAQ**

Provides pollutant measurements including:

- PM2.5
- O₃
- NO₂
- Other pollutants

[OpenAQ](https://openaq.org)

---

### 🚦 Traffic

**NYC DOT Real-Time Traffic Speeds**

Live road-segment speed data is collected hourly through an automated process.

[NYC Open Data](https://data.cityofnewyork.us)

---

### ⚡ Energy

**U.S. Energy Information Administration**

Hourly electricity demand data for New York State.

[EIA Open Data](https://www.eia.gov/opendata/)

---

## 🔄 Project Workflow

```text
Public APIs
     ↓
Data Collection
     ↓
Data Cleaning & Processing
     ↓
Feature Engineering
     ↓
Model Training
     ↓
Model Evaluation
     ↓
Predictions & Forecasts
     ↓
Interactive Streamlit Dashboard
