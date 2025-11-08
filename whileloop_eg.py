# wrtie a python program to print first 1000 natural no
i=1
while i<=1000:
    print(i)
    i=i+1
# even no
i=2
while i<=100:
    print(i)
    i=i+2
# even no addition
i=2
sum=0
while i<=100:
    # print(i)
      sum=sum+i
      i=i+2
print(sum)

i=1
sum=0
while i<=100:
    if(i%2==0):
        # print(i)
        sum=sum+i
    i=i+1
print(sum)

# table
i=1
num=int(input("enter a no you want to print a table:"))
while(i<10):
    # print(num*i)
    i=i+1
    print(num,"*",i,"=",num*i)
 
i=10
while(i>=1):
    i=i-1
    # i=i+1
    print(i)

# reverse the no
no=input("enter a no:")
print(no[::-1])

# reverse the nno using while
no=int(input('enter a no :'))
rev=0
while(no>0):
    print(no) 
    rem=no%10
    rev=rev*10+rem
    no=no//10
# print(rev)
print("no\t\trem\t\trev\n")
print(no ,"\t","\t",rem,"\t\t",rev)


# write a program check the given no is palindrome or not
no=int(input('enter a no :'))
n2=no
rev=0
while(no>0):
    rem=no%10
    rev=rev*10+rem
    no=no//10
# print(rev)
if(rev==n2):
    print("it is palindrome")
else:
    print("it is not palindrome")