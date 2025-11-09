# is use to execute some code only if the file was run directly and not imported
def f1():
    print("f1")
if __name__ ==  "__main__":
    print(dir())
    print(__name__)
    a=input("enter a name:")
    print(a)
# stand alone
    f1()