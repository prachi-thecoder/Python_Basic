# syntax
if(condition):
    print("if")
elif(condition):
    print("elif1")
elif(condition):
    print("elif2")
else:
    print("else")
# eg
if(True):
    print("if")
elif(True):
    print("elif1")
elif(True):
    print("elif2")
else:
    print("else")
# leap year
year=int(input("enter a year:"))
if(year%4==0 and year%100!=0):
    print("this is leap year")
# elif(year!%100):
    #  print("this is leap year")
elif(year%400==0):
    print("this is leap year")
else:
    print("this is not leap year")

#a store gives a discount on the membership status and the amount spent mamber spending over rs 10k get a 10% dis ,non member spending over 15k get a 5% dis and allother get no dis
amt=int(input("enter your amount:"))
member=input("you are a member or not(yes/no) :")
if(member == "yes" or member == "Yes"  and amt>=10000 ):
    dis=amt*10/100
    print("the discount is :",amt-dis)
elif( member == "no" or member == "No" and  amt>=15000):
    dis=amt*5/100
    print("the discount is :",amt-dis)
else:
    print("no discount for this value")

# a bank introduce and intensive policy of giving bonus to all acount holder the policy is as follow a bonus of 2% of balance is given to everyone.
# and bonus of 5% to women if there balance is more the 5k  and a bonus of 3% to men if there  balance if more the 10k accept the balance from ,gender ,and calculate a bonus 
gender=input("enter your gender (women/men)")
balance=int(input("enter your balance:"))
if(gender=="women" or gender=="women" and balance>=5000):
    print("the discount is ",(balance*0.05)+balance)
elif(gender=="men" or gender=="Men" and balance>=10000):
    print("the discount is ",(balance*0.03)+balance)
else:
    print("the balcne is ",balance*0.02)

# and electric power distribution company charges are as follows for 0-200unit rs 0.5 unit for 201-400 unit 3rs per unit +100rs
# 401 - 600 unit 4rs perunit +200 for 600 and above unit 6rsperunit +300rs
unit=int(input("enter your unit:"))
if(unit>=0 and unit<=200):
    total=unit*0.5
    print("the total unit is :",total)
elif(unit>=201 and unit<=400):
    total=unit*3+100
    print("the total unit is:",total)
elif(unit>401 and unit<=600):
    total=unit*4+200
    print("total is ",total)
elif(unit<=600):
    total=unit*6+300
# 
  