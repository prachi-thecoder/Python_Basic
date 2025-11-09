print("1.add member:" )
print("2.union which two club you want to union='science,arts,commerce':")
print("3.show intersection:")
print("4.remove member:club member ")
print("5.check membership:")
print("6.exit")
science=set()
commerce=set()
arts=set()
while(True):
    choice=input("enter your choice:")
    if(choice=='1'):
        a=int(input("enter a no of member you wnat to add:"))
        a_b=input("enter which club you want to add member:")
        for i in range(a):
            if(a_b=="science" or a_b=='SCIENCE'):
                member=input("enter a member name:")
                science.add(member)
                print(science)
                
            elif(a_b=="commerce" or a_b=='COMMERCE'):
                member=input("enter a member name:")
                commerce.add(member)
                print(commerce)
                
            elif(a_b == "arts" or a_b=="ARTS"):
                member=input("enter a member name:")
                arts.add(member)
                print(arts)
                
    elif(choice=='2'):
        uni=input("enter a club which 2 chlub you want to union:")
        uni_i=input("enter a club which 2 chlub you want to union:")
        if(uni=='science' or uni=='SCIENCE' and uni_i=='commerce' or uni_i=='COMMERCE'):
            print(science.union(commerce))
        elif(uni=='commerce' or uni=='COMMERCE' and uni_i=='arts' or uni_i=='ARTS'):
            print(commerce.union(arts))
        else:
            print(arts.union(science))
    elif(choice=='3'):
        uni=input("enter a club which 2 chlub you want to intersection:")
        uni_i=input("enter a club which 2 chlub you want to intersection:")  
        if(uni=='science' or uni=='SCIENCE' and uni_i=='commerce' or uni_i=='COMMERCE'):
            print(science.intersection(commerce))
        elif(uni=='commerce' or uni=='COMMERCE' and uni_i=='arts' or uni_i=='ARTS'):
            print(commerce.intersection(arts))
        else:
            print(arts.intersection(science))     
    elif(choice=='4'):
        opi=input("enter which club you want to remove member:")
        if(opi=='science' or opi=='SCIENCE'):
            user=input("enter a name you want to remove:")
            science.remove(user)
            print(science)
        elif(opi=='commerce' or opi=='COMMERCE'):
            user=input("enter a name you want to remove:")
            commerce.remove(user)
            print(commerce)
        elif(opi=='arts' or opi=='ARTS'):
            user=input("enter a name you want to remove:")
            arts.remove(user)
            print(arts)
    elif(choice=='5'):
        a_b=input("enter which club you want to check member:")
        member=input("enter a member name:")
        if(a_b=="science"):
            print("it is a member of science club",member in science)
        elif(a_b=='commerce'):
            print("it is a member of commerce",member in commerce)
        elif(a_b=='arts'):
            print("it is a member of arts",member in arts)
        else:
            print("it is a not member")
    elif(choice=='6'):
        print("EXIT")
        break
    else:
        print("enter a valid choice")