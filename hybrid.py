# class A:
#     pass
# class B:
#     pass
# class C:
#     pass
# class X(A,B):
#     pass
# class Y(B,C):
#     pass
# class P(X,Y):
#     pass
# mini project
class person:
    def __init__(self,name,age,mobile):
        self.name = name
        self.age = age
        self.mobile = mobile
class traveldetail:
    def __init__(self,mode):
        self.mode = mode
class tourist(person,traveldetail):
    def display(self):
        print("tourist name is :",self.name)
        print("tourist age is:",self.age)
        print("tourist mobile no is :",self.mobile)
        print("tourist mode is :",self.mode)
class tourist_managment(tourist):
    def __init__(self,name,age,mobile,mode):
        person.__init__(self,a,b,c)
        traveldetail.__init__(self,d)
    def vaild_name(self):
        if(self.name.isalpha()):
            return True
        
        return False
    def valid_age(self):
        if(self.age>=60 and self.age<=99):
            return True
        
        return False
       
    def valid_no(self):

        if(self.mobile.isdigit() and len(self.mobile)==10 ):
          return True
        
        return False
    def valid_mode(self):
        if(self.mode.lower()=='airway' or self.mode.lower()=='roadway'):
              return True
        
        return False
        
    def genrate_id(self):
        p = self.name[0:2]
        m = self.mobile[0:2]
        t = self.mode[0:2]
        print("tourist id genrated successfully:",p.upper()+str(self.age)+m+t.upper())

a = input("enter a name:")
b = int(input("enter a age:"))
c = input("enetr a no:")
d = input("enter a mode(rodeway/airway):")
def main():
 

    obj = tourist_managment(a,b,c,d)
    obj.display()

    if not(obj.vaild_name()):
        print("the name is not valid")
        return
    if not(obj.valid_age()):
        print("the age is  notvalid")
        return

    if not(obj.valid_no()):
        print("the mobile no is  notvalid")
        return
    if not(obj.valid_mode()):
        print("the travel mode is not valid")
        return
    obj.genrate_id()

main()


