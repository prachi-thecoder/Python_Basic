# function overloading
class focus:
    def __init__(self,*a):
        print(a)
    def f1(self,a=10):
        print(a)

# f=focus(10)
# f1=focus()
# f2=focus(1,2,3)
f = focus()
f.f1(10)
# 
class area:
    def area(self,*p):
        print(sum(p))
f = area()
f.area(10,20,30,40)
# calculate a area of diffrent shape
from math import pi
class area:
    def area(self,a=0,b=0):
        if(a!=0 and b==0):
            print("area of square",a**2)
            print("area of circle",pi*a*a)
        elif(a!=0 and b!=0):
            print("area of rectangle",a*b)
            print("area of triangle",0.5*a*b)

a = area()
a.area(2)
a.area(5,10)
