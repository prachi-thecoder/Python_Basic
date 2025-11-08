# tuppel creation
t1=()
print("empty tuple:",t1)
t2=(5,)
print("single element tuppel:",t2)
t3=(1,2,3,4,5)
print("tuppel element with multiple element:",t3)
t4=(1,True,'prachi',3,13)
print("heterogenaous tupple:",t4)
t5=(1,(2,3),[4,5])
print("neasted tupple:",t5)
t6=1,2,3,4,5,6
print("tupple without parenthese:",t6)
print("type of t6:",type(t6))

# creation a tuple using the tuple() constructor
t6=tuple("hello")
print("tuple from string",t6)
t7=tuple([1,2,3,4])
print("tuple created using tuple()constructor:",t6)

# accesing element
t=(10,20,30,40,50,60)
print(t[0])
print(t[-1])

# slicing
t=(1,2,3,34,45,5,6,7,87,6)
print(t[1:3])
print(t[:])
print(t[1:2:5])
print(t[::-1])

# nested tupple access
t=(1,(2,3),[4,5])
print(t[1])
print(t[1][0])

# updating a tuple
t=(1,3,4,5)  #type error:'tuple' object does not support item assignment

t[1]=5

t=(1,(2,3),[4,5])
t[2][0]=6   #this is allowed because the inner list is mutable 
print(t)

# traversing a tuple
t=(1,2,3,4,5,6)
for i in t:
    print(i)

# tuple comprehesion
t=(x*2 for x in range (5))
print("tuple comphensiion",tuple(list(t)))

# delete tuple
del t
print(t)

# tuple operation
# concatination
t1=(1,2)
t2=(2,3)
t3=t1+t2
print(t3)

# repetation
t4=t1*3
print(t4)

# membership operator
t=(1,2,3,4)
print(2 in t)
print(5 not in t)

# tuple unpacking
t=(1,2,3)
a , b , c = t
print("unpacking values",a,b,c)

# tuple function
t=(1,2,4,5,6,7,8,9,4)
print("tuple",t)
print("length",len(t))
print("count of 4",t.count(4))
print("index of 4",t.index(4))
print("maximum",max(t))
print("minimum",min(t))
print("sum",sum(t))
sorted_list=sorted(t,reverse = True)
print("sorted",sorted_list)
print("orignal tuple after sorting",t)


# 
