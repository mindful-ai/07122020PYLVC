Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L = [12, 13.5, "red", 'blue', 'gree', True, False, [1, 2, 3]]
>>> L
[12, 13.5, 'red', 'blue', 'gree', True, False, [1, 2, 3]]
>>> # ---------------------------- mutability
>>> L[4]
'gree'
>>> L[4] = 'green'
>>> L
[12, 13.5, 'red', 'blue', 'green', True, False, [1, 2, 3]]
>>> 
>>> L[4]
'green'
>>> L[4][0] = 'G'
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    L[4][0] = 'G'
TypeError: 'str' object does not support item assignment
>>> L[-1]
[1, 2, 3]
>>> L[-1][2] = 5
>>> L
[12, 13.5, 'red', 'blue', 'green', True, False, [1, 2, 5]]
>>> 
>>> # -------------------------- indexing and subscripting
>>> 
>>> L[0]
12
>>> L[1]
13.5
>>> L[-1]
[1, 2, 5]
>>> l[2:5]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    l[2:5]
NameError: name 'l' is not defined
>>> L[2:5]
['red', 'blue', 'green']
>>> L[:]
[12, 13.5, 'red', 'blue', 'green', True, False, [1, 2, 5]]
>>> L[::2]
[12, 'red', 'green', False]
>>> L[::-1]
[[1, 2, 5], False, True, 'green', 'blue', 'red', 13.5, 12]
>>> 
>>> 
>>> # ---------------------------- Operators
>>> 
>>> ['a', 'b'] + ['c', 'd']
['a', 'b', 'c', 'd']
>>> ['a', 'b'] + 'hello'
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    ['a', 'b'] + 'hello'
TypeError: can only concatenate list (not "str") to list
>>> ['a', 'b'] * 4
['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']
>>> len(L)
8
>>> 'red' in L
True
>>> del L[3]
>>> L
[12, 13.5, 'red', 'green', True, False, [1, 2, 5]]
>>> del L
>>> L
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    L
NameError: name 'L' is not defined
>>> 
>>> 
>>> # ------------------- some behaviour to understand
>>> 
>>> L = ["red", "green", "blue"]
>>> L[1]
'green'
>>> L[1] = 'purple'
>>> L
['red', 'purple', 'blue']
>>> L[1] = ['black' 'white']
>>> L
['red', ['blackwhite'], 'blue']
>>> L[1] = ['black', 'white']
>>> L
['red', ['black', 'white'], 'blue']
>>> 
>>> 
>>> L = ["red", "green", "blue"]
>>> L[1:2]
['green']
>>> L[1:2] = ['black', 'white']
>>> L
['red', 'black', 'white', 'blue']
>>> 
>>> 
>>> L = ["red", "green", "blue"]
>>> L
['red', 'green', 'blue']
>>> ip = "10.10.1.2"
>>> # 2.10.10.1
>>> 
>>> 
>>> L = ip.split('.')
>>> L
['10', '10', '1', '2']
>>> L[-1] + L[:-1]
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    L[-1] + L[:-1]
TypeError: can only concatenate str (not "list") to str
>>> L[-1] + L[:2]
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    L[-1] + L[:2]
TypeError: can only concatenate str (not "list") to str
>>> L
['10', '10', '1', '2']
>>> L[-1]
'2'
>>> L[:2]
['10', '10']
>>> L[:3]
['10', '10', '1']
>>> L
['10', '10', '1', '2']
>>> L[3:]
['2']
>>> L[3:] + L[:3]
['2', '10', '10', '1']
>>> '.'.join(L[3:] + L[:3])
'2.10.10.1'
>>> '.'.join(L[3:] + L[:3]).replace("10", "1")
'2.1.1.1'
>>> 
>>> 
>>> # --------------------------- FUnctions
>>> 
>>> L
['10', '10', '1', '2']
>>> L = ["red", "green", "blue"]
>>> 
>>> 
>>> # --- Add elements
>>> 
>>> L.append("purple")
>>> L
['red', 'green', 'blue', 'purple']
>>> L.append("grey")
>>> L
['red', 'green', 'blue', 'purple', 'grey']
>>> L + ['white')
SyntaxError: invalid syntax
>>> L + ['white']
['red', 'green', 'blue', 'purple', 'grey', 'white']
>>> L.insert(1, "yellow")
>>> L
['red', 'yellow', 'green', 'blue', 'purple', 'grey']
>>> 
>>> L1 = ['golden', 'orange', 'brown']
>>> L + L1
['red', 'yellow', 'green', 'blue', 'purple', 'grey', 'golden', 'orange', 'brown']
>>> L
['red', 'yellow', 'green', 'blue', 'purple', 'grey']
>>> L.extend(L1)
>>> L
['red', 'yellow', 'green', 'blue', 'purple', 'grey', 'golden', 'orange', 'brown']
>>> L + ['black']
['red', 'yellow', 'green', 'blue', 'purple', 'grey', 'golden', 'orange', 'brown', 'black']
>>> L
['red', 'yellow', 'green', 'blue', 'purple', 'grey', 'golden', 'orange', 'brown']
>>> L = L + ['black'] # L.append('black')
>>> L
['red', 'yellow', 'green', 'blue', 'purple', 'grey', 'golden', 'orange', 'brown', 'black']
>>> 
>>> 
>>> # ------ remove elements
>>> 
>>> L
['red', 'yellow', 'green', 'blue', 'purple', 'grey', 'golden', 'orange', 'brown', 'black']
>>> L.pop()
'black'
>>> L
['red', 'yellow', 'green', 'blue', 'purple', 'grey', 'golden', 'orange', 'brown']
>>> L.pop()
'brown'
>>> L.pop(1)
'yellow'
>>> L
['red', 'green', 'blue', 'purple', 'grey', 'golden', 'orange']
>>> 'purple' in L
True
>>> L.remove('purple')
>>> L
['red', 'green', 'blue', 'grey', 'golden', 'orange']
>>> 
>>> 
>>> # >>>>>>>>>>>>>>>> RAshmi
>>> 
>>> L
['red', 'green', 'blue', 'grey', 'golden', 'orange']
>>> L = ['red', 'green', 'blue', 'grey', ['golden', 'orange']]
>>> L[-1]
['golden', 'orange']
>>> L[-1].insert(0, 'yellow')
>>> L
['red', 'green', 'blue', 'grey', ['yellow', 'golden', 'orange']]
>>> type(L[-1])
<class 'list'>
>>> d = type(L[-1])
>>> d
<class 'list'>
>>> type(d)
<class 'type'>
>>> d == 'list'
False
>>> 
>>> # >>>>>>>>>>>>>>>>>>>>>>>>
>>> 
>>> # ------------------------- re-arrange elements
>>> 
>>> L
['red', 'green', 'blue', 'grey', ['yellow', 'golden', 'orange']]
>>> L.pop()
['yellow', 'golden', 'orange']
>>> L
['red', 'green', 'blue', 'grey']
>>> sorted(L)
['blue', 'green', 'grey', 'red']
>>> L
['red', 'green', 'blue', 'grey']
>>> sorted(L)
['blue', 'green', 'grey', 'red']
>>> L.sort()
>>> L
['blue', 'green', 'grey', 'red']
>>> 
>>> 
>>> L
['blue', 'green', 'grey', 'red']
>>> reversed(L)
<list_reverseiterator object at 0x000001730B16A7B8>
>>> list(reversed(L))
['red', 'grey', 'green', 'blue']
>>> L
['blue', 'green', 'grey', 'red']
>>> L.reverse()
>>> L
['red', 'grey', 'green', 'blue']
>>> 
>>> 
>>> # ----------------- searching
>>> 
>>> L.index("red")
0
>>> L.index("black")
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    L.index("black")
ValueError: 'black' is not in list
>>> "black" in L
False
>>> 
>>> 
>>> L
['red', 'grey', 'green', 'blue']
>>> L.append("red")
>>> L.count("red")
2
>>> s = "mississippi"
>>> s.count('s')
4
>>> s.find('s')
2
>>> 
