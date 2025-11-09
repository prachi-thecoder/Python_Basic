# print positive no
l=[1,2,3,4,5,6,7,8,-1]
a=filter(lambda x:x>=0 , l)
print(list(a))

# print even no
l=[1,2,3,4,5,6,7,8,]
a=filter(lambda x:x%2==0 , l)
print(list(a))

# create a list of string and filter the string lenth is more than 3
l=['abc','krc','pqrs','iugiyg']
a=filter(lambda x:len(x)>3 ,l)
print(list(a))

# to sort a list of dict 
k=[{'name':'prachi','age':20},{'name':'abc','age':18}]
p=sorted(k,key=lambda x:x['age'])
print(p)

#create a list and find average then add a list is greater than average
l=[1,2,3,4,5,6]
a=sum(l)/len(l)
print(a)
d=filter(lambda x:x>a,l)
print(list(d))

#create a list of dict and sort them after giving discount
l=[
    {
        'item':'pen','price':100
    },
     {
        'item':'bag','price':600
    },
     {
        'item':'writing_pad','price':50
    }
]
p=sorted(l,key=lambda x:x['price']*0.5)
print(p)


