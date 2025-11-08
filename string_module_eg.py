# write a program that genrate random character

import string
import random
# print(random.choice(string.ascii_letters))

# print(random.choices(string.ascii_letters,k=8))

# wap to genrate password
a=" "
for i in range(4):
    a=a+random.choice(string.ascii_letters)+random.choice(string.digits)+random.choice(string.punctuation)  
print(a)

#wap to select a random element from set ,list, dic value

import string
import random
a=set()
p=[]
c={}
for i in range(5):
    k=input("enter a set element:")
    a.add(k)
print(a)
for i in range(5):
    l=input("enter a list element:")
    p.append(l)
print(p)
for i in range(5):
    d=input("enter a key:")
    val=input("enter a value:")
    c[d]=val
print(c)   
print(random.choice(list(a)))
print(random.choice(p))
print(random.choice(list(c.values())) )