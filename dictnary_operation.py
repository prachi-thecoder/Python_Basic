# membership operator
d1={'name':'prachi','marks':20}
print("is 'name' key in d1","name" in d1)
print("is 'age' key in d1","age" in d1)
# identity operator
a={"name":"abc","marks":30}
b={"name":'abc','marks':30}
print("is a is b ",a is b)
print("is a is not b:",a is not b)

# comparison operetor
a={"x":1,"y":2,"z":3}
b={'x':1,"y":2}
print(a==b)
print(a!=b)

# dictinory merge operator
a={"x":1}
b={"y":2}
print("union of a and b:",a|b)
print(a)
print(b)

a|= b
print("combining two dictionory and assign:",a)
print(b)

# dictionary assignment opertor 
a={"x":1,"y":2}
b=a
print("assginment b to a:",b)
a['x']=10
print(a)
print(b)
