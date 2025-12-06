# Databricks notebook source
# %% [markdown]
# ## 📡 STEP 1: FETCH REAL DATA FROM API
# **Requirement 4.1: API Data Ingestion**

# %%
# Import libraries
import requests
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Start Spark
spark = SparkSession.builder.appName("CryptoAnalysis").getOrCreate()

# Fetch real cryptocurrency data
print("🔗 Fetching LIVE cryptocurrency data...")

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc", 
    "per_page": 50,
    "page": 1
}

# Make API call
response = requests.get(url, params=params, timeout=30)
crypto_data = response.json()

print(f"✅ SUCCESS! Got {len(crypto_data)} LIVE cryptocurrencies")
print(f"💰 Bitcoin Price: ${crypto_data[0]['current_price']:,.2f}")
print(f"📈 24h Change: {crypto_data[0]['price_change_percentage_24h']:.2f}%")


# COMMAND ----------

# %% [markdown]
# ## 🧹 STEP 2: CLEAN & PREPARE DATA
# **Requirement 4.2: Data Cleaning**

# %%
print("🧼 Cleaning real data...")

# Create clean list
clean_data = []
for coin in crypto_data:
    clean_data.append({
        "coin_id": coin["id"],
        "name": coin["name"],
        "symbol": coin["symbol"].upper(),
        "price": float(coin["current_price"]),
        "market_cap": float(coin["market_cap"]),
        "daily_change": float(coin["price_change_percentage_24h"]),
        "volume": float(coin["total_volume"]),
        "high_24h": float(coin["high_24h"]),
        "low_24h": float(coin["low_24h"])
    })

# Create DataFrame
df = spark.createDataFrame(pd.DataFrame(clean_data))

# Add useful columns
df = df.withColumn("market_cap_billion", round(col("market_cap") / 1000000000, 3))
df = df.withColumn("price_category", 
    when(col("price") > 1000, "High (>$1000)")
    .when(col("price") > 100, "Medium ($100-$1000)")
    .when(col("price") > 10, "Low ($10-$100)")
    .otherwise("Very Low (<$10)")
)

print(f"✅ Cleaned {df.count()} cryptocurrency records")
print("\n📊 Sample Data:")
df.select("name", "symbol", "price", "daily_change").show(5)


# COMMAND ----------

# %% [markdown]
# ## 💾 STEP 3: SAVE TO DELTA TABLES IN CATALOG
# **Requirement 4.3: Store in Delta tables in catalog**

# %%
print("💾 Saving to catalog: madsc102_final.crypto_analysis")

# Use the provided catalog and schema
spark.sql("USE CATALOG madsc102_final")
spark.sql("USE SCHEMA crypto_analysis")

# Save as Delta table
df.write \
    .mode("overwrite") \
    .format("delta") \
    .option("overwriteSchema", "true") \
    .saveAsTable("crypto_markets")

print("✅ Saved as: madsc102_final.crypto_analysis.crypto_markets")

# Verify
crypto_table = spark.table("crypto_markets")
print(f"📊 Verified: {crypto_table.count()} records in table")


# COMMAND ----------

# %% [markdown]
# ## 🔍 STEP 4: EXPLORE DATA
# **Requirement 4.5: Notebook Analysis**

# %%
print("🔍 Exploring cryptocurrency data...")

# 1. Basic statistics
print("\n📈 MARKET OVERVIEW:")
stats = crypto_table.select(
    count("*").alias("Total Coins"),
    avg("price").alias("Average Price"),
    min("price").alias("Lowest Price"), 
    max("price").alias("Highest Price"),
    avg("daily_change").alias("Avg Daily Change")
).collect()[0]

print(f"• Total Coins: {stats['Total Coins']}")
print(f"• Price Range: ${stats['Lowest Price']:,.2f} - ${stats['Highest Price']:,.2f}")
print(f"• Market Mood: {'Bullish 📈' if stats['Avg Daily Change'] > 0 else 'Bearish 📉'}")

# 2. Top 5 cryptocurrencies
print("\n🏆 TOP 5 CRYPTOCURRENCIES:")
crypto_table.orderBy(col("market_cap").desc()) \
    .select("name", "symbol", "price", "daily_change", "market_cap_billion") \
    .limit(5) \
    .show()

# 3. Performance by price category
print("\n💰 PERFORMANCE BY PRICE CATEGORY:")
crypto_table.groupBy("price_category") \
    .agg(
        count("*").alias("Coin Count"),
        avg("daily_change").alias("Avg Daily Change"),
        sum("market_cap_billion").alias("Total Market Cap (B)")
    ) \
    .show()
