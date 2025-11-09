d={'name':'prachi','marks':20}
print(len(d))
print(max(d))
print(min(d))
print(sorted(d,reverse=True))
d1={1:'a',2:'b'}
print(sum(d1))
print(all(d1))
print(reversed(list(d1)))
print(any(d1))

# key()
d={'name':'prachi',"age":19}
print(d.keys())
print(d.values())
print(d.items())
# print(d[3])  #keyerror
print(d.get('age'))
d={'name':'prachi'}
print(d.get('name'))
print(d.get(3,"not found"))  

# update()
d1={"name":"prachi","marks":21}
d2={"age":19,"city":"newyork"}
d1.update(d2)
print(d1)
d1.update({"country":"usa"})
print(d1)
d1.update(name="xyz",marks=40)
print(d1)

