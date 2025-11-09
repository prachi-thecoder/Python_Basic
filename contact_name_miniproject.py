# print("1.add contacts:")
# print("2.search contacts:")
# print("3.view all:")
# print("4.count contacts:")
# print("5.delete contacts:")
# print("6.clear all contacts:")
# print("7.exit")
d={}
# count=1
while(True):
    print("1.add contacts:")
    print("2.search contacts:")
    print("3.view all:")
    print("4.count contacts:")
    print("5.delete contacts:")
    print("6.clear all contacts:")
    print("7.exit")
    user=input("enter a choice:")
    if(user=='1'):
        name=input("enter a name of contact:")
        no=int(input("enter a no:"))
        d[name]=no
        print(d)
        print("your no is added successfully")
    elif(user=='2'):
        search=input("enter a name of contact you want to search of no :")
        print(d.get(search,'not found'))
    elif(user=='3'):
        print(d)
    elif(user=='4'):
        print("total no of contacts:")
        count=len(d)
        print(count)
    elif(user=='5'):
        dele=input("enter a element u want to remove:")
        d.pop(dele)
        print(d)
    elif(user=='6'):
        print(d.clear())
        print("all the contacts are clear")
    elif(user=='7'):
        print('exit')
        break