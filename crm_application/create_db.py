import csv
import sqlite3
# Create or connect to a database
conn = sqlite3.connect('crm_database.db')
cursor = conn.cursor()
# Create a table for storing contacts
cursor.execute('''
CREATE TABLE IF NOT EXISTS contacts (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
email TEXT,
phone TEXT,
company TEXT
)
''')
with open('contacts.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for row in reader:
        cursor.execute("INSERT INTO contacts (name, email, phone, company) VALUES (?, ?, ?, ?)", (row[0], row[1], row[2], row[3]))

# Commit the changes and close the connection
conn.commit()
conn.close()