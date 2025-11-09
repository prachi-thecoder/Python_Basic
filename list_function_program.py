#  write a python prog to a declare a integer list and calculate sum of all elements of list ,find min and max value from the list
l=[1,2,3,4,5,6,6]
print(sum(l))
print(max(l))
print(min(l))

# write a python prog to declare 2 list if both the list are equal then repeat both list 3 time 
# else concate both the list
a=[1,2,3,4]
b=[1,2,3,4]
if(a == b):
    print(a * 3 ,b*3)
else:
    print(a + b)
#write a python prog take no from user and cheack given no is present or not in list
# if it is yes then find sum of all the list element and sort given list in assending order
# else convert given list into decending order

a=int(input("enter a no:"))
b=[1,2,3,4,5,6]
if(a in b):
    print(sum(b))
    print(sorted(b))
else:
    print(sorted(b,reverse=True))

# declare 1 list and form 2nd list from 1 which contain only even no using list compherhsion
# print even no 
a=[1,2,3,4,5]
l1=[i for i in a if i%2==0]
print(l1)

#  prin even index 
l=[1,2,4,5,6,7,8,8]
l1=[]
for i in l:
    if i %2==0:
        l1.append(i)
print(l1)

# write a python prog to take a list from list of word return only thoes with les than 5 char
user=["cat","bat","prachi","prajakta"]
l=[]
for i in user:
    if(len(i)<5):
        l.append(i)
print(l)

# by list compherisinon
l=["pra","ama","prachii"]
l1=[i for i in l if len(i)<5]
print(l1)

# to convert a word in uppercase by list comphereshion
l=["pra","ama","prachii"]
l1=[i.upper() for i in l ]
print(l1)

# to find second largest no from list 
   


# to take a elements of a list from user
d=[]
for i in range(5):
    user=int(input("enter a elements:"))
    d.append(user)
print(d)

# to remove duplicate
b1=[]
b=[]
for i in range(5):
    a=int(input("enter a list:"))
    b.append(a)
print(b)
for i in b:
    if i not in b1:
        b1.append(i)
print(b1)
# to take a value from user and find that value in a list if itis present then replace it with python
# only update first occuerence of an element else print list asitis
b1=[]
for i in range(6):
    a=int(input("enter a list items:"))
    b1.append(a)
print(b1)
b=int(input("enter a element:"))
if b in b1:
    k=b1.index(b)
    b1[k]='python'
    print(b1) 
else:
    print(b1)

#count the no of words where of len>2 and 1st and last charater are same count how many words are 
count=0
l=['aaa','abcd','adb','pqes']
for i in l:
    if(len(i)>2 and i[0] == i[-1]):
        count+=1
print(count)
         
# swap a list 1 and last element
l=[1,2,3,4,5,6]
l[0],l[-1]=l[-1],l[0]
print(l)



