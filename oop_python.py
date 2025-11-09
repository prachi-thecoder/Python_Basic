# self is compulsory as parameter in function
class focus:
    def f1(self):
        print("f1")
        print(id(self))
obj=focus()
print(id(obj))
obj.f1()
obj1=focus()
print(id(obj1))
obj1.f1()

# instance variable
class student:
    def info(self):
        self.name="prachi"
        self.roll_no=21
    def display(self):
        print(self.name)
        print(self.roll_no)
obj=student()
obj.info()
obj.display()
obj.marks=78
print(obj.__dict__)
obj1=student()
obj1.info()
obj1.display()
print(obj1.__dict__)
# 
class employee:
    def info(self,a,b,c):
        self.name=a
        self.id=b        
        self.salary=c
    def display(self):
        print(self.name)
        print(self.id)
        print(self.salary)
obj=employee()
obj.info("prachi",19,50000)
obj.display()
print(obj.__dict__)
obj1=employee()
obj1.info("prajakta",19,100000)
obj1.display()
print(obj1.__dict__)
# 
class bank:
    def accept(self,a,b,c):
        self.coustmer_name=a
        self.coustmer_account=b
        self.balance=c
    def deposite(self):
        deposite=int(input("enter a amount u want to deposite:"))
        balance=self.balance+deposite
        print(balance)
    def widraw(self):
        widraw=int(input("enter a amount u want to widraw:"))
        if(self.balance<=widraw):
            print("unsufficent balance")
        else:
            self.balance=self.balance-widraw
            print(self.balance)
    def display(self):
        print(self.coustmer_name)
        print(self.coustmer_account)
        print(self.balance)
obj=bank()
obj.accept("prachi",6698938435,2000)
obj.deposite()
obj.widraw()
obj.display()
print(obj.__dict__)
# 
class rectangle:
    def accept(self):
        self.len=int(input("enter a lenth:"))
        self.wid=int(input("enter a width:"))

    def calculate(self):
        self.area=self.len*self.wid

    def display(self):
        print(self.area)
obj=rectangle()
obj.accept()
obj.calculate()
obj.display()
print(obj.__dict__)
#prod_name,prod_quan,prod_price,dis,total
class order:
    def accept(self,a,b,c):
        self.product_name=a
        self.product_quantity=b
        self.product_price=c
    def calculate_total(self):
        self.total=self.product_quantity*self.product_price
    def calculate_dis(self):
        if(self.total>=2000):
            self.dis=self.total*30/100
            # print(self.dis)
            self.after_dis=self.total-self.dis
            # print(self.after_dis)      
        elif(self.total>=1000):
            self.dis=self.total*15/100
            # print(self.dis)
            self.after_dis=self.total-self.dis
            # print(self.after_dis)      
        elif(self.total>=500):
            self.dis=self.total*5/100
            # print(self.dis)
            self.after_dis=self.total-self.dis
            # print(self.after_dis)      
        else:
            self.dis = 0
            self.after_dis = self.total
            print("there is no discount")
    def display(self):
        print(self.product_name)
        print(self.product_quantity)
        print(self.product_price)
        print(self.dis)
        print(self.after_dis)
obj=order()
obj.accept("book",1,1300)
obj.calculate_total()
obj.calculate_dis()
obj.display()
print(obj.__dict__)