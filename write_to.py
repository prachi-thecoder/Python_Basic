# write mode
f = open('1.txt','w')
f.write("welcome")
f.close()
# for multilines 
f = open('1.txt','w')
f.writelines(["welcome to write mode\n","prachi"])
f.close()

# accept info from user and write into a file
k= input("enter a file name:")
f = open(k,'w')
p = input("enter a line:")
l = input("enter a line:")
# f.writelines([p])
f.write(p+"\n")
f.write(l)
f.close()
