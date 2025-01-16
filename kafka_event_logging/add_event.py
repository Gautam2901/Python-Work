import sqlite3
from datetime import datetime

# connect to SQLite database
conn = sqlite3.connect("events.db")
c = conn.cursor()

# Insert sample events
c.execute('''
INSERT INTO event_logs (event_time, event_description)
VALUES(?, ?)
''', (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "User Logged in"))

c.execute('''
INSERT INTO event_logs (event_time, event_description)
VALUES(?, ?)
''', (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "File uploaded"))

# Added some more events
events = [
    ("2024-12-12 16:00:00", "User signed up"),
    ("2024-12-12 16:10:00", "Admin changed settings"),
    (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "File downloaded"),
]
for event_time, description in events:
    c.execute('''
    INSERT INTO event_logs (event_time, event_description)
    VALUES(?, ?)
    ''', (event_time, description))

conn.commit()
print("Events added successfully")
conn.close()
