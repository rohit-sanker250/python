class Bank:
  def getroi(self):
    return 10
class SBI(Bank):
    def getroi(self):
        return 7
        
class ICICI(Bank):
    def getroi(self):
        return 8
b1 = Bank()
b2 = SBI()
b3 = ICICI()
print("Bank Rate of intrest:",b1.getroi())
print("SBI Rat of intrest:",b2.getroi())
print("ICICI Rate of intrest:",b3.getroi())                