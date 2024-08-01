class PersonalInfo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_personal_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class JobInfo:
    def __init__(self, job_title, salary):
        self.job_title = job_title
        self.salary = salary

    def display_job_info(self):
        print(f"Job Title: {self.job_title}")
        print(f"Salary: ${self.salary}")

class Employee(PersonalInfo, JobInfo):
    def __init__(self, name, age, job_title, salary):
        PersonalInfo.__init__(self, name, age)
        JobInfo.__init__(self, job_title, salary)

# Example usage
emp = Employee("Eve", 30, "Manager", 95000)
emp.display_personal_info()
emp.display_job_info()
