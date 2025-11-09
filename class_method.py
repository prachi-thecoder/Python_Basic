class demo:
    x=10
    def f2(self):
        self.a=15
        print(self.a)
    @classmethod
    def f1(self):
        print(self.x) 
    
de = demo()
de.f2()
de.f1()

# 
class demo1:
    def f1(self):
        self.a=15
        print(self.a)

d1 = demo1()
d1.f1()