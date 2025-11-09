# additation
from functools import reduce
l=[1,2,3,4,5,6,7,8]
a=reduce(lambda x,y:x+y,l)
print(a)

# print addition of odd no using reduce function
from functools import reduce
l=[1,2,3,4,5,6,7,8]
b=filter(lambda x:x%2!=0,l)
print(reduce(lambda x,y:x+y,b,8))
# print(a)

#mini project
# 1.filter out q with 0 
# calculate total price for each valid order
# calculate total bill using reduce
from functools import reduce
orders=[{'item':'laptop','price':50000,'quantity':1},
        {'item':'mouce','price':500,'quantity':-1},
        {'item':'keyboard','price':1500,'quantity':2},
        {'item':'monitour','price':12000,'quantity':1},
        {'item':'kebal','price':1000,'quantity':3}
 ]
a=filter(lambda x:x['quantity']>=0,orders)
# print(list(a))
b=map(lambda x:x['price']*x['quantity'],a)
# print(list(b))
p=(reduce(lambda x,y:x+y,b))
print(p)

# biling per patient,total bill,no of patient are eligible for free consultant
# patient with age>60 get 20% disc
# patient with income<15000 get free consultion
patients=[
           {
                'name':"amit","age":65,"fee":500,"income":18000
           },
           {
                'name':"rita","age":45,"fee":500,"income":12000
           },
           {
                'name':"suresh","age":70,"fee":500,"income":10000
           },
           {
                'name':"pooja","age":30,"fee":500,"income":20000
           }
]
        