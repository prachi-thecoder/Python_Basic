# syntax of nested if 
# if condition:
#     if condition:
#         statement 1
#         statement 2
#     statement 3
# statement 4

# # nested if else
# if condition:
#     if calculate:
#         statement 1
#     else:
#         statement 2
# else:
#     statement 3
#     if condition:
#         statement 4
#     else:
#         statement5
    
if(1000):
    if(True):
        print("helo")
        print("helo1")
    print("if end")
else:
    if(0):
        print("else if ")
    print("else")

i=100
if(1==10):
    if(i<20):
        print("i is smaller than 20")
if(i<15):
    print("i is smaller than 15")
else:
    print("i is grater than 15")

# short hand if statement syntax if condition:statement
# short hand if else statement syntax stat1 if condition else state2
a=10
print("+ve")if a>0 else print("-ve")
# write a python program to cheak enter no is even or odd using short hand if else
no=int(input("enter a no :"))
print("no is even ")if no%2==0 else print("odd")

a=10
b=20
print("a") if a>b else print("=") if (a==b) else print("b")

# find maximum no between 3 no 
a=10
b=20
c=30
print("the  a no is max") if a>b  and a>c else print("the  b no is max") if b>c  else print("c is max")  

# write a python program to take a no from user and cheak the no is multiple of 3 and 5 or only 3 or only 5 
no=int(input("enter a no :"))
if(no%3==0 and no%5==0):
    print("the no is multiple of 3 and 5 ")
elif(no%3==0):
    print("the no is multiple of 3")
elif(no%5==0):
    print("the no is multiple of 5")
else:
    print("the no is multiple of none of both")

# write a python program to check enter char vowel and consonent
a=input("enter a char:")
vowel="aeiouAEIOU"
if(a in vowel):
    print("it is a vowel")
else:
   print("it is a consonent ")
