f = open("pqr",'a')
d = f.write("welcome \n")
f.close()

#
f = open("new.txt",'a')
empl = input("enter a employee name:")
empl_id = input("enter aemployee id:")
emp_sal = input("enter a salary :")
d = f.write("\n"+"employee name is :"+empl+"\n")
d = f.write("employee id is :"+empl_id+'\n')
d= f.write("employee salary is :"+emp_sal)
f.close()
# write a program to merge conteint of 2 file and write in another file 
f = open("pqr",'r')
d = f.read()
f1 = open("new.txt",'r')
k = f1.read()
f3 = open("neww.txt",'a')
f3.write(d+k)
f.close()
f1.close()
f3.close()
# 
f1 = open("neww.txt",'r')
k = f1.read()
f3 =open("neww.txt",'a')
# l = f3.write(k)
t=k.replace('python','java')
l = f3.write(t)
f1.close()
f3.close()

# replace 2 word form user
f1 = open("neww.txt",'r')
k = f1.read()
inp1=input("enter a word u want to replace:")
inp2 = input("enter a word u want to replace with:")
f3 = open("neww.txt",'a')
t = k.replace(inp1 , inp2)
l = f3.write(t)
f1.close()
f3.close()
# use while loop 
f1 = open("lqr.txt",'a')
while(True):
    p=input("enter a data:")
    k = f1.write("\n"+p)
    user = input("enter u wnat to continue or stop (y/n):")
    if(user=='n'):
        break
f1.close()
