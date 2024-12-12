from kafka import KafkaConsumer
import sqlite3

# Consumer setup

consumer = KafkaConsumer("event_topic", bootstrap_servers = 'localhost:9092')

#Connect to SQLite DB

conn = sqlite3.connect("events.db")
c = conn.cursor()

# Consume events and store them in the DB

for message in consumer:
    event_data = message.value.decode("utf-8")
    event_time = event_data.split(" | ")[0].split(":")[1]

    event_description = event_data.split(" | ")[0].split(":")[1]

    # Insert event into the database
    c.execute('''
    INSERT INTO event_logs (event_time, event_description)
    VALUES (?, ?)
    ''', (event_time, event_description))
    conn.commit()

    print(f"Stored Event: {event_data}")

# Close the connection (this line will not get reached unless the consumer stops.)

conn.close()


