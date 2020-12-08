Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L = ["red", "green", "blue"]
>>> L[1] = "yellow"
>>> L
['red', 'yellow', 'blue']
>>> T = ("red", "green", "blue")
>>> T[1] = "yellow"
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    T[1] = "yellow"
TypeError: 'tuple' object does not support item assignment
>>> type(T)
<class 'tuple'>
>>> 
>>> # --------------------------- rearranging elements
>>> 
>>> sorted(T)
['blue', 'green', 'red']
>>> T.sort()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    T.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> reversed(T)
<reversed object at 0x00000216F17D5550>
>>> tuple(reversed(T))
('blue', 'green', 'red')
>>> T.reverse()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    T.reverse()
AttributeError: 'tuple' object has no attribute 'reverse'
>>> 
>>> # ------------------------ searching
>>> 
>>> "red" in T
True
>>> T.count("red")
1
>>> T.index("red")
0
>>> 
>>> # ----------------------- note the usage here
>>> 
>>> T
('red', 'green', 'blue')
>>> L
['red', 'yellow', 'blue']
>>> 
>>> r, g, b = T
>>> r
'red'
>>> g
'green'
>>> b
'blue'
>>> type(r)
<class 'str'>
>>> type(T)
<class 'tuple'>
>>> 
>>> 
>>> r,g = T
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    r,g = T
ValueError: too many values to unpack (expected 2)
>>> r, g, *x = T
>>> r
'red'
>>> g
'green'
>>> x
['blue']
>>> r, g, *x = ("red", "Greeb", "yellow", "golden", "orange", "brown")
>>> r
'red'
>>> g
'Greeb'
>>> x
['yellow', 'golden', 'orange', 'brown']
>>> type(x)
<class 'list'>
>>> 
