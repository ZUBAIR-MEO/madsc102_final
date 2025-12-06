# 🚀 Cryptocurrency Market Analysis Dashboard

## 📈 Project Overview
A real-time cryptocurrency analytics platform built on Databricks that predicts market movements using machine learning. The system analyzes live market data from CoinGecko API to generate intelligent trading signals and visualize market trends through an interactive dashboard.

## 🎯 Core Hypothesis
**"Market capitalization and trading volume patterns can predict short-term cryptocurrency price movements with sufficient accuracy to generate actionable trading signals."**

## 🔍 What It Does
1. **Real-Time Data Pipeline** - Fetches live cryptocurrency data from CoinGecko API
2. **ML Price Prediction** - Uses Linear Regression to forecast price movements
3. **Trading Signals** - Generates BUY/SELL/HOLD recommendations
4. **Interactive Dashboard** - Visualizes market trends and ML predictions
5. **Daily Automation** - Scheduled updates for fresh insights

## 🛠️ Tech Stack
- **Platform**: Databricks (Delta Lake, Unity Catalog)
- **Data Processing**: PySpark
- **Machine Learning**: PySpark MLlib
- **API**: CoinGecko (Real-time crypto data)
- **Visualization**: Databricks SQL Dashboard

## 📊 Key Features
- **Live Market Data** - Top 100 cryptocurrencies
- **ML Predictions** - Price forecasts with confidence scores
- **Smart Signals** - AI-powered trading recommendations
- **Interactive Charts** - Real-time visualizations
- **Market Insights** - Trend analysis and patterns


## Setup catalog
CREATE CATALOG madsc102_final;
CREATE SCHEMA crypto_analysis;

## 📈 Sample ML Prediction

Bitcoin Prediction:
Current Price: $45,000
ML Predicted: $47,250 (+5%)
Signal: BUY 🟢
Confidence: High

##📱 Dashboard Includes
Market overview metrics
Top gainers/losers
ML trading signals distribution
Price vs prediction comparison
Interactive filters by symbol/price/confidence

##🔄 Automation
Daily data refresh at 9 AM UTC
Automatic ML model retraining
Dashboard auto-update

## 📁 Project Structure

/crypto-analysis/
├── crypto_analysis.ipynb    # Main pipeline
├── ml_models.py            # ML predictions
├── dashboard_queries.sql   # Visualization SQL
└── automation.py          # Daily refresh

##🎯 Business Value
Investors: Data-driven trading decisions
Traders: Real-time market insights
Analysts: Pattern recognition and forecasting
Students: Hands-on big data & ML experience

## 💡 Why It Matters
Democratizes Analytics - Makes complex market data accessible
Reduces Risk - ML-backed insights vs emotional trading
Real-time - Live data for timely decisions
Scalable - Handles 100+ cryptocurrencies efficiently

## 📞 Get Started
Clone this repository
Import notebooks to Databricks
Run the main analysis
Build your dashboard

