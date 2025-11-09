# mini project 
print("1.add a name to list")
print("2.remove from list")
print("3show list")
print("4. exit")
b1=[]
while(True):
    a=input("enter a choise:")
    if(a=='1'):
        user=input("enter a list items:")
        b1.append(user)
        print(b1)
    elif(a=='2'):
        name=input("enter a name you want to remove:")
        b1.remove(name)
        print(b1)
    elif(a=='3'):
        print(b1)
    elif(a=='4'):
        break
    else:
        print("enter a correct choise")
        


