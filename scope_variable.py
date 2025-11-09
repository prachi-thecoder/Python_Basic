# local variable
def f1():
    a=10
    print(a)
f1()
# global variable
a=10
def f2():
    a=20
    print(a)
f2()
print(a)

# global keyword
a=10
def f3():
    global a
    a+=2
    print(a)
f3()
print(a)

# nonlocal varible
a=10
def f3():
    a=20
    print(a)
    def f4():
        nonlocal a
        a+=2
        print(a)
    f4()
    print(a)
f3()
print(a)

# passing a immutable parameter in function    call by value 
def f1(a):
    a=a.lower()
    print(a) 
    print(id(a))
x="PRACHI"
f1(x)
print(x)
print(id(x))

# passing a mutable parameter in function    call by reference
def f1(a):
    a.append(80)
    print(a)
    print(id(a))
x=[1,2,4]
f1(x)
print(x)
print(id(x))

