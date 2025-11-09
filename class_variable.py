class demo:
    class_name='focus'
    def setname(self,a):
        self.name=a
    def getname(self):
        print(self.name)
    def setname(self,b):
        self.name=b
    def getname(self):
        print(self.name)
    def f1(self):
        print(demo.class_name)
class1 = demo()
class1.setname("prachi")
class1.getname()
class1.f1()
obj1 = demo()
obj1.setname("prajakta")
obj1.getname()
class1.f1()

# 
class demo:
    x=1
    def __init__(self):
        demo.y =2
    def f1(self):
        demo.z =3
obj = demo()
demo.a=10
print(demo.__dict__)
# 
class demo:
    x=1
    def __init__(self):
        demo.y = 2
        print(demo.y)
    def f1(self):

        demo.z = 3
        print(demo.z)
        print(demo.x)
obj = demo()
obj.f1()
demo.a=10
print(demo.a)
# print(demo.__dict__)
# 
class demo:
    x=1
    def __init__(self,p):
        self.a=p

d = demo(10)
demo.x=100
print(d.__dict__)
print(demo.__dict__)
d1=demo(20)
print(d1.__dict__)
print(demo.__dict__)
# write a python prog to track a object how many time it run
class demo:
    x=0
    def __init__(self):
        demo.x += 1  
d = demo()
d1 = demo()
print(demo.x)
#
class demo:
    def f1(x,self):
       print(self)
d = demo()
d.f1(10)
# 
class demo:
    x=10
    def f1(self):
        self.y=20
d1 = demo()
d1.x=30
d1.y=40
print(d1.x,d1.y)
 
#  
class demo1:
    a=30
    def f1(self):
        self.b=40
        self.c=50
d = demo1()
d.f1()
print(demo1.a,d.b,d.c)
d1 = demo1()
d1.f1()
demo1.a = 100
print(demo1.a,d.b,d.c)