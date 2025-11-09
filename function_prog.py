# that accepts a string and count the no of upper and lower case letter
lcount=0
count=0
def f1(user):
    for i in user:
        if(i.isupper()):
            global lcount
            lcount=lcount+1
            # print(lcount)
        elif(i.islower()):
            global count
            count=count+1
            #  print(count)
user=input("enter a string")            
f1(user)
print(lcount)
print(count)
# which accept list having even no of element and swap the elemnet at adjasent position
li=[]
def adjasent_position(li):
    for i in li:
        li[i],li[i+1] = li[i+1],li[i]
    return li

for i in range(6):
    user=int(input("enter a element:"))
    li.append(user)
if(max(li)% 2 != 0):
    print("enter a last element even")
adjasent_position(li)
print(li)             

# that accept a no and the check wether it is perfect no or not
user=int(input("enter a no :"))
if(user %  )