# ETL Pipeline: Real-time News Article Processing

This project implements an **ETL (Extract, Transform, Load)** pipeline for processing real-time cryptocurrency-related news articles. Built for the **Big Data Integration and Storage (PROG8451)** course, this system demonstrates streaming data processing using **Kafka**, **Spark Structured Streaming**, and **MySQL**.

---

## 📌 Overview

The pipeline:

- **Extracts** JSON-formatted news articles via an API
- **Transforms** data using Spark (schema enforcement, timestamp conversion, etc.)
- **Loads** clean records into a MySQL database for querying

---

## 🔧 Technologies Used

- **Kafka** – Distributed messaging system for real-time data
- **Spark Structured Streaming** – Data transformation and stream processing
- **Python** – API interaction and Kafka producer
- **MySQL** – Final data storage for analytics
- **Scala** – Used for Spark transformations

---

## 🧩 Pipeline Architecture

```mermaid
graph LR
    A[Python Producer] --> B[Kafka (finaltopic)]
    B --> C[Spark Structured Streaming]
    C --> D[MySQL (final.articles)]
```

| Component              | Role                                                                 |
|------------------------|----------------------------------------------------------------------|
| `source_data.py`       | Extracts articles from NewsAPI and saves to `articles.json`          |
| `producer.py`          | Monitors `articles.json`, transforms data, and streams to Kafka      |
| `Kafka (finaltopic)`   | Message queue for real-time article delivery                         |
| `Spark (Scala)`        | Transforms messages and writes structured data to MySQL              |
| `MySQL`                | Stores cleaned and structured news articles                          |

---

## 🚀 Pipeline Stages

### 1. Data Extraction (Python)
- **Script**: `source_data.py`
- Connects to NewsAPI and fetches news articles with the keywords:
  `bitcoin`, `cryptocurrency`, `crypto`, `BTC`, `btc`
- Saves raw data to a local file: `articles.json`

📷 ![articles.json Output](images/articles_json.png)

---

### 2. Kafka Producer
- **Script**: `producer.py`
- Monitors the `articles.json` file for changes
- Performs the following:
  - Removes `urlToImage`
  - Converts `publishedAt` to datetime
  - Converts the `source` field into a key-value format
- Streams the cleaned JSON to the Kafka topic `finaltopic`

📷 ![Producer Output](images/producer_output.png)

---

### 3. Data Transformation (Spark Structured Streaming)
- **Language**: Scala
- Spark reads from the Kafka topic, applies schema and transformations:
  - Enforces types like `StringType` and `TimestampType`
  - Handles nullable fields like `author` and `description`

📷 ![Spark Console Output](images/spark_console.png)

---

### 4. Data Loading (MySQL)
- **Sink**: MySQL database
- Final structured records are written to `final.articles` table
- Example SQL Query to validate:

```sql
SELECT * FROM articles LIMIT 5;
```

📷 ![MySQL Data Output](images/mysql_output.png)

---

## 📅 Project Info

- **Course**: PROG8451 - Big Data Integration and Storage  
- **Semester**: Winter 2025  
- **Section**: 2  
- **Instructor**: Prof. Shanti Couvrette  
- **Author**: Lucas Gustavo Alves  
- **Date**: April 20, 2025  

---

## 📁 Folder Structure

```
/project-folder
│
├── images/
│   ├── articles_json.png
│   ├── producer_output.png
│   ├── spark_console.png
│   └── mysql_output.png
│
├── source_data.py
├── producer.py
├── spark_code.scala
├── sql_schema.sql
└── README.md
```

---

## 📬 Contact

For any questions or feedback, feel free to reach out via GitHub Issues or contact the project author.

---
