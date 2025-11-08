# declare a tupple and unpack given tuple into sevral variable print addition of all variable 
a=(1,2,3,4,5,6,7)
t1,t2,t3,t4,t5,t6,t7 = a
print(a)
print(sum(a))

#to get 4th element from last elent of tuple
t=(1,2,3,4,5,6,7,7)
print(t[-4])

#calculate product of all element of tuple
product=1
p=(1,2,3,4,5,6)
for i in p:
    product*=i
print(product)

# comman element add in other tuple
t1=(1,2,3,4,5,7)
t2=(1,2,3,5,7,8)
t=(i for i in t2 if i in t1)
print(tuple(list(t))) 
 

#convert tupple of integer into tuple of string
a=(1,2,3,4,5)
t=( str(i) for i in a )
print(list(t))

# to count no of even and odd elements in tupple
a=(1,2,3,4,5,6,7,8)
sum=0
odd=0
for i in a:
    if(i%2==0):
        sum=sum+i
    elif(i%2!=0):
        odd=odd+i
print("the sum of even no is :",sum)
print("the sum of odd no is :",odd) 



# check if all element in tuple are same or not 
t=(1,2,1,1)
if all(i==t[0] for i in t):
    print("all the elemest are same")
else:
    print("all element are not same")

# to take elements of a tuple from user and unpack the tuple
k=[]
for i in range(5):
    user=int(input("enter a element:"))
    k.append(user)
print(tuple(k))
t=tuple(k)
a,b,c,d,e = t
print(f"a={a},b={b},c={c},d={d},e={e}")

# take a element of nested list from user
l=[]
user1=int(input("enter a how many rows you want:"))
for i in range(user1):
    l1=[]
    user2=int(input("enter a how many element u want in nested :"))
    for i in range(user2):
        b=int(input("enter a how many element:"))
        
        l1.append(b)
    l.append(l1)
print(l)

#take a element of nested list from user and ask user wwhat they want list or tuple
p='y'
l=[] 
user1=int(input("enter a how many rows you want:"))
for i in range(user1):
    l1=[]
    user2=int(input("enter a how many element u want in nested :"))
    p=input("enter you want tuple:")
    if(p=='y' or p=="Y"):
        for i in range(user2):
            b=int(input("enter a elements:"))
            l1.append(b)
        l.append(tuple(l1))
        print(l)
    elif(p=='n' or p=='N'):    
        user2=int(input("enter a how many element u want in nested :"))
        for i in range(user2):
            b=int(input("enter a element:"))
            l1.append(b)
        l.append(l1)
        print(l)
        
