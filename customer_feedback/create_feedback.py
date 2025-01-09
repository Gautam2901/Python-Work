import sqlite3

# Connect to the database (it will be created if it doesn't exist)
conn = sqlite3.connect('customer_feedback.db')
cursor = conn.cursor()

# Create table for customer information
cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    phone TEXT
)
''')

# Create table for customer feedback
cursor.execute('''
CREATE TABLE IF NOT EXISTS feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    feedback_text TEXT,
    status TEXT,
    feedback_date TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and tables created successfully!")
