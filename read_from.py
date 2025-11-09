# file handling
# readline use for 1st line read 
f = open('abc.txt','r')
d=f.readline(2)     #in braces if we give 2 it means compiler will read only 2 charcter 
print(d)
# print(f.readline(5))  
# p=f.readline()    # this line give defaultly /n
# print(p)
f.close()

# for reading multiple lines
f = open('abc.txt','r')
d=f.readlines()     #in braces if we give 2 it means compiler will read only 2 charcter 
print(d)
# print(f.readline(5))  
# p=f.readline()    # this line give defaultly /n
# print(p)
f.close()

#write a program to count no of line in a given txt file 
f = open('abc.txt','r')
d=f.readlines()
print(len(d))
f.close()
# to read a 7th line 
f = open('abc.txt','r')
d=f.readlines()
print(d[6])
f.close()


