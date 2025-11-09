operand=input("enter your operand :")
var1=int(input("enter a input no :"))
var2= int (input("enter a input 2nd no:"))
if(operand=="+"):
    add=var1+var2
    print("the addition is as follows:",add)
elif(operand=="-"):
    sub=var1-var2
    print("the substraction is as follows:",sub)
elif(operand=="*"):
    mult=var1*var2
    print("the multiplication is as follows:",mult)
elif(operand=="/"):
    div=var1/var2
    print("the division is as follow:",div)
elif(operand=="%"):
    mod=var1%ar2
    print("the module is as follow:",mod)
elif(operand=="//"):
    floor=var1//var2
    print("the floor is as follow:",floor)
elif(operand=="**"):
    exp=var1**ar2
    print("the exponentiation is as follow:",exp)
elif(operand=="&"):
    bitwise_and=var1&var2
    print("the bitwise and is as follow",bitwise_and)
elif(operand=="|"):
    bitwise_or=var1|var2
    print("the bitwise or is as follow",bitwise_or)
elif(operand=="^"):
    bitwise_xor=var1^var2
    print("the bitwise xor is as follow",bitwise_xor)
# elif(operand=="~"):
#     bitwise_not=var1~var2
#     print("the bitwise not is as follow",bitwise_not)
elif(operand==">>"):
    right_shift=var1>>var2
    print("the right shift as follows:",right_shift)
elif(operand=="<<"):
    left_shift=var1<<var2
    print("the leftshit is as follow:",left_shift)

