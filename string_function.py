# string function
a='python'
b='python'
print(a==b)
print(a!=b)
print(a<=b)
print(a>=b)
print(a<b)
print(a>b)

# write a python prog take a 2 string from user and check wether they equal or not
a=input("enter a string:")
b=input("enter a string:")
if(a==b):
    print("the string is equal")
else:
    print("the string is not equal")

# string function
a='prachi'
print("capitalize():",a.capitalize())
print("lower():",a.lower())
print("upper():",a.upper())
print("swapcase():",a.swapcase())
print("title():",a.title())
print("casefold():",a.casefold())
a='prachi'
print("center(width):",a.center(50))
print("center(width,fillchar):",a.center(50,"*"))
print("count(string):","12356543431231".count("2"))
print("count(string):","12356543431231".count("2",2,5))
a='prachi'
print("startswith('char'):",a.startswith('i'))
print("startswith('char'):",a.startswith('$',2,4))
print("endswith('char'):",a.endswith('i'))
print("endswith('char'):",a.endswith('$',2,4))
print("find('char'):",a.find('i'))       # return index of the first occurence of the substring if find otherwise it return -1
print("find('char'):",a.find('a',2,4))
a='praching'
print("find('char'):",a.replace('ing','ly'))
print("rfind('char'):",a.rfind('i'))
print("rfind('char'):",a.rfind('$',2,4))
print("index('char'):",a.index('i'))    #return index of the first occurence of the substring if find otherwise it return valueerror
print("index('char'):",a.index('a',2,4))
print("rindex('char'):",a.rindex('a'))
print("rindex('char'):",a.rindex('a',2,4))
k1='pythoonn'
# print(id(k))
k1=k.replace('y','$',2)
# print(id(k))
# print(id(k))
print(id(k1))
print(k)

p='python123' 
print(p.isalnum())
print(p.islower())
print(p.isupper())
print(p.istitle())
print("hello world".isspace())
print(p.isalpha())
print('hello'.isprintable())
print('abc123'.isidentifier())

m='python122rttt33'
print(m.split('&'))
print(m.split())
print(m.split('&',3))
print(m.partition(' '))

print("123/u3442".isdecimal())
print("\u1122".isdigit())
print("1233442".isnumeric())


# eg
# write a python prog to check given string palindreom or not 
a=input("enter a string:")
if(a[::]==a[::-1]):
    print("it is palindrome")
else:
    print("it is not palindrome")

# write a python prog to get a string made up of the first 2 and last 2 char of a given string 
# if the string len is less than 2 then return empty string 
s=input("enter a string:")
if(len(s)<2):
    print("empty string:")
else:
    print(s[0:2]+s[-2:])

#write a python prog to add "ing" at end of given string (length should be atleast 3)if given string 
# already ends with "ing" then add "ly" at the end 
# if the string length is <3 return the orignal string
user=input("enter a string:")
if(len(user)<=3):
    print("the orignal string is:",user)
elif(user.find('ing')=='ing'):
    print(user.replace('ing','ly'))
else:
    print(user+'ing')

print('abc&gmail&.com'.partition('&'))
print('abc&gmail&.com'.rpartition('&'))
print('prachii'.rjust(20))
print('prachii'.rjust(20,'*'))
print('prachii'.ljust(20))
print('prachii'.ljust(20,'*'))
print('         prachii')
print('          prachii'.strip())
print('sssprachii'.strip('s'))
print('           prachiisss'.lstrip('s'))
print('prachiiss'.lstrip('s'))
print('prachiiss       '.rstrip('s'))
print('prachiss'.rstrip('s'))
#  
print('@ab'.join("prachi"))
print('prachii'.zfill(20))
a='prachi'
b=a.maketrans('r','$')
print(b)
print(a.translate(b))
print(a)
b=a.maketrans('r','$','i')
print(b)
print(a.translate(b))

a='h\te\tl\to'
print(a)
print('expandtabs():',a.expandtabs())
print('expandtabs(tabsize):',a.expandtabs(2))
print('expandtabs(tabsize):',a.expandtabs(3))
print('expandtabs(tabsize):',a.expandtabs(5))
