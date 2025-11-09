no1=int(input("enter a no:"))
no2=int(input("enter a no:"))
while(no1<no2):
    if(no1%2==0):
        print(no1)
        no1+=1
        
no=int(input('enter a no :'))
# rev=0
n2=no
sum=0
while(no>0):
    rem=no%10
    sum=sum+rem*rem*rem
    no=no//10
    if(sum==n2):
        print("it is amstrong no")
    else:
        print("it is not amstrong no")


# a=int(input("enter a no:"))
sum=0
b='y'
while(b=="y" or b=="Y"):
    a=int(input("enter a no:"))
    b=input("do u want to continue (y/n)")
    sum=sum+a
    print(sum)