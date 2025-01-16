import sqlite3

def add_contact(name, email, phone, company):
    conn = sqlite3.connect('crm_database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (name, email, phone, company) VALUES (?, ?, ?, ?)", (name, email, phone, company))
    conn.commit()
    conn.close()
    print("Contact added successfully!")

def view_contacts():
    conn = sqlite3.connect('crm_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    conn.close()
    for contact in contacts:
        print(contact)

def add_task(contact_id, task_description, due_date, status):
    conn = sqlite3.connect('crm_database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (contact_id, task_description, due_date, status) VALUES (?, ?, ?, ?)", 
                   (contact_id, task_description, due_date, status))
    conn.commit()
    conn.close()
    print("Task added successfully!")

def view_tasks():
    conn = sqlite3.connect('crm_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    for task in tasks:
        print(task)

# Example usage:
while True:
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Add Task")
    print("4. View Tasks")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        email = input("Enter email: ")
        phone = input("Enter phone number: ")
        company = input("Enter company name: ")
        add_contact(name, email, phone, company)
    elif choice == '2':
        print("Contacts in CRM:")
        view_contacts()
    elif choice == '3':
        contact_id = int(input("Enter contact ID: "))
        task_description = input("Enter task description: ")
        due_date = input("Enter due date (YYYY-MM-DD): ")
        status = input("Enter task status: ")
        add_task(contact_id, task_description, due_date, status)
    elif choice == '4':
        print("Tasks in CRM:")
        view_tasks()
    elif choice == '5':
        break
    else:
        print("Invalid choice! Please enter again.")