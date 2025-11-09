 D:\html> python   
Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> pqr = 10
>>> pqr
10
>>> a_b_c = 10
>>> a_b_c
10  
>>> 1abc=10
  File "<python-input-5>", line 1
    1abc=10
    ^
SyntaxError: invalid decimal literal
>>> abc123 = 10
>>> abc123
10
>>> #abc = 10
>>> if = 21
  File "<python-input-9>", line 1
    if = 21
       ^
SyntaxError: invalid syntax
>>> IF = 20
>>> _x = 20
>>> _x
20
>>> __x = 20
>>> __x 
20
>>> __x__ = 20
>>> __x__
20
>>> a=b=c=10
>>> a
10
>>> b
10
>>> c
10
>>> import keyword
>>> keyword kwlist
  File "<python-input-22>", line 1
    keyword kwlist
            ^^^^^^
SyntaxError: invalid syntax
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> a = 10
>>> type(a)
<class 'int'>
>>>  a = -10
  File "<python-input-26>", line 1
    a = -10
IndentationError: unexpected indent
>>> type(a)
<class 'int'>
>>> a = 0b1111
>>> type(a)
<class 'int'>
>>> a = 0x1111
>>> type(a)
<class 'int'>
>>> b=10.3
>>> type(b)
<class 'float'>
>>> b = -10.324
>>> type(b)
<class 'float'>
# >>> b = 1.23e^2
#   File "<python-input-36>", line 1
#     b = 1.23e^2
#            ^
# SyntaxError: invalid decimal literal
# >>> b = 1.2e^2
#   File "<python-input-37>", line 1
#     b = 1.2e^2
#           ^
# SyntaxError: invalid decimal literal
# >>> b = 1.2
# >>> b = 1.2e
#   File "<python-input-39>", line 1
#     b = 1.2e
#           ^
# SyntaxError: invalid decimal literal
# >>> a = 3+2i
#   File "<python-input-40>", line 1
#     a = 3+2i
          ^
SyntaxError: invalid decimal literal
>>> a = 3+2j
>>> type(a)
<class 'complex'>
>>> 3+j2
Traceback (most recent call last):
  File "<python-input-43>", line 1, in <module>
    3+j2
      ^^
NameError: name 'j2' is not defined
>>> a.real
3.0
>>> a.img
Traceback (most recent call last):
  File "<python-input-45>", line 1, in <module>
    a.img
AttributeError: 'complex' object has no attribute 'img'. Did you mean: 'imag'?
>>> a.imag
2.0
# >>> a= 0b1111j
#   File "<python-input-47>", line 1
#     a= 0b1111j
#             ^
# SyntaxError: invalid binary literal
# >>> a = 0b11112j
#   File "<python-input-48>", line 1
#     a = 0b11112j
              ^
SyntaxError: invalid digit '2' in binary literal
>>> a= 0b1111+2j
>>> a = ox1111+2j
Traceback (most recent call last):
  File "<python-input-50>", line 1, in <module>
    a = ox1111+2j
        ^^^^^^
NameError: name 'ox1111' is not defined
>>> 2+ob1111j
Traceback (most recent call last):
  File "<python-input-51>", line 1, in <module>
    2+ob1111j
      ^^^^^^^
NameError: name 'ob1111j' is not defined
>>> a = 3+3j
>>> b = 2+2j
>>> a+b
(5+5j)
>>> a-b
(1+1j)
>>> a*b
12j
>>> a/b
(1.5+0j)
>>> a = True
>>> type(a)
<class 'bool'>
>>> True+True
2
>>> True/False
Traceback (most recent call last):
  File "<python-input-61>", line 1, in <module>
    True/False
    ~~~~^~~~~~
ZeroDivisionError: division by zero
>>> 0==True
False
>>> 99*False
0
>>> 99/True
99.0
>>> 0/1
0.0
>>> 