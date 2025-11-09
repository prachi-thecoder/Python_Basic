# built in function
l1=[1,2,3,4,5,6,7,8,8,9,9,1]
print(l1)
print(type(l1))
print("length of string : ",len(l1))
print("maximum value from list :",max(l1))
print("minimum value from list :",min(l1))
print("sum of list element:",sum(l1))
print("sum(list,start): ",sum(l1,100))
print("sorted(l): ",sorted(l1))
print("sorted(list,reverse): ",sorted(l1,reverse=True))
print("all(l1):",all(l1))
print("any(l1):",any(l1))
print("reversed(l1):",list(reversed(l1)))
# 
s=['a','b','c','d','e','f','g','h','i','j']
print(s)
print(max(s))
print(min(s))

c=[2+2j,4+5j,1+3j,4+5j]
print(sum(c))
print("sum of complex element in list: ",sum(c))

l=['aaa','av','cda','abcd','aad']
print(l)
print(sorted(l))
print(sorted(l,reverse=True))
print(sorted(l,key=len))
# append function
l=[1,2,3,4,5,6]
print("append(element)",l.append(6))
print("append(element):",l)

l.append([10,20,30,40,50])
print("append(element):",1)
l.append("abc")
print(l)
l.append(1+2j)
print(l)

# extend function
l="python"
l1=[1,2,3,4,5]
l1.extend(l)
print("extend(sequence):",l1)
l1.extend(['a','b','c'])
print("extend(seq):",l1)

# insert func
l=[1,2,3,4,5]
print(l.insert(1,'abc'))
print("insert(1,'abc):",l)
l=[1,2,3,4,5]
l.insert(-2,10)
print("insert(-1,20):",l)
l.insert(-5,50)
l=[1,2,3,4,5,6]
l.insert(-1,70)
print("insert(6,70):",l)
l.insert(6,[80,90])
print("insert(6[80,90]):",l)

# count
l=[1,2,3,4,5,6,7,8,8]
print("index(2):",l.index(2))
print("index('3):",l.index('3'))
print("index(8):",l.index(8))

# index(element)
l=[10,2,30,40]
print("index(3):",l.index(2))
# print("index('3):",l.index('3'))

l=[True,False,1,2]
print(l.index(True))
print(l.index(False))
# index(element , start ,end)
l=[2,1,23,45]
print(l.index(2))
print(l.index(2,1))
print(l.index(2,1,4))

# reverse()
l=[10,20,30,40,50]
l.reverse()
print(l)

# sort
l=[1,2,4,6,78,5]
l.sort()
print(l)
l.sort(reverse=True)
print(l)
l=['aa','abc','ab','abcd']
l.sort(key=len,reverse=True)
print(l)

# pop
l=[10,20,30,40,40]
print(l.pop())
print(l)
print(l.pop(2))

# remove
l=[10,20,30,40,50,60,3]
l.remove(20)
print(l)

# clear
l=[1,2,4,6,7]
l.clear()
print(l)
print(id(l))

# del()
a=10
print(a)
del(a)

l=[1,3,4,5,6]
del l[1]
print(l)