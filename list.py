# creation of list
l=[1,2,3,23,22,1,21]
print(l)

l1=[-1,-2,0,1,2,3,4]
print(l1)

l2=[1.1,2.3,3.3]
print(l2)

l3=['a','b','c']
print(l3)

l4=[1+2j,2+3j]
print(l4)

l5=[1,2.3,'r']
print(l5)
el=[]
print(el)
print(type(el))

l1=[1,2,3,4,5,5,
    5,6,6,7,3,3,
    3,45,5,  
]
print(l1)
nl=[[1,22,3,44],[2,3,4,5,6]]
print(nl)

a='python'
print(list(a))
l='1000'
print(list(l))

# accessing a list
l=[1,2,3,4,5,5,6,76,0]
print(l[7])
print(l[-7])
print(l[2])
print(l[-2])

l=[1,2,3,4,5,[56,66]]
print(l[5])
print(l[5][1])
print(l[-1][1])
print(l[-1][-2])

# travelsing a list
# using for loop
l=[1,2,3,4,5,5,6,6]
for i in l:
    print(i)
# using range
for i in range(len(l)):
    print(l[i])
# using while loop
i=0
while(i<len(l)):
    print(l[i])
    i += 1
    # 
for i,j in enumerate(l,10):
    print(i,j)

# list compreshenion
[print(i) for i in l]

# list update note:the content of the list has been changes after creation 
# ii] python wil not create a new list after update
# update using index
l=[1,2,3,4,4]
print(l)
print(id(l))
l[2]=100
print(l)
print(id(l))
# update using slicing
list1=[10,2,3,4,5,6,7,7,7,23,4,4]
print(list1)
print(list1[0:5])
print(list1[:5])
print(list1[5:])
print(list1[:])
print(list1[-5:-2])
print(list1[-2:-5])
print(list1[:11])
print(list1[2:0])
print(list1[4:None])
print(list1[-3:8])
print(list1[-7])
print(list1[::2])
print(list1[1::2])
print(list1[::-1])
print(list1[-4:-2:-1])
print(list1[-2::2])

