import json
from employee import Employee

EMPLOYEE_FILE = "employees.json"

def save_employees(employees):
    """Saves the list of employees to a JSON file."""
    with open(EMPLOYEE_FILE, "w") as file:
        json.dump(employees, file)

def load_employees():
    """Loads the list of employees from a JSON file."""
    try:
        with open(EMPLOYEE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def add_employee(existing_employees):
    """Adds a new employee to the list."""
    name = input("Enter employee name: ")
    id = input("Enter employee ID: ")
    salary = input("Enter employee salary: ")
    department = input("Enter employee department: ")

    for emp in existing_employees:
        if emp["id"] == id:
            print("Error: An employee with this ID already exists!")
            return None

    return Employee(name, id, salary, department)

def remove_employee(existing_employees):
    """Removes an employee from the list by ID."""
    id = input("Enter the ID of the employee to remove: ")
    for emp in existing_employees:
        if emp["id"] == id:
            existing_employees.remove(emp)
            print(f"Employee with ID {id} has been removed.")
            return existing_employees
    print("Error: Employee with this ID does not exist!")
    return existing_employees
