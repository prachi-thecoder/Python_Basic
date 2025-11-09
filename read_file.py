#copy a file content of 1 and print in another file
f = open("abc.txt",'r')
d = f.read()
# print(d)
f1 = open("write.txt",'w')
k = f1.write(d)
# print(k)
f.close()
f1.close()