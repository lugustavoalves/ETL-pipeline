from kafka import KafkaConsumer
import json
import os
from hdfs import InsecureClient

# Kafka consumer
topic = "midtermtopic"
brokers = "localhost:9092"
group_id = "maingroup"

consumer = KafkaConsumer(topic, bootstrap_servers=brokers,
                        auto_offset_reset='earliest', enable_auto_commit=False, group_id=group_id)

# HDFS client configuration
hdfs_client = InsecureClient('http://localhost:9870', user='XXXXX')
hdfs_path = '/BigData/midterm/final_json.json'

def save_to_hdfs(data):
    # Check if the file exists, create it if it does not
    if not hdfs_client.status(hdfs_path, strict=False):
        with hdfs_client.write(hdfs_path, encoding='utf-8', overwrite=True) as writer:
            json.dump(data, writer)
            writer.write('\n')
    else:
        with hdfs_client.write(hdfs_path, encoding='utf-8', append=True) as writer:
            json.dump(data, writer)
            writer.write('\n')


for message in consumer:
    article = json.loads(message.value)
    save_to_hdfs(article)
    print(f"Consumed article: {article['title']}")
    consumer.commit()
