class college:
    def f1():
        print("hello")

college.f1()
d = college()
d.f1()    #we can not call directly by using obj name because it is static method
# 
class college:
    @staticmethod
    def f1():
        print("hello")
    def f2(self):
        print('f2')

college.f1()
d = college()
d.f2() 
# college.f2()
class imp:
# a = 10  #public
# __b=21   #private
#    _c=11  #protected
    def f1(self):
        print("public")
    def __f2(self):
        print("private")
    def _f3(self):
        print("protected")
# print(imp.a)
# print(imp._c)
# print(imp.__b)
d = imp()
d.f1()
d._f3()
d.__f2()
# eg
# class employee:
    # create employee by using constructor 
    # get 1 empid and validate empid using static mathod
    # empid start with emp and len 6
    # create emp obj
    #instance variable emp name emp id emp position and department
# instance method promotion
# if position isfresher then junier if junier then senior and senior then head give position will midlevel
# transfer_branch if branch is pune then transfer mumbai if mumbai then banglore if banglore then us 
# display() 
class employee:
    