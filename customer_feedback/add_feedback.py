import sqlite3

def add_customer(name, email, phone):
    conn = sqlite3.connect('customer_feedback.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO customers (name, email, phone) VALUES (?, ?, ?)",
                   (name, email, phone))
    conn.commit()
    conn.close()
    print("Customer added successfully!")

def add_feedback(customer_id, feedback_text, status, feedback_date):
    conn = sqlite3.connect('customer_feedback.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO feedback (customer_id, feedback_text, status, feedback_date) VALUES (?, ?, ?, ?)",
                   (customer_id, feedback_text, status, feedback_date))
    conn.commit()
    conn.close()
    print("Feedback added successfully!")

def view_feedback():
    conn = sqlite3.connect('customer_feedback.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM feedback")
    feedbacks = cursor.fetchall()
    conn.close()

    if feedbacks:
        for feedback in feedbacks:
            print(f"Feedback ID: {feedback[0]}, Customer ID: {feedback[1]}, Feedback: {feedback[2]}, Status: {feedback[3]}, Date: {feedback[4]}")
    else:
        print("No feedback available.")

def update_feedback_status(feedback_id, new_status):
    conn = sqlite3.connect('customer_feedback.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE feedback SET status = ? WHERE id = ?", (new_status, feedback_id))
    conn.commit()
    conn.close()
    print("Feedback status updated successfully!")




# Example usage:
while True:
    print("1. Add Customer")
    print("2. Add Feedback")
    print("3. View Feedback")
    print("4. Update Feedback Status")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter customer name: ")
        email = input("Enter customer email: ")
        phone = input("Enter customer phone: ")
        add_customer(name, email, phone)
    elif choice == '2':
        customer_id = int(input("Enter customer ID for the feedback: "))
        feedback_text = input("Enter feedback text: ")
        status = input("Enter feedback status (e.g., Pending, Resolved): ")
        feedback_date = input("Enter feedback date (YYYY-MM-DD): ")
        add_feedback(customer_id, feedback_text, status, feedback_date)
    elif choice == '3':
        view_feedback()
    elif choice == '4':
        feedback_id = int(input("Enter feedback ID to update status: "))
        new_status = input("Enter new feedback status (e.g., Pending, Resolved): ")
        update_feedback_status(feedback_id, new_status)
    elif choice == '5':
        break
    else:
        print("Invalid choice! Please enter again.")
