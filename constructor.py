# default constructor
class demo:
    def __init__(self):
        print("constructor")
    def f1(self):
        print("f1")
obj = demo()
obj.f1()
# parametar constructor
class demo:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def f1(self):
        print(self.a,self.b)
obj = demo(10,20)
obj.f1()  
obj.x=21
print(obj.__dict__)      
obj1 = demo("prachi","mhaske")
obj1.f1()
print(obj1.__dict__)
# constructor overloading is not supported in python
# class demo:
#     def __init__(self):
#         print("default")
#     def __init__(self,a,b):
#         print("parameter")
# obj = demo()
# obj1 = demo(1,2)

# eg of parameter constructor display information for 2 employee
class employee:
    def __init__(self,a,b,c,d):
        self.employee_name=a
        self.employee_salary=b
        self.employee_mobile=c
        self.employee_position=d
    def display(self):
        print(self.employee_name)
        print(self.employee_salary)
        print(self.employee_mobile)
        print(self.employee_position)

obj = employee("prachi",600000,8687466983,"developer")
obj.display()
obj1 = employee("prajakta",788999,7878749,"hr")
obj1.display()
print(obj.__dict__) 
print(obj1.__dict__)
