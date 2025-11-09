#if statement syntax
if (condition):
    print("statement 1")
print("statement 2")   

#write a python program to take SP and CP from user and check if the shopkeeper get a profit or loss and print amt after profit and loss
a=int(input("Enter SP"))
b=int(input("Enter CP")) 
if (a>b):
    print("profit")
    print(a-b)
if (a<b):
   print("loss")    
   print(a-b)

#write a python program to entered number is in between 1500 to 2100 if yes then print given no is between the condition
a=int(input("Enter a number"))
if a>=1500 and  a<=2100:
    print("Yes the number is between given range")

# write a python program to calculate absolute value:
a=int(input("enter a value :"))
if a<0 :
    print(-a)

#if else statement syntax
if (condition):
    print("statement 1")
else:   
    print("statement 2")   

#write a python program to check candidate are elegible or not
a=int(input("enter age :"))
if(a>=18) :
    print("you are eligible")
else:
    print("you are not eligible")

#write a python program to check shape given is rectangle or square
l=int(input("enter length :"))
b=int(input("enter breadth :"))
if l==b:
    print("It is a square")
else:
    print("It is a rectangle")

#write a python program to 

