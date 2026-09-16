<div align="center">

# 🏙️ NYC Smart City Predictive Analytics

### Machine Learning for Air Quality & Energy Demand Forecasting

<p>
  <img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/scikit--learn-Machine%20Learning-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" />
  <img src="https://img.shields.io/badge/Prophet-Time%20Series-00A67E?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Plotly-Visualization-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" />
</p>

<p>
  <strong>An end-to-end machine learning project for analyzing NYC air quality,<br>
  predicting PM2.5 pollution, and forecasting energy demand using real-world public data.</strong>
</p>

<p>
  <a href="https://smart-city-analytics-jexzhpr9k7vb97morgl7app.streamlit.app">
    <img src="https://img.shields.io/badge/🚀%20Live%20Dashboard-Open%20App-2ea44f?style=for-the-badge" />
  </a>
</p>

</div>

---

## 📌 Project at a Glance

<table>
<tr>
<td align="center"><strong>3</strong><br>Public Data Sources</td>
<td align="center"><strong>2</strong><br>Predictive Tasks</td>
<td align="center"><strong>48h</strong><br>Energy Forecast</td>
<td align="center"><strong>≈ 2.5</strong><br>PM2.5 MAE</td>
<td align="center"><strong>3</strong><br>Dashboard Tabs</td>
</tr>
</table>

---

# 🌆 What is NYC Smart City Predictive Analytics?

**NYC Smart City Predictive Analytics** is an end-to-end machine learning project that combines public datasets from **OpenAQ, NYC DOT, and the U.S. Energy Information Administration (EIA)** to study air quality and energy-demand patterns in New York City.

The project demonstrates a complete data science workflow:

