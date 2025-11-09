# syntax : for variable in sequence :
#                        statements
# short hand for loop : for variable in sequence : statement
# eg
# write a python prog to print cube of first 100 even no
for i in range(2,201,2):
    print("cube of i",i)
    print(i**3)

# write the python prog to find a sum of series of a no up to nth term
no=int(input("enter a no:"))
nth=int(input('enter a nth term:'))
i=0
sum=0
while(i<=nth):
    sum=sum+no
    no=sum*10+no
    print(sum)

# 
n=int(input("enter a no:"))
t=int(input("enter a nth term:"))
sum=0
n1=n
for i in range(0,t):
    sum+=n
    n=n*10+n1
print(sum)
# 
n=int(input("enter a no :"))
nth=int(input("enter a nth term:"))
sum=0
n1=n
for i in range(0,nth):
    print(n,end='+')
    sum+=n
    n=n*10+n1
print("=",sum)

#wtpp  to take a input from user and print n natural no in decending order
n=int(input("enter a no:"))
for i in range(n,0,-1):
    # i=i+1
    print(i)
