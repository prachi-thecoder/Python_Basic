import cal 
print(cal.add(1,2))

# giving a nickname to file
# import cal as a
# print(a.sub(5,3))

# when u have to execute only selected function use this
# from cal import mul
# print(mul(2,3))

a=11
b=2
c=22
# all function we can access by using *
from cal import *
print(mul(2,3))
print(add(2,3))
print(sub(3,2))
print(div(2,10))
print(a,b,c) 
