class a:
    def __init__(self,a):
        print(a)
class b(a):
    def __init__(self,a,b):
        print(b)
class C(b):
    def __init__(self,a,b,c):
        a.__init__(a)
        b.__init__(b)
        print(C)

obj = C(1,2,3)