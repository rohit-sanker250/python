class Calculation1:
    def summation(self,a,b):
        return a+b;
class Calculation2:
    def Multiplication(self,a,b):
        return a*b;
class Calculation3(Calculation1,Calculation2):
    def Divide(self,a,b):
        return a/b;
d=Multiplication()
print(d.summation(10,20))