// spark-shell --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.3,mysql:mysql-connector-java:8.0.33

import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._

// Define schema
val schema = StructType(Array(
  StructField("source", StringType, nullable = true),
  StructField("author", StringType, nullable = true),
  StructField("title", StringType, nullable = true),
  StructField("description", StringType, nullable = true),
  StructField("url", StringType),
  StructField("publishedAt", TimestampType),
  StructField("content", StringType, nullable = true)
))

// Read from Kafka
val df = spark
  .readStream
  .format("kafka")
  .option("kafka.bootstrap.servers", "localhost:9092")
  .option("subscribe", "finaltopic")
  .option("startingOffsets", "earliest")
  .load()

// Parse JSON
val parsedDf = df.select(
  from_json(col("value").cast("string"), schema).alias("data")
).select("data.*")

// Start streaming to console
val query = parsedDf
  .writeStream
  .outputMode("append")
  .format("console")
  .start()


val query_mysql = parsedDf.writeStream
  .foreachBatch { (batchDF: org.apache.spark.sql.DataFrame, batchId: Long) =>
    batchDF.write
      .format("jdbc")
      .option("url", "jdbc:mysql://localhost:3306/final")
      .option("dbtable", "articles")
      .option("user", "root")
      .option("password", "XXXXX")
      .mode("append")
      .save()
  }
  .start()
