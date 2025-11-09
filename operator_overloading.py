class focus:
    def d1(self):
        self.x = 10
    def __add__(self,a):
        return self.x+a.x
    def __sub__(self,a):
        return self.x-a.x
    def __mul__(self,a):
        return self.x*a.x
    def __gt__(self,a):
        return self.x>a.x
d= focus()
d.d1()
d2=focus()
d2.d1()
print(d+d2)
print(d-d2)
print(d*d2)
print(d>d2)
# 
class complex_no:
    def __init__(self,a,b):
        self.a =a
        self.b = b
    def __add__(self,p):
        return self.a+p.a,self.b+p.b      
i = complex_no(10,11)  
d = complex_no(10,10)
print(i+d)
#bank account class 3 instace variable account holder name,intial balance ,acount no
# it contain instance method deposite,widral
# you have to create account using operator overloading concept 
# transfer funds using operator overloading compare 2 ac and show the result 
class bank_ac:
    def __init__(self,name,balance,no):
        self.holder_name=name
        self.holder_intial_balance=balance
        self.holder_ac_no=no
    def deposite(self):
        user=int(input("enter a balance u want deposite:"))
        self.holder_intial_balance=self.holder_intial_balance+user
        print(self.holder_intial_balance)
    def widral(self):
        user1=int(input("enter a wdral no:"))
        self.holder_intial_balance=self.holder_intial_balance-user1
        print(self.holder_intial_balance)
    def display(self):
        print(self.holder_name)
        print(self.holder_ac_no)
        print(holder_intial_balance)
        # print("after depself.holder_intial_balance)
    def __add__(self,a):
        return self.holder_name+a.holder_name,str(self.holder_ac_no)[0:3]+str(a.holder_ac_no)[0:2],self.holder_intial_balance+a.holder_intial_balance
    def __sub__(self,q):
        amt=1000
        if(self.holder_intial_balance>q.holder_intial_balance):
            self.holder_intial_balance=self.holder_intial_balance-amt
            q.holder_intial_balance+=amt
            print("transfer amount",amt,"balance ",self.holder_intial_balance)
            print("recived amount",amt,"balance ",q.holder_intial_balance)
        else:
            q.holder_intial_balance=q.holder_intial_balance-amt
            self.holder_intial_balance+=amt
            print("transfer amount",amt,"balance ",q.holder_intial_balance)
            print("recived amount",amt,"balance ",self.holder_intial_balance)
d = bank_ac("prachi",1500,123457)
d.deposite()
d.widral()
d1=bank_ac("prajakta",1000,176989)
d1.deposite()
d1.widral()
print("combine ac :",d+d1)
d-d1
