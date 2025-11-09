# eg
# take a element from user and add in set
s=set()
for i in range(5):
    a=int(input("enter a element:"))
    s.add(a)
print(s)
# to take a value from user and delete given value from set
s={1,2,3,4,5,6,6}
a=int(input("enter a no u want to delete:"))
s.remove(a)
print(s)
# to take element of set from user and convert given set into list if given element present in set
a=set()
for i in range(6):
    user=int(input('enter a element:'))
    a.add(user)
    print(a)
value=int(input("enter a no u want to see:"))
if(value in a):
    print(list(a))
else:
    print(a)
# to take itreable object 1 string 2 list 3 tuple from user and add all this in set as a element
s=set()
li=[]
tu=[]
str_user=input("enter a string:")
user=int(input("enter a elements u wnat:"))
for i in range(user):
    user_1=int(input("enter a elements:"))
    tu.append(user_1)
user1=int(input("enter a elemenst of tuple u want:"))
for i in range(user1):
    user_11=int(input('enter a elements:'))
    li.append(user_11)
print(str_user)
print(set(tuple(li)))
print(tu)
s.update(tuple(str_user))
s.update(tuple(li))
s.update(tuple(tu))
print(s)

#uncommon element
s1=set()
s2=set()
print("enter a elment of set1")
for i in range(4):
    a=int(input("enter a element:"))
    s1.add(a)
print("enter a elment of set2")
for i in range(4):
    b=int(input("enter a elemnt:"))
    s2.add(b)
print(s1)
print(s2)
print(s1.isdisjoint(s2))

# remove common element and print s1
s1={1,2,3,4,5}
s2={4,5,6,7,8}
for i in s1.intersection(s2):
        s1.remove(i)
print(s1)

#to take element for 2 set from user and check 1 set is subset of another set
s1=set()
s2=set()
print("element of 1 set")
for i in range(5):
    a=int(input('enter a element of 1 set:'))
    s1.add(a)
for i in range(5):
    b=int(input("enter a element of 2 set:"))
    s2.add(b)
if(s1.issubset(s2)):
    print("yes it is subset of s1")
else:
    print("no")

# find second largest no
s={1,2,3,4,5}
t=(sorted(s,reverse=True))
print(t)
print("it is second largest no:",t[1])

# 
