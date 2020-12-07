Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = "python"
>>> type(s)
<class 'str'>
>>> 
>>> 
>>> type(s) == "<class 'str'>"
False
>>> type(s) == 'str'
False
>>> type(s)
<class 'str'>
>>> t = type(s)
>>> t
<class 'str'>
>>> type(s) = t
SyntaxError: can't assign to function call
>>> type(s) == t
True
>>> type(t)
<class 'type'>
>>> # ------------------------------------ immutable nature of strings
>>> 
>>> s
'python'
>>> s[0]
'p'
>>> s[1]
'y'
>>> s[-1]
'n'
>>> s[-2]
'o'
>>> 
>>> s[0] = 'j'
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    s[0] = 'j'
TypeError: 'str' object does not support item assignment
>>> s = 'jython'
>>> s
'jython'
>>> s[0] = 'p'
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    s[0] = 'p'
TypeError: 'str' object does not support item assignment
>>> 
>>> 
>>> # ------------------------------------- subscripting
>>> 
>>> s
'jython'
>>> s = 'python'
>>> 
>>> 
>>> s[0]
'p'
>>> s[-1]
'n'
>>> s[1:3]
'yt'
>>> s[1:4]
'yth'
>>> s[-5:-2]
'yth'
>>> s[1:6]
'ython'
>>> s[1:6:2]
'yhn'
>>> 
>>> 
>>> 
>>> s[0:4]
'pyth'
>>> s[:4]
'pyth'
>>> s[2:6]
'thon'
>>> s[2:]
'thon'
>>> s[:]
'python'
>>> s[::2]
'pto'
>>> s[::-1]
'nohtyp'
>>> 
>>> 
>>> # ------------------------------------- Operators
>>> 
>>> 'hello' + 'world'
'helloworld'
>>> 'hello' * 3
'hellohellohello'
>>> len(s)
6
>>> 'py' in s
True
>>> 'app' in s
False
>>> del s
>>> s
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> 
>>> # --------------------------------------- string functions
>>> 
>>> # ------------- case
>>> 
>>> 
>>> s
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> s = "python"
>>> s
'python'
>>> s.upper()
'PYTHON'
>>> s.lower()
'python'
>>> s.capitalize()
'Python'
>>> 
>>> 
>>> # ----------------------- querying
>>> 
>>> s
'python'
>>> s.isalpha()
True
>>> s.isdigit()
False
>>> '878'.isdigit()
True
>>> '7632shdj'.isdigit()
False
>>> '7632shdj'.isalpha()
False
>>> '7632shdj'.isalnum()
True
>>> ' '.ispace()
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    ' '.ispace()
AttributeError: 'str' object has no attribute 'ispace'
>>> ' '.isspace()
True
>>> s
'python'
>>> s.islower()
True
>>> s.isupper()
False
>>> s = 'Python'
>>> s.islower()
False
>>> s.upper()
'PYTHON'
>>> s = 'Python'
>>> s.isupper()
False
>>> 
>>> 
>>> 
>>> site = "www.google.com"
>>> site.startswith('https')
False
>>> site.endswith('com')
True
>>> 
>>> 
>>> spc = '&^%'
>>> spc.isdigit()
False
>>> spc.isalnum()
False
>>> 
>>> 
>>> # ------------------------------ searching
>>> 
>>> s
'Python'
>>> s.find('t')
2
>>> s.count('t')
1
>>> 't' in s
True
>>> 
>>> # ------------------------------- modifying
>>> 
>>> ip = '192-168-1-1'
>>> ip[3]
'-'
>>> ip[3]='.'
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    ip[3]='.'
TypeError: 'str' object does not support item assignment
>>> 
>>> 
>>> ip.replace('-', '.')
'192.168.1.1'
>>> ip
'192-168-1-1'
>>> newip = ip.replace('-', '.')
>>> ip
'192-168-1-1'
>>> newip
'192.168.1.1'
>>> 
>>> amount = '12,34,786'
>>> int(amount)
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    int(amount)
ValueError: invalid literal for int() with base 10: '12,34,786'
>>> amount.replace(',','')
'1234786'
>>> int(amount.replace(',','')) * 0.15 + int(amount.replace(',',''))
1420003.9
>>> 
>>> 
>>> 
>>> 
>>> data = '   1232354  '
>>> int(data)
1232354
>>> len(data)
12
>>> data.strip()
'1232354'
>>> data.lstrip()
'1232354  '
>>> data.rstrip()
'   1232354'
>>> 
>>> 
>>> 
>>> data
'   1232354  '
>>> 
>>> 
>>> 
>>> text = '28092020LVC'
>>> text.ljust(20)
'28092020LVC         '
>>> text.rjust(20, '<')
'<<<<<<<<<28092020LVC'
>>> 
>>> 
>>> 
>>> 
>>> t = 'This is a python live virtual class'
>>> t.split()
['This', 'is', 'a', 'python', 'live', 'virtual', 'class']
>>> t.split('a')
['This is ', ' python live virtu', 'l cl', 'ss']
>>> 
>>> 
>>> L = ['This', 'is', 'a', 'python', 'live', 'virtual', 'class']
>>> '-'.join(L)
'This-is-a-python-live-virtual-class'
>>> 
>>> 
>>> # ------------------------------- iteration
>>> 
>>> for c in 'python':
	print(c)

	
p
y
t
h
o
n
>>> for c in 'python':
	print(c.upper())

	
P
Y
T
H
O
N
>>> for c in 'python':
	print(c.upper(), end=' ')

	
P Y T H O N 
>>> 
>>> 
>>> text = "The first version requires that numerator and denominator are instances of numbers.Rational and returns a new Fraction instance with value numerator/denominator. If denominator is 0, it raises a ZeroDivisionError. The second version requires that other_fraction is an instance of numbers.Rational and returns a Fraction instance with the same value. The next two versions accept either a float or a decimal.Decimal instance, and return a Fraction instance with exactly the same value. Note that due to the usual issues with binary floating-point (see Floating Point Arithmetic: Issues and Limitations), the argument to Fraction(1.1) is not exactly equal to 11/10, and so Fraction(1.1) does not return Fraction(11, 10) as one might expect. (But see the documentation for the limit_denominator() method below.) "
>>> 
>>> 
>>> text
'The first version requires that numerator and denominator are instances of numbers.Rational and returns a new Fraction instance with value numerator/denominator. If denominator is 0, it raises a ZeroDivisionError. The second version requires that other_fraction is an instance of numbers.Rational and returns a Fraction instance with the same value. The next two versions accept either a float or a decimal.Decimal instance, and return a Fraction instance with exactly the same value. Note that due to the usual issues with binary floating-point (see Floating Point Arithmetic: Issues and Limitations), the argument to Fraction(1.1) is not exactly equal to 11/10, and so Fraction(1.1) does not return Fraction(11, 10) as one might expect. (But see the documentation for the limit_denominator() method below.) '
>>> 
>>> len(text.split())
119
>>> 
