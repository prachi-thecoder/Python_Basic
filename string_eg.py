# write a python prog to take a string from user and check wether the string is uppercase or not 
# if it is yes then convert into lowercase
user=input("enter a string:")
if(user.isupper()):
    print("yes it is uppercase",user.lower())
else:
    print(user)

# wtp prog to take 2 string from user and if it is equal 
# then replace first char of both the string with '$' else replace with@
user1=input("enter a string:")
user2=input("enter a string:")
if(user1==user2):
    print(user1.replace(user1[0],'$'), user2.replace(user1[0],'$'))
else:
    print(user1.replace(user1[0],'&'), user2.replace(user2[0],'&'))

# wtp prog to count digit alphabets ,specialsymbols in a given string
count=0
count1=0
count2=0
user=input("enter a string:")
for i in user:
    if i.isdecimal():
        count+=1
    elif i.isalpha():
        count1+=1
    else:
        count2+=1
print("the decimal no is :",count)
print("the aplhabet is :",count1)
print("the specialsymbol is:",count2)

# wapp to take a string from user and take and character from user and find wether the character 
# is in string or not  if yes then replace that char with # and fill given strirng 000
# else fill with 00000
a=input("Enter a string:")
b=input("Enter a character:")

c=a.find(b)
if c+1:
        d=a.replace(b,'#')
        print(d,d.zfill(len(a)+3))
else:
    print(a.zfill(len(a)+5))

# wpp take a string from user and check given string is in lower case or not if yes
# then count first char occurance in a given string  and split using first char 
# else then convert into lower case and perform partition using second char of given string 
user=input("enter a string:")
if(user.islower):
    print(user.count(user[0]))
    print(user.split(user[0]))
else:
    print(user.lower())
    print(user.partition(user[1]))

# 
user=input("enter a string:")
print(user.replace(user[0],'$'))   
# clculate sum and average of a digit in present string
text='python@123987p'
count=0
sum=0
for i in text:
    if(i.isdecimal()):
        count+=1
        sum=sum+int(i)
print("the no is:",count)
print("the sum is :",sum)
print("average of given is:",sum/count)

# 
a='python123  programing abc12'
count=0 
for i in a:
    if(i.isalnum()):
        count+=1
print("the alphabets and no is :",count)

# to count no of words in string
a='python123 programing abc12'
# print(len(a.split(" ")))
print(a.isnumeric())

        
