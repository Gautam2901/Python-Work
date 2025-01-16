import csv
import sqlite3

conn = sqlite3.connect('crm_database.db')
cursor = conn.cursor()

with open('contacts.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for row in reader:
        cursor.execute("INSERT INTO contacts (name, email, phone, company) VALUES (?, ?, ?, ?)", (row[0], row[1], row[2], row[3]))

conn.commit()
conn.close()

