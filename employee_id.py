class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class det(Person):
    def display(self,empid):
        self.empid=empid
        print("employee id is :",self.empid,"employee name is",self.empid)

p2=det("rohit",24)
p2.display(201)