Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Numbers
>>> 
>>> a = 10
>>> type(a)
<class 'int'>
>>> a = 10.2
>>> type(a)
<class 'float'>
>>> 
>>> a = 10
>>> b = 3
>>> 
>>> # ------------------------- Operators
>>> 
>>> # Arithmetic operators
>>> 
>>> a + b
13
>>> a - b
7
>>> a * b
30
>>> a / b
3.3333333333333335
>>> a % b
1
>>> a ** b
1000
>>> 
>>> a//b
3
>>> 
>>> # Relational operators
>>> 
>>> a > b
True
>>> a < b
False
>>> a >= b # Is a greater than or equal to b?
True
>>> a <= b
False
>>> a != b
True
>>> a == b * 5
False
>>> (a - b * 7) == ( b - a * 5)
False
>>> a
10
>>> b
3
>>> # 49? -11?
>>> (a - b * 7)
-11
>>> 
>>> 
>>> # ----------------------------- Logical operators
>>> 
>>> a
10
>>> b
3
>>> (a - b > 6) or (b - a != 10)
True
>>> (a - b > 6) and (b - a != 10)
True
>>> (a - b < 6) and (b - a != 10)
False
>>> not(a - b < 6) and (b - a != 10)
True
>>> 
>>> a++
SyntaxError: invalid syntax
>>> a += 1
>>> a
11
>>> 
>>> # -------------------------------------------------
>>> 
>>> # ---------------------------------- Functions in-built
>>> 
>>> a
11
>>> a = 100
>>> int(a)
100
>>> a = '100'
>>> type(a)
<class 'str'>
>>> a + 10
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a + 10
TypeError: can only concatenate str (not "int") to str
>>> int(a) + 10
110
>>> b = '123.45'
>>> int(b) + 4
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    int(b) + 4
ValueError: invalid literal for int() with base 10: '123.45'
>>> float(a) + 10
110.0
>>> c = "345..dsf"
>>> int(c)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    int(c)
ValueError: invalid literal for int() with base 10: '345..dsf'
>>> float(c)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    float(c)
ValueError: could not convert string to float: '345..dsf'
>>> a = 100
>>> hex(a)
'0x64'
>>> bin(a)
'0b1100100'
>>> oct(a)
'0o144'
>>> 
>>> v = '0x64'
>>> int(v)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    int(v)
ValueError: invalid literal for int() with base 10: '0x64'
>>> int(v, 16)
100
>>> a
100
>>> a - b
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    a - b
TypeError: unsupported operand type(s) for -: 'int' and 'str'
>>> b = 7
>>> a - b
93
>>> b - a
-93
>>> abs(a - b)
93
>>> abs(b - a)
93
>>> a = 100
>>> str(a)
'100'
>>> n = 1101011
>>> type(n)
<class 'int'>
>>> int(n)
1101011
>>> int(n, 2)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    int(n, 2)
TypeError: int() can't convert non-string with explicit base
>>> int(str(n), 2)
107
>>> bin(107)
'0b1101011'
>>> 
>>> 
>>> # ----------------------------------- Modules
>>> 
>>> 
>>> ang = 90
>>> sin(ang)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    sin(ang)
NameError: name 'sin' is not defined
>>> import math
>>> sin(ang)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    sin(ang)
NameError: name 'sin' is not defined
>>> math.sin(ang)
0.8939966636005579
>>> math.sin(ang * 3.14/180)
0.9999996829318346
>>> math.sin(ang * 3.14159/180)
0.9999999999991198
>>> math.sin(ang * math.pi/180)
1.0
>>> math.sin(math.radians(90))
1.0
>>> import random
>>> random.randint(1, 100)
10
>>> random.randint(1, 100)
54
>>> random.randint(1, 100)
22
>>> random.randint(1, 100)
45
>>> random.randint(1, 100)
87
>>> 
