<div align="center">

# 🏙️ NYC Smart City Predictive Analytics

### Machine Learning for Air Quality & Energy Demand Forecasting

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?logo=scikitlearn)
![Prophet](https://img.shields.io/badge/Prophet-Time%20Series-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

**An end-to-end machine learning project that analyzes New York City's air quality and energy demand using real-world public datasets.**

[🚀 Live Demo](https://smart-city-analytics-jexzhpr9k7vb97morgl7app.streamlit.app)

</div>

---

## 📊 What is NYC Smart City Predictive Analytics?

NYC Smart City Predictive Analytics is an end-to-end machine learning project designed to analyze relationships between **air quality, energy demand, and city activity** in New York City.

The project combines real-world public datasets from:

- OpenAQ
- NYC DOT
- U.S. Energy Information Administration (EIA)

It uses machine learning and time-series forecasting to predict pollution levels, forecast energy demand, and explore potential changes through an interactive what-if simulator.

### The platform can:

- Predict **PM2.5 pollution levels**
- Forecast **NYC energy demand 48 hours ahead**
- Analyze pollution patterns by **hour of day and day of week**
- Compare different machine learning models
- Simulate reduced city activity scenarios
- Continuously collect live traffic data for future model improvements

---

## 🔍 Project Overview

The project focuses on two major predictive tasks:

### 🌫️ PM2.5 Pollution Prediction

A machine learning model predicts PM2.5 pollution levels using:

- Hour of day
- Day of week
- Energy demand

Two models were trained and compared:

- Linear Regression
- Random Forest

The Random Forest model achieved an approximate **MAE of 2.5** and was selected for the dashboard.

### ⚡ Energy Demand Forecasting

The project uses **Prophet time-series forecasting** to forecast electricity demand for the next:

**48 hours**

### 🔮 What-If Pollution Simulator

The Streamlit dashboard includes a what-if simulator that allows users to explore how reducing city activity could affect predicted PM2.5 levels.

The current simulator uses **energy demand as a proxy for city activity**, because live traffic data is not yet integrated into the trained pollution model.

---

# 📈 Benchmark & Model Performance

## PM2.5 Prediction

| Model | Purpose | Metric | Result |
|---|---|---|---:|
| Random Forest | PM2.5 Prediction | MAE | **≈ 2.5** |
| Linear Regression | Baseline Comparison | MAE | Higher than Random Forest |

Random Forest was selected after comparing its performance against the Linear Regression baseline.

## Energy Forecasting

| Model | Purpose | Forecast Horizon |
|---|---|---:|
| Prophet | Energy Demand Forecasting | **48 Hours** |

---

# 🧠 Machine Learning Pipeline

The complete machine learning pipeline consists of the following stages:

```text
┌─────────────────────────────┐
│       Public Data APIs      │
│ OpenAQ | NYC DOT | EIA      │
└──────────────┬──────────────┘
               ↓
┌─────────────────────────────┐
│       Data Collection       │
│ Air Quality | Traffic |     │
│ Energy Demand               │
└──────────────┬──────────────┘
               ↓
┌─────────────────────────────┐
│      Data Engineering       │
│ Cleaning | Missing Values   │
│ Time Alignment | Merging    │
└──────────────┬──────────────┘
               ↓
┌─────────────────────────────┐
│     Feature Engineering     │
│ Hour | Day of Week | Energy │
│ Demand                      │
└──────────────┬──────────────┘
               ↓
       ┌───────┴────────┐
       ↓                ↓
┌──────────────┐  ┌──────────────┐
│ PM2.5 Model  │  │ Energy Model │
│              │  │              │
│ Linear       │  │ Prophet      │
│ Regression   │  │ Forecasting  │
│      ↓       │  │      ↓       │
│ Random       │  │ 48-Hour      │
│ Forest       │  │ Forecast     │
└──────┬───────┘  └──────┬───────┘
       ↓                 ↓
       └────────┬────────┘
                ↓
┌─────────────────────────────┐
│    Streamlit Dashboard      │
│ Analytics | Forecast |      │
│ Prediction | What-If        │
└─────────────────────────────┘
