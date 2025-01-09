Customer Feedback System

Project Overview

The Customer Feedback System is a simple CRM (Customer Relationship Management) application designed to collect, store, and manage customer feedback. It demonstrates fundamental CRM concepts, including customer management, feedback collection, and status tracking. The project uses Python for application logic and SQLite as the database.

Features:

Add Customer Information:

Users can add new customers by providing basic details such as name, email, and phone number.

Collect Customer Feedback:

Feedback can be recorded for a specific customer, along with a status (e.g., Pending or Resolved) and feedback date.

View All Feedback:

Users can view a list of all customer feedback, displaying key details such as feedback ID, customer ID, feedback text, status, and date.

Update Feedback Status:

The status of a feedback entry can be updated (e.g., from Pending to Resolved).

Technologies Used:

Python: Primary language for building the application.

SQLite: Lightweight relational database for storing customer and feedback data.

Visual Studio Code: Code editor for writing and running Python scripts.

Steps to Set Up and Run the Project

1. Set Up Your Environment

Install Python:

Download and install the latest version of Python from the official website.

Verify the installation by running python --version in the terminal.

SQLite Installation:

SQLite is included with Python, so no separate installation is required.

You can verify by typing sqlite3 in the terminal.

Install a Text Editor:

Download and install Visual Studio Code or use any preferred text editor.

2. Create the Database

Create a Python script to set up the SQLite database.

This script will create two tables:

customers: To store customer details.

feedback: To store feedback provided by customers, linked to the customers table via a foreign key.

3. Add Customers and Feedback

Create a Python script to add customer information.

The script should allow users to input customer details and store them in the database.

Users can also add feedback for existing customers by providing customer ID, feedback text, status, and feedback date.

4. View and Update Feedback

Implement functionality to view all feedback.

Add an option to update the status of any feedback entry.

Display feedback details in a user-friendly format.

5. Running the Application

Run the main script in the terminal.

Follow the prompts to:

Add new customers.

Record feedback.

View all feedback entries.

Update feedback status.

Exit the application when done.

Sample Data

Users can manually add sample customers and feedback using the terminal prompts.

Optionally, a script can be created to import sample data from a CSV file.

Learning Outcomes

This project provides hands-on experience with:

Python programming: Building command-line applications using Python.

Database interactions: Using SQLite for creating databases and performing CRUD (Create, Read, Update, Delete) operations.

CRM concepts: Understanding the basics of customer relationship management, including data collection, feedback management, and status tracking.

Terminal operations: Running Python scripts and interacting with the application via the terminal.

Future Enhancements

User Authentication:

Implement a login system to restrict access to authorized users.

Search Functionality:

Add the ability to search for feedback by customer name or feedback status.

Export Data:

Allow users to export feedback data to a CSV file.

GUI Version:

Create a graphical user interface (GUI) for a more user-friendly experience.

Conclusion

The Customer Feedback System is a beginner-friendly project that introduces the basics of CRM systems, database management, and Python scripting. It serves as an excellent starting point for developers looking to build more advanced CRM applications in the future.

Thank you for using this system! Feel free to contribute or suggest improvements.
