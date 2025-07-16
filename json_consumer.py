from kafka import KafkaConsumer
import json
import os

# Kafka consumer
topic = "midtermtopic"
brokers = "localhost:9092"
group_id = "maingroup"

consumer = KafkaConsumer(topic, bootstrap_servers=brokers,
                        auto_offset_reset='earliest', enable_auto_commit=False, group_id=group_id)

path_hdfs_file = "final_json.json"

def save_to_hdfs(data):
    # Check if the file exists, create it if it does not
    if not os.path.exists(path_hdfs_file):
        with open(path_hdfs_file, "w") as f:
            f.write(json.dumps(data) + "\n")
    else:
        with open(path_hdfs_file, "a") as f:
            f.write(json.dumps(data) + "\n")

for message in consumer:
    article = json.loads(message.value)
    save_to_hdfs(article)
    print(f"Consumed article: {article['title']}")
    consumer.commit()
