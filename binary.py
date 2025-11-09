# for binary file we use .bin,.dat  
with open("example.bin",'wb')as f:
    f.write(b"hello world")
# 
with open('example.bin','rb')as f:
    k=f.read()
    print(k)
# 
with open('example.bin','ab')as f:
    f.write(b"append text")
    # f.seek(0)
    # print(f.read())
# 
with open('example.bin','+ab')as f:
    f.write(b"append text")
    f.seek(0)
    print(f.read())
# 
with open('example.bin','+wb')as f:
    f.write(b"append text with write")
    print(f.read())
# 
with open('example.bin','+rb')as f:
    print(f.read())
    f.write(b"append text using read ")
    f.seek(0)
    print(f.read())
# 
with open('2.jpeg','rb')as f:
    p=f.read()
    print(p)
with open('new.jpeg','wb')as f:
    a=f.write(p)    
# 

