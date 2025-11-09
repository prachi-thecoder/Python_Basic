l=[1,2,3,4,5,6,7]
k=map(lambda x:x*2,l)
print(list(k))

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
p=map(l,lambda x:x['price']*0.5)
print(list(p))

# sorted using age 
l=[{'info':{'age':19}},
   {'info':{'age':21}},
   {'info':{'age':18}}
]
p=sorted(l, key=lambda x:x['info']['age'])
print(list(p))

# take a list of string and convert into int
l=["1","2","3","4"]
a=map(lambda x: int(x),l)
print(list(a))

#given a list of string filter out string having len<5 then convert the
#  remaning string to uppercase using map and lambda fun
l=["cat","iuhuh","hiuis","ff","his"]
a=filter(lambda x:len(x)<5,l)
print(list(map(lambda x:x.upper(),a)))

# print all the true values from the list
l=[1,2,0,True,"",-1,-45,False,0.0,{},[],()]
a=filter(None,l)
print(list(a))