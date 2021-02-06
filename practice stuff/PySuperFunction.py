class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age



class Employee(Person):
    def __init__(self, name, age, email):
        super().__init__(name, age)
        self.email = email



emp = Employee("Codeloop", 25, "codeloop@gmail.com")
print(emp.name)
print(emp.age)
print(emp.email)

#https://codeloop.org/python-class-inheritance-python-tutorial/