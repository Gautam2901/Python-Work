import sqlite3

# Connection to the database.

conn = sqlite3.connect("events.db")
c = conn.cursor()

# Create table for event logs

c.execute('''
CREATE TABLE IF NOT EXISTS event_logs (
    id INTEGER PRIMARY KEY,
    event_time TEXT,
          event_description TEXT
    )
''')

# Commit and close the connections

conn.commit()
conn.close()