# homework
# letter pattern 
for i in range(7):
    for j in range(7-i):
        print("*",end=" ")
    print()
for i in range(2):
    for j in range(i+5):
        print("*",end=" ")
    print()

    
#pattern of k letter
# * * * * * * * 
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# *
# * *
# * * * 
# * * * *
# * * * * *
# * * * * * *
# * * * * * * *
for i in range(7):
    for j in range(7-i):
        print("*",end=" ")
    print()
for i in range(7):
    for j in range(i+1):
        print("*",end=" ")
    print()

# ******
# *    *    
# ******
# *
# *

# * 
# *
# *
# *
# *
# *
# *
# * * * *
for i in range(8):
    print("*",end=" ")
    for j in range(i-6):
        print("*" ,end=" ")

        for j in range(i-6):
            print("*" ,end=" ")
        for i in range(6):
            print("*",end=" ")
    # for i in range(1):
    #     print("*",end="")
    print()


    # 
for i in range(8):
    print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()

    # 
for i in range(8):
    print("*",end="")
    # for k in range(8-i):
    #     print(" ",end=" ")
    for j in range(i-2):
        print("*",end="")
print("  ")
for i in range(8):
    print("*",end="")
    print()