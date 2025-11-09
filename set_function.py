# general purpose set function
s={1,3,4,5,6,7,8,2,3,5,6,6}
print(s)
print(len(s))
print(min(s))
print(max(s))
print(sorted(s))
print(sum(s))
print(all(s))
print(any(s))
print(sorted(s,reverse=True))

#reverse 
s={1,2,3,4,4,4,5,5}
print(list(reversed(list(s))))
# add fun()
s.add(7)
print(s)
s.add("prachi")
print(s)
s.add(2)
print(s)
s.add((1,2))
print(s)
s.add()
# print(s)
# update fun()
s={1,2,3,4}
s.update((1,5))
print(s)
s.update([1,9])
print(s)
s.update("prachi")
print(s)
#remove fun
s1={1,1,2,3,4,4,5,'prachi'}
s1.remove(3)
print(s1)
# discard fun()
s={1,2,3,3,3,4,5}
s.discard(21)
print(s)
# pop
removed = s.pop()
print(removed)
print(s)
# clear()
s1={1,1,2,4,6,6,5}
s1.clear()
print(s1)

# set operation
s1={1,2,3,4,5}
s2={1,3,4,6,7}
print(s1 | s2)  #when we use unoin the parameter is itreable
print(s1.union(s2))
print(s1.union("prachi"))
print(s1.union({10,20}))
# intersection
s1={1,2,3,4,5}
s2={1,3,4,6,7}
print(s1 & s2)
print(s1.intersection(s2))
print(s1.intersection((1,2)))
print(s1)
print(s2)
print(s1.intersection_update(s2))
print(s1)
print(s2)
# diffrence
s1={1,2,3,4,5}
s2={1,2,3,5,6}      #which is not common 
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.symmetric_difference(s2))
print(s1^s2)
# symmetric_difference_update
s1.symmetric_difference_update(s2)
print(s1)
print(s2)
# subset
s1={1,2,3,4,5,6}
s2={2,3,5,4,6}
print(s1.issubset(s2))
print(s1<=s2)   #s2 element in s1 
print(s1.issuperset(s2))  #s2 element in s1 
print(s1>=s2)
print(s1.isdisjoint(s2))    #no common element it will retrun true
print(s1!=s2)
# frozen set
# 
s={1,2,3,4,5}
f=frozenset([1,2,3])
print(f)
print(type(f))
# f.add(10)
s.add("prachi")
print(s)
f=frozenset([1,2,3])
print(f)