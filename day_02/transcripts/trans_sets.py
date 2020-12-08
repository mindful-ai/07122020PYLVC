Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s1 = {'a', 'a', 'b', 'b', 'c' ,'d', 'e', 'f', 'g' }
>>> type(s1)
<class 'set'>
>>> s1
{'f', 'c', 'a', 'g', 'b', 'd', 'e'}
>>> s1[2]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    s1[2]
TypeError: 'set' object is not subscriptable
>>> 'a' in s1
True
>>> s2 = set("defghijk")
>>> s2
{'f', 'g', 'h', 'i', 'j', 'k', 'd', 'e'}
>>> # ----------------------------- operators
>>> 
>>> s1 ^ s2
{'c', 'b', 'a', 'h', 'i', 'j', 'k'}
>>> s1 & s2
{'e', 'd', 'g', 'f'}
>>> s1 | s2
{'i', 'f', 'c', 'g', 'a', 'h', 'b', 'j', 'k', 'd', 'e'}
>>> 
>>> # ---------------------------- adding and removing
>>> 
>>> s1.add("x")
>>> s1
{'f', 'c', 'a', 'g', 'x', 'b', 'd', 'e'}
>>> s3 = {'y', 'z'}
>>> s1.update(s3)
>>> s1
{'f', 'c', 'y', 'a', 'g', 'x', 'z', 'b', 'd', 'e'}
>>> 
>>> s1.remove('g')
>>> s1
{'f', 'c', 'y', 'a', 'x', 'z', 'b', 'd', 'e'}
>>> 
>>> # ---------------------------- functions
>>> 
>>> s1.union(s2)
{'i', 'f', 'y', 'e', 'a', 'x', 'g', 'z', 'b', 'h', 'k', 'j', 'd', 'c'}
>>> s1.intersection(s2)
{'d', 'e', 'f'}
>>> 
>>> 
>>> # -------------------------------- interconversion
>>> 
>>> s1
{'f', 'c', 'y', 'a', 'x', 'z', 'b', 'd', 'e'}
>>> list(s1)
['f', 'c', 'y', 'a', 'x', 'z', 'b', 'd', 'e']
>>> tuple(s1)
('f', 'c', 'y', 'a', 'x', 'z', 'b', 'd', 'e')
>>> 
