class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show_details(self):
        print(f"Person: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, emp_id):
        Person.__init__(self, name, age)
        self.employee_id = emp_id
    
    def show_details(self):
        print(f"Employee: {self.name}, Age: {self.age}, ID: {self.employee_id}")

class PartTime(Person):
    def __init__(self, name, age, hours):
        Person.__init__(self, name, age)
        self.working_hours = hours
    
    def show_details(self):
        print(f"Part-Time: {self.name}, Age: {self.age}, Hours: {self.working_hours}")

class Consultant(Employee, PartTime):
    def __init__(self, name, age, emp_id, hours, project):
        Employee.__init__(self, name, age, emp_id)
        PartTime.__init__(self, name, age, hours)
        self.project_name = project
        
    def show_details(self):
        print(f"Consultant: {self.name}, Age: {self.age}, ID: {self.employee_id}, "
              f"Hours: {self.working_hours}, Project: {self.project_name}")
        

p1 = Person("nikhil", 30)
e1 = Employee("sam", 28, "E123")
pt1 = PartTime("Charlie", 22, 25)
c1 = Consultant("james", 35, "C456", 15, "AI Project")

p1.show_details()
e1.show_details()
pt1.show_details()
c1.show_details()
