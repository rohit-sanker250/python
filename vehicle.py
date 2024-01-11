class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display(self):
        print("welcome to machine world")

class Car(Vehicle):
     def display(self):
        print("car brand is :",self.brand,"car model is",self.model )

class Motorcycle(Vehicle):
     def display(self):
        print("motorcycle brand is",self.brand,"motorcycle model is",self.model)

c=Car("Benz","TT")
c.display()

m=Motorcycle("KTM","Duke 250")
m.display()
    
                         