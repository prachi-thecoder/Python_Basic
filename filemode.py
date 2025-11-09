f = open("neww.txt",'r+')
print(f.read())
f.write("python")
print(f.tell())         #it return a current postion
print("------------------------")
f.seek(0)          #set filepointer at specefic position
print(f.read())
f.close()
# 
f = open("neww.txt",'w+')
f.write("python")
print(f.read())
# print(f.tell())         #it return a current postion
print("------------------------")
f.seek(0)          #set filepointer at specefic position
print(f.read())
f.close()
# 
f = open("neww.txt",'a+')
print(f.read())
f.write("py")
# print(f.tell())         #it return a current postion
print("------------------------")
f.seek(0)          #set filepointer at specefic position
print(f.read())
f.close()

# x mode it will create a file if it is not exist and after execution avoid creation of duplicate files
f= open("prachii.txt",'x')
