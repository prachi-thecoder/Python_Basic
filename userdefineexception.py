class negativenumberexception(Exception):
    pass
def checknumber(number):
    if(number<0):
        raise negativenumberexception(f"error{number} is not positve no")
    return f"{number} is a positve no"

try:
    num=int(input("enter a no:"))
    result = checknumber(num)
    print(result)
except negativenumberexception as e:
    print(e)
except ValueError:
    print(f"{number}enter a valid no")
# 
class negativenumberexception(Exception):
    pass
def f1(username,password):
    username="admin"
    password="admin123"
    if(user2!=username or getpass!= password):
        raise negativenumberexception(f"{username} and {password} is not correct")
    print("your username is ",username)
    print("your password is",password)
    print('your login successful')

try:
    user2=input("enter a username:")
    getpass=input("enter password:")
    result = f1(user2,getpass)
    
except negativenumberexception as e:
    print(e)
# 
class invalidevehincledetails(Exception):
    pass
class vehincle:
    def regestrationid(self,idd):
        if(len(idd)!=7 and idd[0:3]!='VR'):
            raise invalidevehincledetails(f"{idd} is incorrect prefix")
        if(idd[2:3]!='-'):
            raise invalidevehincledetails(f"{idd} - is missing ")
        if(idd[3:]!=idd.isdigit()):
            raise invalidevehincledetails(f"{idd} non numeric character")
        if(len(idd)<7):
            raise invalidevehincledetails(f"{idd} is to short")
obj = vehincle()
try:
    user = input("enter a id:")
    obj.regestrationid(user)
except invalidevehincledetails as e:
    print(e)
    