```text
Public APIs
    ↓
Data Collection
    ↓
Data Cleaning
    ↓
Feature Engineering
    ↓
Machine Learning
    ↓
Model Evaluation
    ↓
Forecasting
    ↓
Interactive Dashboard

The platform currently focuses on two predictive tasks:

🌫️ PM2.5 pollution prediction
⚡ 48-hour energy demand forecasting

It also includes an interactive what-if simulator for exploring potential pollution changes under reduced city-activity scenarios.

## 💡 Why This Project?

Modern cities generate enormous amounts of environmental, transportation, and energy data.

The challenge is not simply collecting this data, but turning it into useful analytical insights.

This project explores how multiple public data sources can be combined into a single machine-learning workflow to answer questions such as:

How does pollution vary across different times and days?
Which features contribute most to PM2.5 predictions?
Can electricity demand be forecast 48 hours into the future?
How could changes in city activity affect predicted pollution?
How can continuously collected traffic data be incorporated into future models?

The goal is to demonstrate a practical smart-city analytics pipeline, rather than a standalone machine-learning model.

## 🎯 Core Capabilities
🌫️ PM2.5 Prediction

Predicts PM2.5 pollution levels using:

Hour of day
Day of week
Energy demand

Models evaluated:

Linear Regression
Random Forest
⚡ Energy Demand Forecasting

Uses Prophet time-series forecasting to predict electricity demand:

## 📊 Benchmark

The PM2.5 prediction task compares a traditional statistical baseline with a tree-based machine-learning model.

Metric	          Linear Regression	        Random Forest
Model Type	          Linear	                 Ensemble
Task	              PM2.5 Prediction	      PM2.5 Prediction
MAE	                    Higher	                ≈ 2.5
Selected Model          	—	                       ✓

The Random Forest model was selected based on the comparison performed during model development.

Forecast horizon: 48 hours

🔮 What-If Pollution Simulator

Allows users to experiment with reduced city-activity scenarios and observe the corresponding predicted PM2.5 level.

The current simulator uses energy demand as a proxy for city activity.

🚦 Live Traffic Data Collection

NYC traffic-speed data is collected hourly through an automated background process.

The traffic dataset is currently being accumulated for future model improvements and is not yet included in the trained PM2.5 prediction model.

## 🧠 Machine Learning Pipeline

The project follows a complete machine-learning pipeline from raw public data to interactive predictions.

┌──────────────────────────────────────┐
│           PUBLIC DATA SOURCES        │
│                                      │
│   OpenAQ  │  NYC DOT  │  EIA         │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│          DATA COLLECTION              │
│                                      │
│ Air Quality │ Traffic │ Energy       │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│          DATA ENGINEERING             │
│                                      │
│ Cleaning │ Missing Values │ Time      │
│ Alignment │ Aggregation │ Merging     │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│         FEATURE ENGINEERING          │
│                                      │
│ Hour of Day │ Day of Week            │
│ Energy Demand                         │
└──────────────────┬───────────────────┘
                   │
          ┌────────┴────────┐
          ▼                 ▼
┌──────────────────┐ ┌──────────────────┐
│ PM2.5 Prediction │ │ Energy Forecast  │
│                  │ │                  │
│ Linear Regression│ │     Prophet      │
│        ↓         │ │        ↓         │
│ Random Forest    │ │   48-Hour        │
│                  │ │   Forecast       │
└────────┬─────────┘ └────────┬─────────┘
         │                    │
         └─────────┬──────────┘
                   ▼
┌──────────────────────────────────────┐
│        STREAMLIT DASHBOARD           │
│                                      │
│ Analytics │ Forecast │ Prediction    │
│           │          │ What-If       │
└──────────────────────────────────────┘


## 🔄 Project Workflow
1. Data Collection

The project collects real-world data from multiple public APIs.

Air Quality

OpenAQ provides pollutant measurements including:

PM2.5
O₃
NO₂
Other available pollutants
Traffic

NYC DOT provides real-time road-segment traffic-speed data.

Energy

The EIA API provides hourly electricity-demand data for New York State.

2. Data Engineering

Raw data from different sources cannot simply be thrown into a dataframe and declared a smart city. Humanity has tried worse.

The datasets are processed to make them usable for modeling.

Processing includes:

Cleaning raw API responses
Handling missing values
Processing timestamps
Extracting hour-of-day information
Extracting day-of-week information
Aligning inconsistent time ranges
Aggregating observations
Merging datasets

Because the datasets have different periods of availability, some relationships are aligned using hour-of-day and day-of-week patterns rather than exact date matching.

3. Feature Engineering

The current PM2.5 prediction model uses:

Hour of Day
     +
Day of Week
     +
Energy Demand
     ↓
PM2.5 Prediction

These features allow the model to learn recurring temporal and energy-related patterns.

4. Model Training

Two models were evaluated for PM2.5 prediction.

Linear Regression

Used as the baseline model.

Random Forest

Used as the primary machine-learning model.

The models were compared using Mean Absolute Error (MAE).

Random Forest achieved an approximate MAE of 2.5.

5. Energy Forecasting

Historical electricity-demand data is modeled using Prophet.

Historical Energy Demand
          ↓
     Time-Series Data
          ↓
        Prophet
          ↓
    48-Hour Forecast
6. Dashboard Integration

The trained models are integrated into an interactive Streamlit dashboard.

The application provides:

-Historical air-quality analysis
-Energy demand forecasting
-PM2.5 prediction
-What-if scenario analysis

## 📈 Model Performance
PM2.5 Prediction

Model	                     Purpose	       Metric	            Result
Random Forest	        PM2.5 Prediction	    MAE	              ≈ 2.5
Linear Regression	   Baseline Comparison	  MAE	        Higher than
                                                            Random Forest
Energy Forecasting
Model              Purpose	                    Forecast Horizon
Prophet	    Energy Demand Forecasting	              48 Hours

## 🔍 Key Finding
Day of Week has the highest feature importance

The Random Forest model produced the following feature-importance distribution:

Feature	                        Importance
Day of Week	                        42%
Energy Demand                     	37%
Hour of Day	                        21%

Interpretation
Within this trained model and dataset:

Day of Week → 42%

had the highest feature importance, followed by:

Energy Demand → 37%

and:

Hour of Day → 21%

This indicates that weekly activity patterns contributed strongly to the model's PM2.5 predictions.

Important: Feature importance describes the behavior of the trained model. It does not establish that day of week directly causes pollution changes.

## 🗃️ Data Sources

🌫️ OpenAQ

Purpose: Air-quality measurements
Data includes:

PM2.5
O₃
NO₂
Other pollutants

Source: https://openaq.org

🚦 NYC Open Data / NYC DOT

Purpose: Real-time traffic speeds
Provides road-segment speed measurements that are collected hourly for future integration into the prediction system.

Source: https://data.cityofnewyork.us

⚡ U.S. Energy Information Administration

Purpose: Electricity demand
Provides hourly electricity-demand data for New York State.

Source: https://www.eia.gov/opendata/

## 🖥️ Interactive Dashboard

The project contains a 3-tab Streamlit application.

🌫️ 1. Air Quality Analytics

Explore historical air-quality patterns and understand how pollution varies across different temporal patterns.

⚡ 2. Energy Demand Forecast

View the predicted energy demand for the next 48 hours.

🔮 3. Pollution Prediction & What-If Simulator

Generate PM2.5 predictions and experiment with reduced city-activity scenarios.

## 🛠️ Technology Stack
<table> <tr> <th>Category</th> <th>Technology</th> <th>Purpose</th> </tr> <tr> <td><strong>Programming</strong></td> <td>Python 3.11</td> <td>Core development</td> </tr> <tr> <td><strong>Data Processing</strong></td> <td>pandas</td> <td>Cleaning and transformation</td> </tr> <tr> <td><strong>Machine Learning</strong></td> <td>scikit-learn</td> <td>Model training and evaluation</td> </tr> <tr> <td><strong>Prediction Model</strong></td> <td>Random Forest</td> <td>PM2.5 prediction</td> </tr> <tr> <td><strong>Baseline Model</strong></td> <td>Linear Regression</td> <td>Model comparison</td> </tr> <tr> <td><strong>Time-Series</strong></td> <td>Prophet</td> <td>Energy-demand forecasting</td> </tr> <tr> <td><strong>Dashboard</strong></td> <td>Streamlit</td> <td>Interactive web application</td> </tr> <tr> <td><strong>Visualization</strong></td> <td>Plotly</td> <td>Interactive charts</td> </tr> <tr> <td><strong>Air Quality</strong></td> <td>OpenAQ API</td> <td>Pollution measurements</td> </tr> <tr> <td><strong>Traffic</strong></td> <td>NYC DOT</td> <td>Traffic-speed data</td> </tr> <tr> <td><strong>Energy</strong></td> <td>EIA API</td> <td>Electricity-demand data</td> </tr> </table>

## 📁 Project Structure
smart-city-analytics/
│
├── app.py
│
├── data/
│   └── processed datasets
│
├── images/
│   ├── workflow.png
│   ├── Air Quality Pattern.png
│   ├── Energy Forecast.png
│   └── Pollution Predictor.png
│
├── fetch_air_quality.py
├── fetch_energy.py
├── fetch_traffic.py
├── clean_and_merge.py
├── train_model.py
├── forecast_energy.py
│
├── requirements.txt
├── README.md
└── LICENSE

##  📚 Project Files
File	                                   Description
app.py	                           Streamlit dashboard
fetch_air_quality.py	          Collects OpenAQ air-quality data
fetch_energy.py	                 Collects EIA energy-demand data
fetch_traffic.py	               Collects NYC traffic-speed data
clean_and_merge.py	               Cleans and combines datasets
train_model.py	                 Trains and evaluates PM2.5 models
forecast_energy.py	             Generates energy-demand forecasts
requirements.txt	                      Python dependencies
images/	                           README and dashboard visuals

## 🚀 Getting Started
Prerequisites

Before running the project locally, install:

Python 3.11 or compatible version
Git
Internet connection for public API access

You can verify Python with: 
python --version

🚀 Installation
1. Clone the Repository
git clone https://github.com/VIMAL-999/smart-city-analytics.git
2. Navigate to the Project
cd smart-city-analytics
3. Install Dependencies
pip install -r requirements.txt

▶️ Run the Application

Start the Streamlit dashboard:

streamlit run app.py

The application will then open in your browser.

🌐 Live Demo
<div align="center">
🚀 Explore the Interactive Dashboard

Open NYC Smart City Predictive Analytics →

</div>

⚠️ Known Limitations
🚦 Traffic Data Not Yet Integrated Into the Model

Live NYC traffic data is currently being collected hourly.

However, it is not yet included as a feature in the trained PM2.5 prediction model.

The data is being collected for future model improvements.

🌫️ Air Quality Data Availability

Air-quality observations cover different periods depending on monitoring-station availability.

The available historical observations span approximately:

2016–2023

Station uptime and data availability vary across locations and periods.

🕐 Time Alignment

The datasets have different:

Date ranges
Sampling periods
Availability
Sensor coverage

Therefore, some data relationships are aligned using hour-of-day and day-of-week patterns rather than exact date-level matching.

🔮 What-If Simulator

The current simulator uses:

Energy demand as a proxy for city activity

Direct traffic-based activity modeling has not yet been integrated into the trained prediction model.

📊 Limited Prediction Features

The current PM2.5 prediction model uses a relatively small feature set:

Hour of day
Day of week
Energy demand

Additional environmental and meteorological variables could improve future versions.

🔮 Future Development

The project is designed to evolve into a more complete smart-city analytics platform.

🚦 01. Live Traffic Integration

Integrate collected traffic-speed data directly into the PM2.5 prediction pipeline.

Potential features include:

Average traffic speed
Traffic intensity
Road-segment activity
Temporal traffic patterns
🌦️ 02. Weather Integration

Add weather variables that may provide additional predictive information:

Temperature
Humidity
Wind speed
Atmospheric pressure
Precipitation
🔄 03. Automated Model Retraining

Develop an automated pipeline capable of:

Collect New Data
       ↓
Validate Data
       ↓
Clean & Transform
       ↓
Feature Engineering
       ↓
Retrain Model
       ↓
Evaluate Model
       ↓
Deploy Updated Model
🐳 04. Docker Deployment

Containerize the application using Docker to improve:

Reproducibility
Deployment
Environment management
Portability
🌫️ 05. Multi-Pollutant Prediction

Extend the prediction system beyond PM2.5 to include:

NO₂
O₃
CO
PM10
📍 06. Location-Based Predictions

Future versions could provide more granular predictions at:

Monitoring-station level
Neighborhood level
Borough level

instead of relying primarily on city-wide patterns.

🤖 07. Automated ML Pipeline

A future production architecture could include:

Data Sources
     ↓
Data Ingestion
     ↓
Data Validation
     ↓
Feature Engineering
     ↓
Model Training
     ↓
Model Evaluation
     ↓
Model Registry
     ↓
Deployment
     ↓
Monitoring
     ↓
Automated Retraining

📌 Key Takeaways
<div align="center">
Metric / Component	Result
🤖 PM2.5 Model	Random Forest
📉 PM2.5 MAE	≈ 2.5
⚡ Energy Forecast	48 Hours
🗓️ Strongest Feature	Day of Week
📊 Day-of-Week Importance	42%
⚡ Energy Demand Importance	37%
🕐 Hour-of-Day Importance	21%
🌫️ Air Quality Source	OpenAQ
🚦 Traffic Source	NYC DOT
⚡ Energy Source	EIA
🖥️ Dashboard	Streamlit
📊 Visualization	Plotly
</div>

📚 Documentation
Core Project Components
📊 Data Collection — API-based collection from OpenAQ, NYC DOT, and EIA
🧹 Data Engineering — Cleaning, transformation, alignment, and merging
🤖 Machine Learning — Random Forest and Linear Regression
📈 Forecasting — Prophet-based 48-hour energy forecast
🔮 What-If Analysis — Interactive pollution scenario simulation
🖥️ Dashboard — Streamlit-based visualization and analytics
🚦 Traffic Pipeline — Automated collection for future model development

🤝 Contributing

Contributions are welcome.

If you would like to improve the project:

Fork the repository
Create a new feature branch
Make your changes
Test the changes locally
Commit your changes
Open a Pull Request

📄 License

This project is licensed under the MIT License.

See the LICENSE file for details.
