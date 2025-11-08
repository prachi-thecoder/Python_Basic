class p:
    def __init__(self,a):
     print(b)
class q:
    def __init__(self,a,b):

     print(a)
class r(p,q):
    def __init__(self,a,b,c):
     p.__init__(self,a)
     q.__init__(self,b)
     print(c)

a=input("enter a value:")
b=input("enter a value:")
c=input("enter a value:")
r1=r(a,b,c)