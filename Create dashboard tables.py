# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC #📊 Creating tables for dashboard

# COMMAND ----------

# Table 1: Summary statistics (fixed)
summary_df = spark.sql("""
SELECT 'Total Cryptocurrencies' as metric, CAST(COUNT(*) as STRING) as value 
FROM madsc102_final.crypto_analysis.crypto_markets
UNION ALL
SELECT 'Total Market Cap', CONCAT('$', ROUND(SUM(market_cap_billion), 1), 'B') 
FROM madsc102_final.crypto_analysis.crypto_markets
UNION ALL
SELECT 'Average Price', CONCAT('$', ROUND(AVG(price), 2)) 
FROM madsc102_final.crypto_analysis.crypto_markets
UNION ALL
SELECT 'Market Sentiment', 
    CASE 
        WHEN AVG(daily_change) > 5 THEN 'Very Bullish 🚀'
        WHEN AVG(daily_change) > 0 THEN 'Bullish 📈'
        WHEN AVG(daily_change) > -5 THEN 'Neutral ↔️'
        ELSE 'Bearish 📉'
    END
FROM madsc102_final.crypto_analysis.crypto_markets
""")

summary_df.write.mode("overwrite").saveAsTable(
    "madsc102_final.crypto_analysis.dashboard_summary"
)

# COMMAND ----------

from pyspark.sql.functions import col

crypto_table = spark.table(
    "madsc102_final.crypto_analysis.crypto_markets"
)

top_coins = crypto_table.orderBy(
    col("market_cap").desc()
).select(
    "name", "symbol", "price", "daily_change"
).limit(15)

top_coins.write.mode("overwrite").saveAsTable(
    "madsc102_final.crypto_analysis.dashboard_top_coins"
)

# COMMAND ----------

categories = spark.sql("""
SELECT price_category, COUNT(*) as coin_count 
FROM madsc102_final.crypto_analysis.crypto_markets
GROUP BY price_category
""")

categories.write.mode("overwrite").saveAsTable(
    "madsc102_final.crypto_analysis.dashboard_categories"
)

# COMMAND ----------

print("✅ Created 3 dashboard tables:")
print("1. dashboard_summary - Market overview")
print("2. dashboard_top_coins - Top 15 coins")
print("3. dashboard_categories - Price categories")

# COMMAND ----------

print("\n📁 ALL TABLES IN OUR SCHEMA:")
display(
    spark.sql(
        "SHOW TABLES IN madsc102_final.crypto_analysis"
    )
)