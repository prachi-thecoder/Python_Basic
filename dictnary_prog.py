# declare a dictnary with employe name ,employe id ,employee salary and print dictnary
d={"employee_name":'prachi',"employee_id":217686,"employee_salary":5000}
print(d)
# declare a dictnary with coustmer product ,coustmer name,costumer bill and print dictnary
d1={"costumer_name":'prachi',"costumer_product":["wheat","brush"],"costumer_bill":300}
print(d1)
print(d1['costumer_product'])
# declare a dictnary take a key and values from user
d={}
user=int(input("enter no how many key and value u want:"))
for i in range(user):
    k=input("enter a key:")
    v=input("enter a values:")
    d[k]=v
print(d)

# check key exist or not in dictnary or not 
d={}
for i in range(3):
    user=input("enter a key :")
    user2=input("enter a value:")
# value=input("enter a value you want to check:")
    d[user]=user2
key=input("enter a key you want to check:")
print(d.get(key,"not found"))

#write a python prg to take a list of string and return a dict where the keys are string
#  length and the value are list of string of that length 
li=[]
d={}
for i in range(3):
    user=input("enter a list of string:")
    li.append(user)
    print(li)
for i in li:
    l=len(i)
    if l not in d:
        d[l]=[]
    d[l].append(i)
print(d)

# count the frequency of word 
d={}
# count=1
user=input("enter a sentence:")
for i in user.split():
    i=i.lower()
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)
# count the frequency of char
d={}
user=input("enter a scentence:")
for i in user:
    i=i.lower()
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)

# to remove given key value pair from dict
d={}
for i in range(2):
    user=input("enter a key:")
    user1=input("enter a value:")
    d[user]=user1
print(d)
remo=input("enter a key u want to remove:")
print(d.pop(remo))
print(d)

#swap the values 
d={}
for i in range(2):
    user=input("enter a key:")
    user2=input("enter a value:")
    d[user]=user2
print(d)
for i,j in enumerate(d):
    d[j]=j
    j,d[j]=d[j],j
print(d)

#write a python program make a menu card take a key and values from user and ask user to enter a key 
# which value want to see in dictnary
a='MENU CARD'
print(a.center(50,"*"))
d={}
no=int(input("enter a no how many key and values you want:"))
for i in range(no):
    key=input("enter a key:")
    value=input("enter a values:")
    d[key]=value
print(d)
ite=input("enter a key u want to see of value:")
print(d.get(ite))

# create simple program to manage student marks i>add student and their marks
# ii>update marks
# iii>view all student record
# iv>search for a student 
# v>exit
student={}
user=int(input("enter a no you want to add in dictnary:"))
for i in range(user):
    student_name=input("enter a name of student:")
    marks=input("enter a marks:")
    student[student_name]=marks
print(student)
# a=input("enter student name :")
# update_marks=int(input("enter a marks u want to update:"))
# student.update({a,update_marks})
# print(student) 
rec=input("enter a name :")
student.get(rec)
print(student)

# find min and max in values
d={1:'prachi',2:'two'}
b=d.values()
print(min(b))
print(max(b))
# print(b)
# sort according to value
d={1:'prachi',2:'two'}
b=d.values()
print(sorted(b,reverse=True))
