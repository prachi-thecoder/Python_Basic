a=int(input("enter a no:"))
b=int(input("enter a no:"))
print(a/b)
#
try:
    li=[1,2,3,4,5]
    print(li[6])
except:
    print("enter valid index")
print(li)
#
try:
    a=int(input("enter a no:"))
    b=int(input("enter a no:"))
    print(a/b)
except:
    print("enter valid no:")
print("end") 
# 
try:
    print(10/0)
except ArithmeticError:
    print("arithmatic")
except ZeroDivisionError:
    print("zero mode")
print("end")
# 

try:
    a=float(input("enter a no:"))
except Exception as e:
    print(type(e))
    print(e.__class__)
    print(e.__class__.__name__)
    print(e)
# 
# no exception
try:
    print("try")
except:
    print("except")
finally:
    print("finaly")
print("end")

#exception occur
try:
    print("try")
    print(10/0)
except:
    print("except")
finally:
    print("finaly")
print("end")
# 
# abnormal termination exception
try:
    print("try")
    print(10/0)
except ValueError:
    print("except")
finally:
    print("finally")
print("end")


# 1,3,4 abnormal termination exception
try:
    print("try")
    print(1/0)
except:
    print("error")
    print(1/0)
finally:
    print("finaly")
print("end")
# nested try except else finally block
try:
    print("statement 1")
    print("statement 2")
    print("statement 3")
    print("statement 4")
    try:
        print("statement 5")
        print("statement 6")
    except:
        print("statement 7")
    finally:
        print("statement 8")
    print("statement 9")
except:
    print("statement 10")
finally:
    print("statement 11")
print("statement 12")

#          
try:
    print("try")
    print(1/0)
except:
    print("except")
else:
    print("else")
finally:
    print("finally")
# for same try block you can take multiple except block but singally finally and else block
try:
    print("try")
finally:
    print("finally")
# 
try:
    print(1/0)
finally:
    print("finally")
# 
try:
    print("try")
else:
    print("else")
# 
try:
    print("try")
except:
    print("excepty")
try:
    pass
finally:
    print("finally")
# 


