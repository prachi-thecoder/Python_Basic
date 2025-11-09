# s="pop"
# if(s[::-1]==s):
#     print("yes")
# else:
#     print("no")


# l=[]
# for i in range(7):
#     user=int(input("enter item:"))
#     l.append(user)
# print(l)
# for i in range(l):
#     if(i℅2==0):
#        print(i)

# l=[1,2,4,2,3]
# l.sort()
# print(l[-2])

# l1=[]
# l=["abc","xyz","abcd","pq"]
# for i in l:
#     if(len(i)>2):
#         l1.append(i.upper())
# print(l1)

# l1=[]
# l=[1,10,30,4,100,4]
# for i in l:
#     if(i not in l1):
#         l1.append(i)
# print(l1)

# prod=1
# l=(1,2,3,4,7)
# for i in l:
#     prod=prod*i
# print(prod)

# s1=set((1,2,3,4))
# s2=set((2,3,9,8))
# print(s1.intersection(s2))

# l=[1,2,3,4,8]
# l1=[i*2 for i in l]     
# print(l1)

# user=[1,2,3,4,9,8]
# for i in range(0,len(user),2):
#     user[i],user[i+1]=user[i+1],user[i]
# print(user)
# # 
# l=[11,21,3,19]
# l.sort()
# a=len(l)-1
# for i in range(l[0],l[a]):
#     if i not in l:
#         print(i)
# # find missing
# def missing(l):
#     l.sort()
#     a=len(l)-1
#     for i in range(l[0],l[a]):
#         if i not in l:
#             print(i)
#     print(l[a]+1) 

# l=[1,2,3,4,7]
# print(missing(l))   

# # string function
# v=0
# p=0
# # c="abidef"
# d="aeiouAEIOU"
# user=input("enter a character:")
# for i in user.lower():
#     if(i in d):
#         # print(i)
#         v=v+1
#     else:
#         p=p+1
# if(p==v):
#     print("they are equal")
# else:
#     print("not")
# # 
# user=input("enter password:")
# sp="@#$&*-"
# # for i in user:
# if(len(user)>=8):
#     upper=any(i.isupper() for i in user)
#     lower=any(i.lower() for i in user)
#     digit=any(i.isdigit() for i in user)
#     symbol=any(i in sp  for i in user)
#     if(upper and lower and digit and symbol):
#         print("strong password")
# else:
#     print("weak password")

# l=[]
# l1=[]
# user=input("enter a no of rows:")
# for i in range(7):
#     book=int(input("enter a list of booked seat:"))
# if(i not in l):
#     for i in range(n):
#         for i in range(2):
#             i.append(l)

# print first letter of each string
# l=['abc','pqr','xyz']
# l2=[i[0] for i in l ]
# print(l2)
# 
# s='python program'
# l=[i[::-1] for i in  s.split()]
# print(l)

# l=[1,2,3,4]
# d={i:i**2 for i in l}
# print(d)
# 
# l=[74,88,43,33,70]
# l2=['pass' if i>=70 else 'fail' for i in l]
# print(l2)

# lambda function
# d=[
#   {"item":"pen","price":70},
#   {"item":"pencil","price":10},
#   {"item":"book","price":80},
#   {"item":"notebook","price":10}
#  ]
# l=sorted(d,key=lambda x:x["price"])
# print(l)
# print(list(filter(lambda x:x['price']>70,l)))
# print(list(map(lambda x:x['item'].upper(),d)))
# print(list(map(lambda x:x['price']*2,d)))
# print(list(filter(lambda x:len(x['item'])>=7,d)))
# a=[1,2,3,4,7]
# b=[2,3,7]
# print(list(filter(lambda x:x in b,a)))
 
# l=[1,4,0,True," ",-1,-33,False,0.0,{},(),[]]
# print(list(filter(lambda x:x==None,l)))
# class a:
#     def __init__(self):
#         print("constructor class a")
# class b(a):
#     def __init__(self):
#         super().__init__()
#         print("constructor class b")
# class c(b):
#     def __init__(self):
#         # b.__init__(self)
#         super().__init__()
#         print("constructor class c")
# c1=c()
# # 
# class a:
#     def __init__(self,a):
#         print("constructor class a")
#         # self.a=a
#         print(a)
# class b(a):
#     def __init__(self,a,b):
#         super().__init__(a)
#         print("constructor class b")
#         # self.b=b
#         print(b)
# class c(b):
#     def __init__(self,a,b,c):
#         # b.__init__(self)
#         super().__init__(a,b)
#         # self.c=c
#         print("constructor class c")
#         print(c)
# c1=c(10,20,30)
# 
# class p:
#     def __init__(self,a):
#      print(a)
# class q:
#     def __init__(self,a):

#      print(b)
# class r(p,q):
#     def __init__(self,a,b,c):
#      p.__init__(self,a)
#      q.__init__(self,b)
#      print(c)

# a=input("enter a value:")
# b=input("enter a value:")
# c=input("enter a value:")
# r1=r(a,b,c)

# 
class a:
    print("a")
class b(a):
    print("b")
class c(b):
    print("c")
class d:
    print("e")
class e(c,d):
    print("f")


e1=e()
