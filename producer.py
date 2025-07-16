from kafka.producer import KafkaProducer
import time
import json
import os
from datetime import datetime

# Kafka producer
topic = "finaltopic"
brokers = "localhost:9092"

producer = KafkaProducer(bootstrap_servers=brokers)

# Read the file initially
filename = "articles.json"
last_modified_time = 0
processed_articles = set()

def read_and_send_articles():
    with open(filename, "r") as f:
        articles = json.load(f)
        for article in articles:
            # Check if the article has already been processed
            if article['title'] in processed_articles:
                continue

            # convert the publishedAt field to a datetime type
            if 'publishedAt' in article:
                article['publishedAt'] = datetime.strptime(article['publishedAt'], "%Y-%m-%dT%H:%M:%SZ").isoformat()
            # ensure the source is a key-value pair
            article['source'] = article['source']['name']
            # remove the urlToImage field if it exists
            if 'urlToImage' in article:
                del article['urlToImage']

            producer.send(topic, json.dumps(article).encode('utf-8'))
            producer.flush()
            print(f"Sent article: {article['title']}")

            # Add the article title to the set of processed articles
            processed_articles.add(article['title'])

# Initial read
if os.path.exists(filename):
    read_and_send_articles()
    last_modified_time = os.path.getmtime(filename)

# Checking for updates every second
while True:
    if os.path.exists(filename):
        current_modified_time = os.path.getmtime(filename)
        if current_modified_time != last_modified_time:
            read_and_send_articles()
            last_modified_time = current_modified_time
    time.sleep(1)
