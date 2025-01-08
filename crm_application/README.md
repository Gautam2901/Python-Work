# Simple CRM Application with Contact Management

This project is a basic Customer Relationship Management (CRM) system that allows users to manage customer contacts and tasks. It includes setting up a simple database, creating a user interface for contact management, and applying CRM concepts such as lead, contact, account, and task management.

## Project Overview
- **Objective**: Build a simple CRM-based application from scratch.
- **Key Features**:
  - Add and view customer contacts.
  - Manage tasks associated with each contact.
  - Store data using an SQLite database.

## Steps to Complete the Project

### Step 1: Set Up Your Environment
1. **Install Python**:
   - Download and install Python from the official website.
   - Ensure you check the option to "Add Python to PATH" during installation.
   - Verify the installation by running `python --version` in the command prompt.

2. **Install SQLite**:
   - SQLite comes bundled with Python, so no additional installation is needed.
   - Optionally, you can use an external database like MySQL or PostgreSQL.

3. **Set Up a Text Editor or IDE**:
   - Download and install Visual Studio Code (VSCode).
   - Use the terminal in VSCode to run your Python scripts.

### Step 2: Create the CRM Database
1. **Database Setup**:
   - Create a Python script to connect to an SQLite database.
   - Create a table for storing contacts with fields for `name`, `email`, `phone`, and `company`.
2. **Run the Script**:
   - Execute the script in the terminal to generate the database file (`crm_database.db`).

### Step 3: Develop the Contact Management System
1. **Add Contacts**:
   - Implement a function to insert contact details into the database.
   - Allow users to input contact information via a simple menu-driven interface.

2. **View Contacts**:
   - Create a function to retrieve and display all stored contacts from the database.

### Step 4: Extend the CRM with Task Management
1. **Create Tasks Table**:
   - Add a new table to store tasks, linking each task to a contact via `contact_id`.
2. **Add and View Tasks**:
   - Implement functions to add tasks and view them by retrieving data from the tasks table.
3. **Update the Main Menu**:
   - Add options in the main menu to manage tasks.

### Step 5: Import Sample Data
1. **Download Sample Data**:
   - Use a sample CSV file containing customer contact data.
2. **Write a Script to Import Data**:
   - Implement a Python script to read data from the CSV file and insert it into the contacts table.

## Final Step: Run the CRM Application
After completing all the steps:
- Run the main script to launch the application.
- Use the menu to add contacts, view existing contacts, add tasks, and view tasks.

## Future Enhancements
- **Opportunity Tracking**: Add features to track sales opportunities.
- **Reporting**: Implement basic reporting functionalities for contacts and tasks.
- **User Authentication**: Add login functionality to secure the application.

## Summary
This project provides a hands-on way to learn and apply CRM concepts using Python. By completing this project, users will gain experience in:
- Database management with SQLite.
- Building simple command-line interfaces.
- Managing customer data and tasks effectively.

Feel free to enhance the application further by adding more CRM features or integrating it with a web interface!
