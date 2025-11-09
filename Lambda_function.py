# no parameter no retun
f1=lambda : print('python')
print(type(f1()))
print(f1())
# only return value
f1=lambda:9
print(f1())

# with parameter no return type
f1=lambda x: print(x)
f1(2)
print(f1(2))
#function with parameter with return type
x=lambda x:x*2
print(x(3))

# function with varible argu
x=lambda *x:sum(x)
print(x(3,2,3,4,5))
#withoun calling 
print((lambda x:x*8)(4))
print((lambda x,y:x+y,x*y,x/y,x-y)(2,3))  #it will give nameerroe because it retun only single value

print((lambda x,y:(x+y,x-y,x*y,x/y,x//y))(2,3))
# unpack 
result=lambda x,y:(x+y,x*y)
a,b=result(2,4)
print(f"a={a},b={b}")

# check given no is even or odd using lambda fun 
l=int(input("enter a no:"))
a=lambda l:print("even")if(l%2==0)else print("odd")
a(l)
# l=[1,2,3,4,5,6]n
