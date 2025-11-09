class example:
    def __init__(self):
        print("object is created")
    def __del__(self):
        print("object is destroyed")
d = example()
print("end")

# 
import time
class example:
    def __init__(self):
        print("obj is created")
    def __del__(self):
        print("obj is destroyed")
        
e1 = example()
e2 = e1
e3 = e2
e4 = e3
del e1
print("e1 is distroyed")
time.sleep(5)
del e2
print("e2 is distroyed")