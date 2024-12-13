from utils import load_employees, save_employees, add_employee, remove_employee

def main():
    employees = load_employees()
    while True:
        print("\nMenu:")
        print("1. View Employees")
        print("2. Add Employee")
        print("3. Remove Employee")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            if employees:
                print("\nCurrent Employees:")
                for emp in employees:
                    print(f"- Name: {emp['name']}, ID: {emp['id']}, Salary: {emp['salary']}, Department: {emp['department']}")
            else:
                print("\nNo employees found!")
        elif choice == "2":
            new_employee = add_employee(employees)
            if new_employee:
                employees.append(new_employee.to_dict())
                save_employees(employees)
                print("\nEmployee added successfully!")
        elif choice == "3":
            employees = remove_employee(employees)
            save_employees(employees)
        elif choice == "4":
            print("\nExiting the Employee Management System. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()
