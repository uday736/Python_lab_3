class Employee:
    def __init__(self, name, date_of_join, designation, salary):
        self.name = name
        self.date_of_join = date_of_join
        self.designation = designation
        self.salary = salary
    
    def display(self):
        print(f"Employee Name: {self.name}")
        print(f"Date of Joining: {self.date_of_join}")
        print(f"Designation: {self.designation}")
        print(f"Salary: ${self.salary}")

# Example usage
emp = Employee("John Doe", "2024-01-15", "Software Engineer", 80000)
emp.display()
