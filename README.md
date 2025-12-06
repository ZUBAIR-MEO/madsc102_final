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
- CREATE CATALOG madsc102_final;
- CREATE SCHEMA crypto_analysis;

## 📈 Sample ML Prediction

**Bitcoin Prediction:**
- Current Price: $45,000
- ML Predicted: $47,250 (+5%)
- Signal: BUY 🟢
- Confidence: High

##📱 Dashboard Includes
  1. Market overview metrics
  2. Top gainers/losers
  3. ML trading signals distribution
  4. Price vs prediction comparison
  5. Interactive filters by symbol/price/confidence

##🔄 Automation
  1. Daily data refresh at 9 AM UTC
  2. Automatic ML model retraining
  3. Dashboard auto-update

## 📁 Project Structure

/crypto-analysis/
├── crypto_analysis.ipynb    # Main pipeline
├── ml_models.py            # ML predictions
├── dashboard_queries.sql   # Visualization SQL
└── automation.py          # Daily refresh

##🎯 Business Value
  1. Investors: Data-driven trading decisions
  2. Traders: Real-time market insights
  3. Analysts: Pattern recognition and forecasting
  4. Students: Hands-on big data & ML experience

## 💡 Why It Matters
  1. Democratizes Analytics - Makes complex market data accessible
  2. Reduces Risk - ML-backed insights vs emotional trading
  3. Real-time - Live data for timely decisions
  4. Scalable - Handles 100+ cryptocurrencies efficiently

## 📞 Get Started
  1. Clone this repository
  2. Import notebooks to Databricks
  3. Run the main analysis
  4. Build your dashboard

