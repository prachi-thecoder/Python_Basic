# getter setter method
class student:
    def setname(self,a):
        self.name=a
    def getname(self):
         print(self.name)
    def setage(self,b):
        self.age=b
    def getage(self):
         print(self.age) 
    def setroll(self,c):
        self.roll=c
    def getroll(self):
         print(self.roll)
obj = student()
obj.setname("prachi")
obj.setage(19)
obj.setroll(21)
obj.getname()
obj.getage()
obj.getroll()
print(obj.__dict__)
obj1 = student()
obj1.setname("prajakta")
obj1.getname()
obj1.setage(20)
obj1.getage()
print(obj1.__dict__)