from abc import ABC,abstractmethod
class focus(ABC):
    @abstractmethod
    def f1(self):
        pass
# 
class demo(focus):
    def f1(self):
        print("pass")  
d = demo()
d.f1()


# eg payment gateway
from abc import ABC,abstractmethod
class payment_gateway(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
    @abstractmethod 
    def refund(self,amount):
        # self.reamount = amount
        pass

class cradit(payment_gateway): 
    def pay(self,amount):
        self.amount = amount
        print("your amount is pay using credit card:",self.amount)
   
    def refund(self,amount):
        self.reamount = amount
        print("your amount is refund using credit card:",self.reamount)

class upi(payment_gateway):
    def pay(self,amount):
        print("your amount is pay using upi:",amount)
    def refund(self,reamount):
        print("ypur amount is refund using upi:",reamount)
d = upi()
d.pay(200)
d.refund(100)

h = cradit()
h.pay(500)
h.refund(66)
