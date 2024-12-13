class Employee:
    def __init__(self, name, id, salary, department):
        self.name = name
        self.id = id
        self.salary = salary
        self.department = department

    def display_employee(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.department}")

    def to_dict(self):
        return {
            "name": self.name,
            "id": self.id,
            "salary": self.salary,
            "department": self.department
        }
