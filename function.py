# def f1():
#     block
# f1()
def f1():
    print("welcome to function")
f1()
# function with no argument with return type
def f1():
    return"prachi"
print(f1())
def f3():
    return 1,2,3,4
print(f3())
def f4():
     return 1,2,3,4
print(f4())
a,b,c,d=f4()
print(type(a))

# function with parameter
def f1(a):
    print(type(a))
f1(10)
f1([1,2,3])
f1((1,2,3))
# print(type(a))
# function with parameneter and argument no return value
def add(a,b):
    print(a+b)
x=int(input("enter a no:"))
y=int(input("enter a no:"))
print(add(x,y))


# function with return value
def f1(a,b):
    return a+b, a-b, a*b, a%b, a//b, a/b, a**2 ,b**2
print(f1(10,20)) 
# function with default value
def sum(a,b=10):
    print(a,b)
sum(10)
# 
def sum(a,b=2,c=10):     #a,b are positional argument   and c=10 are keyword argument
    print(a+b*c)
sum(10) 

#function with multiple argument(*args) :accept multiple values as a tuple
def add(*args):
    print(args[0]+args[1])
    print(sum(args))
add(1,2,3,4)

# function with keyword argument using **kwargs :accept named arguments as a dictnary
def display(**keyw):
    for key , value in keyw.items():
        print(f"{key}: {value}")
display(name='prachi',age=19,city="nagar")

# all in one 
def example(a,b=2,*arg,**args):
    print("a=",a)
    print("b=",b)
    print("arg=",arg)
    print("args=",args)
example(1,2,3,4,5,x=10,y=20)

# nested function syntax
# def outer():
#     def inner():
#         print("inner")
#     print('outer') 
#     inner()
# outer()

# recursion
def f1(n):
    print(n)
    if(n==10):      #base case
        return
    f1(n+1)      #recursion case
f1(1)

