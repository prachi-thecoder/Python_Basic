class A:
    def f1(self):
        print("base class")
class B(A):
    def f2(self):
        print("derived class")

obj = B()
obj.f1()
obj.f2()
# 

from datetime import datetime
class person:
    def f1(self):
        self.name = "prachi"
        self.date_of_birth = "2006/1/21"
    def calculate_age(self):  
        current_date = datetime.today()
        # print(current_date)
        y,m,d = map(int , self.date_of_birth.split('/'))
        self.date_of_birth =datetime(y,m,d)
        self.age=current_date.year-self.date_of_birth.year
        return  self.age
class voter(person):
    def is_eligible(self):
        if(self.calculate_age() > 18):
            print("it is eligible ")
        else:
            print("it is not eligible")

    def display(self):
        print(self.name)
        print(self.date_of_birth)
        print(self.age)

d1 = voter()
d1.f1()
d1.is_eligible() 
d1.display()  
# 
class base:
    def __init__(self):
        print("base classs constructor")
    def __del__(self):
        print("base destructor")
class derived(base):
    def __init__(self):
        super().__init__()
        print("derived class constructor")
    def __del__(self):
        super().__del__()
        print("derived class destructor")

obj = derived()

# construstor method overriding
class A:
    def f1(self):
        print("base class")
class B(A):
    def f1(self):
        super().f1()
        print("derived class")
obj = B()
obj.f1()
# constructor with parameter 
class A:
    def __init__(self,name):
        self.name = name
        print(f"the name {self.name}")
class B(A):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age
        print(f"the age {self.age}")

obj = B("prachi",19)
