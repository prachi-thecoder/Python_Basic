# int(value) it convert value into int means typecast
print(int(10.3))
print(int(True))
# print(int(true))error
print(int(0b1111))
# print(int(10+5j))error
# print(int("abc"))error
print(int("11"))
# print(int("0b1111"))error
# print(int("10.5"))


print(float(10.3))
print(float(True))
# print(float(true))
print(float(0b1111))
# print(float(10+5j))
# print(float("abc"))
print(float("11"))
# print(float("0b1111"))
print(float(0xffff))
print(float("10.5"))


print(complex(10))
print(complex(True))
print(complex("10.5"))
print(complex(10.5))
# print(complex("0b1111"))
print(complex(10,20))
print(complex(10.5,20.5))
# print(complex("10","20"))
# print(complex("10",20))


print(bool(10))
print(bool(0))
print(bool(-10))
print(bool(10.5))
print(bool(0.0))
print(bool(0.01))
print(bool(10+5j))
print(bool(0+0j))
print(bool("abc"))
print(bool(''))
print(bool(" "))
s="subscribe"
# print(s)
print(s[4:5])


# str(value) it convert given value in the string
# a= 10
a=str(0x1111)
print(type(a))
print(a)
a=str(0b1111)
print(type(a))
a=str(0o1111)
print(type(a))
print(a)
a=str(True)
print(type(a))
print(a)

# hex(int value)it convert given value into hexadecimal string
hex(15)
print (float.hex(15.1))

# bin(int value)it convert given value into binary string
bin(15)
print (bin(15))

# oct(int value)it convert given vlaue into octal string
oct(15)
print (oct(15))

# charcter to decimal 
a='p'
print("decimal value of charcter is:",ord(a))


# 
a= 65
print(chr(8364))
