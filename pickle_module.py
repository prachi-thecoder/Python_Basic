# write from binary
import pickle
data =[1,2,3,4,5,56]
with open('data.bin','wb')as f:
    pickle.dump(data,f)
# reading from binary
with open('data.bin','rb')as f:
    d = pickle.load(f)
    print(d)
# 
import pickle
d={'one':1,'two':2}
with open('mhaske.bin','wb+')as f:
    k=pickle.dump(d,f)
    # print(k)
    f.seek(0)
    m=pickle.load(f)
    print(m)

# 
import pickle
l=[1,2,3,4,5]
li=[]
for i in range(5):
    user=input("enter a element:")
    li.append(user)
    # print(li)
with open('element.bin','wb+')as f:
    pickle.dump(l,f)
    # f.seek(0)
    pickle.dump(li,f)
    f.seek(0)
    m=pickle.load(f)
    print(m)
    n=pickle.load(f)
    print(n)
# 
# write a name and roll name from user in dictnary and write and read
import pickle
d={}
for i in range(3):
    s=input("enter a name :")
    m=input("enter a roll_no:")
    d[s]=m
# print(d)
with open("re.bin",'wb+')as f:
    pickle.dump(d,f)
    f.seek(0)
    print(pickle.load(f))
# 
import pickle
def search_student(name_to_search):
    with open("re.bin",'rb')as f:
        f.seek(0)
        student_data = pickle.load(f)
        if student_data['prachi']== name_to_search:
            print("roll number:",student_data[21])
        else:
            print("name not found")
name=input("enter a name to search:")
search_student(name) 
# 
import pickle
li=[]
k=[]
user1=input("enter a list item_code element:")
li.append(user1)
for i in range(3):
    user=int(input("enter a amount:"))
    k.append(user)
li.append(k)
# print(li)
with open("sales.bin",'wb+')as f:
    p=pickle.dump(li,f)
    f.seek(0)
    o=pickle.load(f)
    print(o)
    print(sum(li[1]))
# 
import pickle
l=[]
l1=[]
l2=[]
l3=[]
count = 0
for i in range(3):
    user=int(input("enter a addmission code:"))
    l1.append(user)
    user1=input("enter a name:")
    l2.append(user1)
    user2=int(input("enter a marks"))
    l3.append(user2)
l.append(l1)
l.append(l2)
l.append(l3)
# print(l)
with open("student.bin",'wb+')as f:
    t=pickle.dump(l,f)
    k=f.seek(0)
    r=pickle.load(f)
    # print(r)
    for i in (r[2]):
        if(i>=75):
            print(i)
            count+=1
            print(count)
        else:
            print("try again")


import pickle
l=[]
l1=[]
l2=[]
l3=[]
count = 0
for i in range(3):
    user=int(input("enter a addmission code:"))
    l1.append(user)
    user1=input("enter a name:")
    l2.append(user1)
    user2=int(input("enter a marks"))
    l3.append(user2)
l.append(l1)
l.append(l2)
l.append(l3)
# print(l)
with open("student.bin",'wb+')as f:
    t=pickle.dump(l,f)
    k=f.seek(0)
    r=pickle.load(f)
    # print(r)
    for j in range(len(r)):
        for i in (r[2]):
            if(i>=75): 
                print(r[j][j])
                count+=1
            else:
                print("try again")
print(count)