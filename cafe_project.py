cold={'iced coffee':110,
      'cold coffee':60,
      'milkshake':50
      
}
hot={
    'espresso':30,
    'hot choclate':50,
    'latte':140
    
}
snacks={
      'paneer pizza':110,
      'sandwich':50,
      'pasta':40,
      'french fries':40      
}
dessert={
    'choclate cake':50,
    'brownie':60,
    'chesse cake':100
    
}
print(cold,hot,snacks,dessert)
# print(d)
d={}
add=0
while(True):
    print('1.add items if u want :')
    print("2.remove dish")
    print('3.search')
    print("4.view all")
    print("5.exit")
    user=input("enter a choice:")
    if(user=='1'):
        key=input("enter a dish name:")
        valu=input("enter a price:")
        d[key]=valu
        print(d)
    elif(user=='2'):
        remo=input("enter a dish u want to remove:")
        d.pop(remo)
        print(d)
    elif(user=='3'):
        sea=input("enter a dish name:")
        print(d.get(sea,'not found'))
    elif(user=='4'):
        print("all items :",d) 
    elif(user=='5'):
        print('exit')
        break  
a="drinking"
print(a.center(50,"*"))
menu={
    'juice':{
         'apple juice':'40rs',
        'mango juice':'40rs',
        'mix juice':'50rs',
        'watermelon juice':'40rs',
        'cocunut juice':'50rs'
    }

}
print(menu)
for i,j in menu .items():
    print(f"\n {i}:")
    for j in [menu][juice].items():
        print(f'\n {j}')


# print([menu]['juice'])
