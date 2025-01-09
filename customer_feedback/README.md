### Customer Feedback System

This project is a simple CRM application designed to record and manage customer feedback. The system includes basic CRM features such as adding customers, recording feedback, viewing feedback, and updating feedback status.

### Key Features

### 1. Add Customer

Collects customer details like name, email, and phone number.

Automatically assigns a unique ID to each customer.

### 2. Add Feedback

Records feedback provided by a specific customer.

Captures additional information such as feedback status (e.g., Pending, Resolved) and feedback date.

### 3. View Feedback

Displays all feedback entries in the database.

Lists feedback ID, customer ID, feedback text, status, and feedback date.

### 4. Update Feedback Status

Allows updating the status of an existing feedback entry.

Supports status changes, such as from "Pending" to "Resolved."

#### Technologies Used

### Python: For scripting and CRUD operations.

### SQLite: As the database to store customer and feedback information.

### VSCode: As the text editor for writing and executing Python scripts.

#### Steps to Set Up and Run the Project

### 1. Set Up the Environment

Install Python:Visit Python's official website to download and install the latest version.

To verify the installation, open a command prompt and type:

python --version

Check SQLite Installation:SQLite comes bundled with Python. To verify, open a command prompt and type:

sqlite3

Install VSCode:Download and install Visual Studio Code.

### 2. Create the Database

Open VSCode and create a new Python script named create_feedback_db.py.

Run the script to create the database file customer_feedback.db with the required tables (customers and feedback).

### 3. Add Customers and Feedback

Create a Python script named add_feedback.py.

Run the script to add customers and their feedback.

Follow the prompts to enter customer details and feedback information.

### 4. View and Update Feedback

Use the provided menu options to view existing feedback.

Update feedback status as required.

### 5. Sample Data

You can manually add sample customer and feedback data using the terminal interface. Alternatively, you may create a script to import sample data from a CSV file.

How It Works

Adding Customers: Users can add new customers by providing their name, email, and phone number.

Recording Feedback: Feedback entries are linked to specific customers using customer IDs.

Viewing Feedback: All recorded feedback can be viewed along with their details.

Updating Status: The status of feedback can be updated to reflect progress (e.g., changing "Pending" to "Resolved").

Learning Outcomes

This project demonstrates:

Basic CRM operations.

CRUD operations using Python and SQLite.

Database interaction and management.

Developing a terminal-based user interface for data entry and updates.

Future Enhancements

Search Functionality: Add the ability to search feedback by customer name or ID.

Data Export: Implement a feature to export feedback data to CSV.

GUI Integration: Develop a graphical user interface for better user experience.

#### Conclusion

This project serves as a hands-on introduction to CRM systems, providing a practical way to learn about feedback management, database operations, and Python scripting. It is ideal for beginners looking to enhance their understanding of basic CRM concepts and database-driven applications.

### Note: Ensure that Python and SQLite are properly installed before running the scripts. Follow the setup steps carefully to avoid errors.
