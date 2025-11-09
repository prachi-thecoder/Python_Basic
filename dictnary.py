# creation of dictnary
# note: keys are inmutable means not changeble and values are mutable measns changeble
d={}
print(type(d))
d1={'name':"prachi","roll":21}
print(d1)
d2={1:{'a':'b'},2:{'c':'d'}}
print(d2)
# d3={[1,2]:10}
# print(d3)
d4={10:[1,2]}
print(d4)
d5={'name':"prachi","roll":21,'Name':'tony'}
print(d5)

#creation of dictnary using dict constructor
d=()
print(d)
d1=dict(['abc',10])
print(d1)
d2=dict(rollno= 1,name='pqr')
print(d2)
# accesing 
d={1:'a',2:'b'}
print(d[1])
d1={'name':'pqr','marks':20}
print(d1['marks'])
# update
d1={'name':'pqr','marks':20}
print(d1['marks'])
d1['name']="abc"
print(d1)
# adding new key and value
d1['rolno']=10
print(d1)
d={1:'a',2:'b'}
# delete dictnary
del d[1]
print(d)
# traversing
d={'name':"prachi",'marks':10}
for i in d:
    print(d[i])
    print(i)
for i,j in enumerate(d):
    print(j,d[j])
dict={}
dict={1:10,2:20}
 
d=dict([(1,'one'),(2,'two')])
print(d)

# neasted dictnary
nested_dict = {
    'student1':{'name':'prachi','age':20},
    'student2':{'name':'praxii','age':19}
}
# print(nested_dict)
# print(nested_dict['student2'])    #accessing nested dict
nested_dict['student1']['phone_no'] = 8784658934   #adding a new value in nested dict
del nested_dict['student1']['age']  #del a key and value from dict 
print(nested_dict)
nested_dict['student3'] = {'name':'prajakta','age':18}    #adding new nested dict
print(nested_dict)
nested_dict['student2']=30       #modifying the values in dict
print(nested_dict)
 
# dict within list
travel_data={
    'ahmednagar':['vishalganpati','chandbibi','dongargan'],
    'pune':['dagdusheth halwaiganpati','ganjbazar']
}
print(travel_data) #printing a dic
print(travel_data['pune'])   #accessing a nested list
# list within dic
travel=[
    {'name':'prachi','age':19},
    {'birth':21,'time':5}
]
print(travel)
print(travel[0])

# looping in dic
info={
    'person1':{
    'name':'prachi',
    'age':19},
    'person2':{
        'name':'prajakta',
        'age':20
    }
}
for i in info.values():
    print(i)
    for k,v in i.items():
        print(f"{k} {v}")