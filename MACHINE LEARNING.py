# Databricks notebook source
# MAGIC %md
# MAGIC # MACHINE LEARNING
# MAGIC  **Simple prediction with PySpark MLlib**

# COMMAND ----------

# Ensure we're in the right catalog
spark.sql("USE CATALOG madsc102_final")
spark.sql("USE SCHEMA crypto_analysis")

# Load data
crypto_df = spark.table("crypto_markets")

print("🤖 CREATING SIMPLE ML MODEL...")

# ========== SIMPLE ML: PRICE PREDICTION ==========
from pyspark.sql.functions import col
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.sql.functions import round, when

# 1. Prepare data - keep it simple!
ml_data = crypto_df.select(
    "coin_id",
    "name",
    "symbol",
    "price",
    "market_cap_billion",
    "volume",
    "daily_change"
).filter(
    col("price") > 0  # Remove invalid data
)

print(f"📊 ML Data: {ml_data.count()} records")

# 2. Create features - just 2 features for simplicity
assembler = VectorAssembler(
    inputCols=["market_cap_billion", "volume"],  # Only 2 features
    outputCol="features"
)

# 3. Train simple linear regression
lr = LinearRegression(
    featuresCol="features",
    labelCol="price",  # Predict price
    predictionCol="predicted_price"
)

# 4. Train model (use all data for simplicity)
model = lr.fit(assembler.transform(ml_data))

print(f"✅ Model trained! R² = {model.summary.r2:.3f}")

# 5. Make predictions
predictions = model.transform(assembler.transform(ml_data))

# 6. Add simple trading signal
simple_predictions = predictions.withColumn(
    "trading_signal",
    when(
        col("predicted_price") > col("price") * 1.05,  # Predicted 5% higher
        "BUY"
    ).when(
        col("predicted_price") < col("price") * 0.95,  # Predicted 5% lower
        "SELL"
    ).otherwise(
        "HOLD"
    )
).withColumn(
    "expected_return",
    round((col("predicted_price") - col("price")) / col("price") * 100, 2)
)

# 7. Save to Delta table
simple_predictions.select(
    "coin_id",
    "name",
    "symbol",
    "price",
    "predicted_price",
    "expected_return",
    "trading_signal"
).write.mode("overwrite").format("delta").saveAsTable("simple_ml_predictions")

print("✅ Saved to: simple_ml_predictions")

# 8. Show results
print("\n📈 SIMPLE ML RESULTS:")
simple_predictions.select(
    "name",
    "symbol",
    "price",
    "predicted_price",
    "expected_return",
    "trading_signal"
).orderBy(col("expected_return").desc()).limit(10).show()


# COMMAND ----------

# Simple summary for dashboard
dashboard_ml = spark.sql("""
SELECT 
    trading_signal,
    COUNT(*) as coin_count,
    ROUND(AVG(expected_return), 2) as avg_return,
    ROUND(AVG(price), 2) as avg_price
FROM simple_ml_predictions
GROUP BY trading_signal
ORDER BY coin_count DESC
""")

dashboard_ml.write.mode("overwrite").saveAsTable("dashboard_ml_summary")

print("✅ Dashboard table created: dashboard_ml_summary")
dashboard_ml.show()
