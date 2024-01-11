class students:
    def __init__(name,adress,phone):
        self.name=name
        self.adress=adress
        self.phone=phone
    def display(self):
        print("student name :",self.name,"student address :",self.adress,"phone number :",self.phone)

p1=students("rohit",525001,"shoranur") 
p1=display()          