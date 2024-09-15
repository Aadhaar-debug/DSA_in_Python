'''
Inheritance Problem:
You need to create a class Employee to represent a generic employee, with attributes name and salary. The class should have a method 
display_details() that prints the employee’s name and salary.

Next, create two derived classes:

Manager: This class should inherit from Employee and have an additional attribute department. It should override the display_details() 
method to include the department in the output.
Developer: This class should also inherit from Employee and have an additional attribute programming_language. It should override the 
display_details() method to include the programming language in the output.
Tasks:
Define the base class Employee with the necessary attributes and methods.
Define the derived classes Manager and Developer with their additional attributes and overridden methods.
Create instances of Manager and Developer, and call their display_details() method to show all the information.
Bonus Challenge:
Add a method in the Manager class called assign_task() that takes the name of a Developer and a task as input, and prints a message 
assigning the task to the developer.

Let me know how you solve it or if you need hints!
'''

class employee:
    def __init__(self):
        self.name = 'Aadhaar'
        self.salary = 500000
    def display_details(self):
        print(f"Name = {self.name}")
        print(f"Salary = {self.salary}")

class Manager(employee):
    def __init__(self, department , name , salary):
        self.department = department
        self.name = name
        self.salary = salary
    def display_details(self):
        print(f"Name = {self.name}")
        print(f"Salary = {self.salary}")
        print(f"department = {self.department}")

class Developer(employee):
    def __init__(self):
        self.programming_language = 'Python'
        self.name = e.name
        self.salary = e.salary
    def display_details(self):
        print(f"Name = {self.name}")
        print(f"Salary = {self.salary}")
        print(f"programming_language = {self.programming_language}")

e = employee()
e.display_details()

m = Manager('Management', 'Qwerty' , 180000)
m.display_details()

d = Developer()
d.display_details()