# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC #  ANALYSIS
# MAGIC **Analytical SQL Queries**

# COMMAND ----------

# QUERY 1: Market performance analysis
print("🔍 SQL QUERY 1: Market Performance Analysis")
print("=" * 40)

query1 = """
SELECT 
    price_category,
    COUNT(*) as number_of_coins,
    ROUND(AVG(price), 2) as average_price,
    ROUND(AVG(daily_change), 2) as avg_daily_change_percent,
    ROUND(SUM(market_cap_billion), 2) as total_market_cap_billions,
    ROUND(AVG(volume), 2) as avg_daily_volume
FROM madsc102_final.crypto_analysis.crypto_markets
GROUP BY price_category
ORDER BY total_market_cap_billions DESC
"""

result1 = spark.sql(query1)
display(result1)

# COMMAND ----------

# QUERY 2: Best and worst performers (fixed)
print("\n🔍 SQL QUERY 2: Best & Worst Performers")
print("=" * 40)

query2 = """
SELECT 
    category,
    name,
    symbol,
    ROUND(price, 2) as current_price,
    ROUND(daily_change, 2) as daily_change_percent,
    ROUND(market_cap_billion, 3) as market_cap_billions
FROM (
    SELECT 
        'TOP GAINERS' as category,
        name,
        symbol,
        price,
        daily_change,
        market_cap_billion,
        ROW_NUMBER() OVER (ORDER BY daily_change DESC) as rn
    FROM madsc102_final.crypto_analysis.crypto_markets
    WHERE daily_change > 0

    UNION ALL

    SELECT 
        'TOP LOSERS' as category,
        name,
        symbol,
        price,
        daily_change,
        market_cap_billion,
        ROW_NUMBER() OVER (ORDER BY daily_change ASC) as rn
    FROM madsc102_final.crypto_analysis.crypto_markets
    WHERE daily_change < 0
)
WHERE rn <= 5
ORDER BY category, daily_change_percent DESC
"""

result2 = spark.sql(query2)
display(result2)