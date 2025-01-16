import sqlite3

conn = sqlite3.connect('crm_database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    contact_id INTEGER,
    task_description TEXT,
    due_date TEXT,
    status TEXT,
    FOREIGN KEY (contact_id) REFERENCES contacts (id)
)
''')

conn.commit()
conn.close()
