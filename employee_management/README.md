#### Employee Management System

### This project is a Python-based Employee Management System that allows users to manage employee records such as viewing, adding, and removing employees. The application stores employee information in a JSON file to ensure data persistence.

#### 1. Features
-1. View Employees:

-Displays all current employee details.

-2. Add Employee:

-Add a new employee to the system.

### Validates to prevent duplicate employee IDs.

-3. Remove Employee:

-Remove an employee by their ID.

### Ensures the JSON file is updated accordingly.

-4. Persistent Data Storage:

-Employee data is stored in a JSON file (employees.json).

### File Structure
```EmployeeManagementSystem/
│
├── employees.json       # The JSON file for storing employee data
├── main.py              # Main entry point
├── employee.py          # Employee class definition
└── utils.py             # Utility functions for employee operations```

File Descriptions

main.py:

Handles the main menu and user interaction.

Provides options for viewing, adding, and removing employees.

employee.py:

Contains the Employee class.

Includes methods to display employee details and convert employee data to a dictionary for JSON storage.

utils.py:

Includes utility functions for loading, saving, adding, and removing employees from the JSON file.

Handles file read/write operations and input validations.

employees.json:

Stores employee records in JSON format.

Automatically created when the application runs for the first time if it does not already exist.

Prerequisites

Python 3.7+: Ensure Python is installed on your system.

Basic understanding of Python and JSON.

Setup Instructions

Clone the Repository:

git clone https://github.com/yourusername/EmployeeManagementSystem.git
cd EmployeeManagementSystem

Run the Application:

python main.py

First-Time Run:

If employees.json does not exist, it will be created automatically.

The file will store all employee data in JSON format.

Usage

Launch the Program:

Run main.py.

You will see a menu with the following options:

Menu:
1. View Employees
2. Add Employee
3. Remove Employee
4. Exit

View Employees:

Displays a list of all current employees in the system.

If no employees exist, it will display a message: No employees found!

Add Employee:

Prompts for employee details: name, ID, salary, and department.

Validates the employee ID to ensure it is unique.

Saves the new employee to employees.json.

Remove Employee:

Prompts for the employee ID.

Removes the employee if the ID matches an existing record.

Saves the updated list to employees.json.

Exit:

Saves all changes and exits the program.

Example Workflow

Initial Setup:

On first run, no employees are present in the system.

Add Employees:

Enter employee name: John Doe
Enter employee ID: 101
Enter employee salary: 50000
Enter employee department: HR

Successfully adds the employee.

View Employees:

Current Employees:
- Name: John Doe, ID: 101, Salary: 50000, Department: HR

Remove Employee:

Enter the ID of the employee to remove: 101
Employee with ID 101 has been removed.

Sample JSON File

Here’s an example of how the employees.json file might look:

[
  {
    "name": "Gautam Cholkar",
    "id": "1",
    "salary": 50000,
    "department": "SDE"
  },
  {
    "name": "Jane Smith",
    "id": "2",
    "salary": 60000,
    "department": "Finance"
  }
]

Error Handling

File Not Found:

If employees.json is missing, the program creates a new one automatically.

Duplicate Employee ID:

Prevents adding employees with duplicate IDs.

Invalid ID for Removal:

Displays an error message if the ID is not found during removal.

Future Enhancements

Search Functionality:

Search employees by name or department.

Update Employee Details:

Modify existing employee information.

GUI Integration:

Build a graphical user interface for better usability.