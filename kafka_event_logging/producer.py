from kafka import KafkaProducer
import sqlite3
import time
from datetime import datetime

# Kafka Producer setup

producer = KafkaProducer(bootstrap_servers = "localhost:9092")

# Fetch event Logs from SQlite

conn = sqlite3.connect("events.db")
c = conn.cursor()
c.execute("SELECT event_description FROM event_logs")
event_logs = c.fetchall()
conn.close()

# Send each event log to kafka

for event in event_logs:
    event_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    message = f"Event Time: {event_time} | Event Description: {event[0]}"
    producer.send('event_topic', value=message.encode("utf-8"))
    print(f"Sent: {message}")
    time.sleep(1) # Simulate delay between events

# Closing the producer
producer.close()