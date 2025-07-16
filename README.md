# ETL Pipeline: Real-time News Article Processing

This project implements an **ETL (Extract, Transform, Load)** pipeline for processing real-time cryptocurrency-related news articles. Built for the **Big Data Integration and Storage (PROG8451)** course, this system demonstrates streaming data processing using **Kafka**, **Spark Structured Streaming**, and **MySQL**.

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
