Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> T = [100, 80, 60, 40, 0]
>>> F = []
>>> for t in T:
	F.append(t * 1.8 + 32)

	
>>> F
[212.0, 176.0, 140.0, 104.0, 32.0]
>>> 
>>> F1 = map(lambda t : t * 1.8 + 32, T)
>>> F1
<map object at 0x0000016F851D56D8>
>>> list(F1)
[212.0, 176.0, 140.0, 104.0, 32.0]
>>> 
>>> # An anonymous function -> lambda
>>> f = lambda x, y : x + y
>>> type(f)
<class 'function'>
>>> f(10, 20)
30
>>> f("apples", "pineapples")
'applespineapples'
>>> f([1,2,3], [4,5,6])
[1, 2, 3, 4, 5, 6]
>>> 
>>> 
>>> L = ["red", "green", "blue"]
>>> L.sort()
>>> L
['blue', 'green', 'red']
>>> L.sort(key=lambda s : s[-1])
>>> L
['red', 'blue', 'green']
>>> L.sort(key=lambda s : s[1])
>>> L
['red', 'blue', 'green']
>>> 
>>> 
>>> L.sort()
>>> L
['blue', 'green', 'red']
>>> L.sort(reverse=True)
>>> L
['red', 'green', 'blue']
>>> 
>>> 
>>> # -------------------------- filter
>>> 
>>> L = list(range(10, 100))
>>> L
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> 73
73
>>> 
>>> F
[212.0, 176.0, 140.0, 104.0, 32.0]
>>> F = []
>>> for n in L:
	if(int(str(n)[1]) + int(str(n)[0]) == 10):
		F.append(n)

		
>>> F
[19, 28, 37, 46, 55, 64, 73, 82, 91]
>>> 
>>> F1 = filter(lambda n : int(str(n)[1]) + int(str(n)[0]) == 10, L)
>>> F1
<filter object at 0x0000016F85269F98>
>>> list(F1)
[19, 28, 37, 46, 55, 64, 73, 82, 91]
>>> 
>>> 
>>> # --------------------------------------- packing and unpacking
>>> 
>>> T1 = ("Anil", "Sunil", "Kapil")
>>> T2 = ("Bangalore", "Hyderabad", "Mumbai")
>>> 
>>> T = zip(T1, T2)
>>> T
<zip object at 0x0000016F85203488>
>>> list(T)
[('Anil', 'Bangalore'), ('Sunil', 'Hyderabad'), ('Kapil', 'Mumbai')]
>>> dict(zip(T1, T2))
{'Anil': 'Bangalore', 'Sunil': 'Hyderabad', 'Kapil': 'Mumbai'}
>>> 
>>> D = {'Anil': 'Bangalore', 'Sunil': 'Hyderabad', 'Kapil': 'Mumbai'}
>>> D.keys()
dict_keys(['Anil', 'Sunil', 'Kapil'])
>>> D.values()
dict_values(['Bangalore', 'Hyderabad', 'Mumbai'])
>>> 
>>> 
>>> D.items()
dict_items([('Anil', 'Bangalore'), ('Sunil', 'Hyderabad'), ('Kapil', 'Mumbai')])
>>> 
>>> list(zip(*D.items()))
[('Anil', 'Sunil', 'Kapil'), ('Bangalore', 'Hyderabad', 'Mumbai')]
>>> 
>>> 
>>> # --------------------------------- reduce()
>>> 
>>> from functools import reduce
>>> L = [1, 2, 3, 4, 5]
>>> reduce(lambda a, b : a + b, L)
15
>>> # --------------------------------- Counter()
>>> 
>>> L = ["red", "red", "red", "green", "green", "blue"]
>>> D = {}
>>> for color in L:
	if color in D:
		D[color] = D[color] + 1
	else:
		D[color] = 1

		
>>> D
{'red': 3, 'green': 2, 'blue': 1}
>>> 
>>> from operator import Counter
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    from operator import Counter
ImportError: cannot import name 'Counter' from 'operator' (C:\Users\Purushotham\AppData\Local\Programs\Python\Python37\lib\operator.py)
>>> from itertools import Counter
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    from itertools import Counter
ImportError: cannot import name 'Counter' from 'itertools' (unknown location)
>>> from collections import Counter
>>> d = Counter(L)
>>> d
Counter({'red': 3, 'green': 2, 'blue': 1})
>>> 
>>> # ------------------------------------ permutations and combinations
>>> 
>>> s = "ABCD"
>>> 
>>> from itertools import permutations, combinations
>>> 
>>> permutations(s)
<itertools.permutations object at 0x0000016F85299728>
>>> list(permutations(s))
[('A', 'B', 'C', 'D'), ('A', 'B', 'D', 'C'), ('A', 'C', 'B', 'D'), ('A', 'C', 'D', 'B'), ('A', 'D', 'B', 'C'), ('A', 'D', 'C', 'B'), ('B', 'A', 'C', 'D'), ('B', 'A', 'D', 'C'), ('B', 'C', 'A', 'D'), ('B', 'C', 'D', 'A'), ('B', 'D', 'A', 'C'), ('B', 'D', 'C', 'A'), ('C', 'A', 'B', 'D'), ('C', 'A', 'D', 'B'), ('C', 'B', 'A', 'D'), ('C', 'B', 'D', 'A'), ('C', 'D', 'A', 'B'), ('C', 'D', 'B', 'A'), ('D', 'A', 'B', 'C'), ('D', 'A', 'C', 'B'), ('D', 'B', 'A', 'C'), ('D', 'B', 'C', 'A'), ('D', 'C', 'A', 'B'), ('D', 'C', 'B', 'A')]
>>> 
>>> s = "0123456789"
>>> list(permutations(s, 3))
[('0', '1', '2'), ('0', '1', '3'), ('0', '1', '4'), ('0', '1', '5'), ('0', '1', '6'), ('0', '1', '7'), ('0', '1', '8'), ('0', '1', '9'), ('0', '2', '1'), ('0', '2', '3'), ('0', '2', '4'), ('0', '2', '5'), ('0', '2', '6'), ('0', '2', '7'), ('0', '2', '8'), ('0', '2', '9'), ('0', '3', '1'), ('0', '3', '2'), ('0', '3', '4'), ('0', '3', '5'), ('0', '3', '6'), ('0', '3', '7'), ('0', '3', '8'), ('0', '3', '9'), ('0', '4', '1'), ('0', '4', '2'), ('0', '4', '3'), ('0', '4', '5'), ('0', '4', '6'), ('0', '4', '7'), ('0', '4', '8'), ('0', '4', '9'), ('0', '5', '1'), ('0', '5', '2'), ('0', '5', '3'), ('0', '5', '4'), ('0', '5', '6'), ('0', '5', '7'), ('0', '5', '8'), ('0', '5', '9'), ('0', '6', '1'), ('0', '6', '2'), ('0', '6', '3'), ('0', '6', '4'), ('0', '6', '5'), ('0', '6', '7'), ('0', '6', '8'), ('0', '6', '9'), ('0', '7', '1'), ('0', '7', '2'), ('0', '7', '3'), ('0', '7', '4'), ('0', '7', '5'), ('0', '7', '6'), ('0', '7', '8'), ('0', '7', '9'), ('0', '8', '1'), ('0', '8', '2'), ('0', '8', '3'), ('0', '8', '4'), ('0', '8', '5'), ('0', '8', '6'), ('0', '8', '7'), ('0', '8', '9'), ('0', '9', '1'), ('0', '9', '2'), ('0', '9', '3'), ('0', '9', '4'), ('0', '9', '5'), ('0', '9', '6'), ('0', '9', '7'), ('0', '9', '8'), ('1', '0', '2'), ('1', '0', '3'), ('1', '0', '4'), ('1', '0', '5'), ('1', '0', '6'), ('1', '0', '7'), ('1', '0', '8'), ('1', '0', '9'), ('1', '2', '0'), ('1', '2', '3'), ('1', '2', '4'), ('1', '2', '5'), ('1', '2', '6'), ('1', '2', '7'), ('1', '2', '8'), ('1', '2', '9'), ('1', '3', '0'), ('1', '3', '2'), ('1', '3', '4'), ('1', '3', '5'), ('1', '3', '6'), ('1', '3', '7'), ('1', '3', '8'), ('1', '3', '9'), ('1', '4', '0'), ('1', '4', '2'), ('1', '4', '3'), ('1', '4', '5'), ('1', '4', '6'), ('1', '4', '7'), ('1', '4', '8'), ('1', '4', '9'), ('1', '5', '0'), ('1', '5', '2'), ('1', '5', '3'), ('1', '5', '4'), ('1', '5', '6'), ('1', '5', '7'), ('1', '5', '8'), ('1', '5', '9'), ('1', '6', '0'), ('1', '6', '2'), ('1', '6', '3'), ('1', '6', '4'), ('1', '6', '5'), ('1', '6', '7'), ('1', '6', '8'), ('1', '6', '9'), ('1', '7', '0'), ('1', '7', '2'), ('1', '7', '3'), ('1', '7', '4'), ('1', '7', '5'), ('1', '7', '6'), ('1', '7', '8'), ('1', '7', '9'), ('1', '8', '0'), ('1', '8', '2'), ('1', '8', '3'), ('1', '8', '4'), ('1', '8', '5'), ('1', '8', '6'), ('1', '8', '7'), ('1', '8', '9'), ('1', '9', '0'), ('1', '9', '2'), ('1', '9', '3'), ('1', '9', '4'), ('1', '9', '5'), ('1', '9', '6'), ('1', '9', '7'), ('1', '9', '8'), ('2', '0', '1'), ('2', '0', '3'), ('2', '0', '4'), ('2', '0', '5'), ('2', '0', '6'), ('2', '0', '7'), ('2', '0', '8'), ('2', '0', '9'), ('2', '1', '0'), ('2', '1', '3'), ('2', '1', '4'), ('2', '1', '5'), ('2', '1', '6'), ('2', '1', '7'), ('2', '1', '8'), ('2', '1', '9'), ('2', '3', '0'), ('2', '3', '1'), ('2', '3', '4'), ('2', '3', '5'), ('2', '3', '6'), ('2', '3', '7'), ('2', '3', '8'), ('2', '3', '9'), ('2', '4', '0'), ('2', '4', '1'), ('2', '4', '3'), ('2', '4', '5'), ('2', '4', '6'), ('2', '4', '7'), ('2', '4', '8'), ('2', '4', '9'), ('2', '5', '0'), ('2', '5', '1'), ('2', '5', '3'), ('2', '5', '4'), ('2', '5', '6'), ('2', '5', '7'), ('2', '5', '8'), ('2', '5', '9'), ('2', '6', '0'), ('2', '6', '1'), ('2', '6', '3'), ('2', '6', '4'), ('2', '6', '5'), ('2', '6', '7'), ('2', '6', '8'), ('2', '6', '9'), ('2', '7', '0'), ('2', '7', '1'), ('2', '7', '3'), ('2', '7', '4'), ('2', '7', '5'), ('2', '7', '6'), ('2', '7', '8'), ('2', '7', '9'), ('2', '8', '0'), ('2', '8', '1'), ('2', '8', '3'), ('2', '8', '4'), ('2', '8', '5'), ('2', '8', '6'), ('2', '8', '7'), ('2', '8', '9'), ('2', '9', '0'), ('2', '9', '1'), ('2', '9', '3'), ('2', '9', '4'), ('2', '9', '5'), ('2', '9', '6'), ('2', '9', '7'), ('2', '9', '8'), ('3', '0', '1'), ('3', '0', '2'), ('3', '0', '4'), ('3', '0', '5'), ('3', '0', '6'), ('3', '0', '7'), ('3', '0', '8'), ('3', '0', '9'), ('3', '1', '0'), ('3', '1', '2'), ('3', '1', '4'), ('3', '1', '5'), ('3', '1', '6'), ('3', '1', '7'), ('3', '1', '8'), ('3', '1', '9'), ('3', '2', '0'), ('3', '2', '1'), ('3', '2', '4'), ('3', '2', '5'), ('3', '2', '6'), ('3', '2', '7'), ('3', '2', '8'), ('3', '2', '9'), ('3', '4', '0'), ('3', '4', '1'), ('3', '4', '2'), ('3', '4', '5'), ('3', '4', '6'), ('3', '4', '7'), ('3', '4', '8'), ('3', '4', '9'), ('3', '5', '0'), ('3', '5', '1'), ('3', '5', '2'), ('3', '5', '4'), ('3', '5', '6'), ('3', '5', '7'), ('3', '5', '8'), ('3', '5', '9'), ('3', '6', '0'), ('3', '6', '1'), ('3', '6', '2'), ('3', '6', '4'), ('3', '6', '5'), ('3', '6', '7'), ('3', '6', '8'), ('3', '6', '9'), ('3', '7', '0'), ('3', '7', '1'), ('3', '7', '2'), ('3', '7', '4'), ('3', '7', '5'), ('3', '7', '6'), ('3', '7', '8'), ('3', '7', '9'), ('3', '8', '0'), ('3', '8', '1'), ('3', '8', '2'), ('3', '8', '4'), ('3', '8', '5'), ('3', '8', '6'), ('3', '8', '7'), ('3', '8', '9'), ('3', '9', '0'), ('3', '9', '1'), ('3', '9', '2'), ('3', '9', '4'), ('3', '9', '5'), ('3', '9', '6'), ('3', '9', '7'), ('3', '9', '8'), ('4', '0', '1'), ('4', '0', '2'), ('4', '0', '3'), ('4', '0', '5'), ('4', '0', '6'), ('4', '0', '7'), ('4', '0', '8'), ('4', '0', '9'), ('4', '1', '0'), ('4', '1', '2'), ('4', '1', '3'), ('4', '1', '5'), ('4', '1', '6'), ('4', '1', '7'), ('4', '1', '8'), ('4', '1', '9'), ('4', '2', '0'), ('4', '2', '1'), ('4', '2', '3'), ('4', '2', '5'), ('4', '2', '6'), ('4', '2', '7'), ('4', '2', '8'), ('4', '2', '9'), ('4', '3', '0'), ('4', '3', '1'), ('4', '3', '2'), ('4', '3', '5'), ('4', '3', '6'), ('4', '3', '7'), ('4', '3', '8'), ('4', '3', '9'), ('4', '5', '0'), ('4', '5', '1'), ('4', '5', '2'), ('4', '5', '3'), ('4', '5', '6'), ('4', '5', '7'), ('4', '5', '8'), ('4', '5', '9'), ('4', '6', '0'), ('4', '6', '1'), ('4', '6', '2'), ('4', '6', '3'), ('4', '6', '5'), ('4', '6', '7'), ('4', '6', '8'), ('4', '6', '9'), ('4', '7', '0'), ('4', '7', '1'), ('4', '7', '2'), ('4', '7', '3'), ('4', '7', '5'), ('4', '7', '6'), ('4', '7', '8'), ('4', '7', '9'), ('4', '8', '0'), ('4', '8', '1'), ('4', '8', '2'), ('4', '8', '3'), ('4', '8', '5'), ('4', '8', '6'), ('4', '8', '7'), ('4', '8', '9'), ('4', '9', '0'), ('4', '9', '1'), ('4', '9', '2'), ('4', '9', '3'), ('4', '9', '5'), ('4', '9', '6'), ('4', '9', '7'), ('4', '9', '8'), ('5', '0', '1'), ('5', '0', '2'), ('5', '0', '3'), ('5', '0', '4'), ('5', '0', '6'), ('5', '0', '7'), ('5', '0', '8'), ('5', '0', '9'), ('5', '1', '0'), ('5', '1', '2'), ('5', '1', '3'), ('5', '1', '4'), ('5', '1', '6'), ('5', '1', '7'), ('5', '1', '8'), ('5', '1', '9'), ('5', '2', '0'), ('5', '2', '1'), ('5', '2', '3'), ('5', '2', '4'), ('5', '2', '6'), ('5', '2', '7'), ('5', '2', '8'), ('5', '2', '9'), ('5', '3', '0'), ('5', '3', '1'), ('5', '3', '2'), ('5', '3', '4'), ('5', '3', '6'), ('5', '3', '7'), ('5', '3', '8'), ('5', '3', '9'), ('5', '4', '0'), ('5', '4', '1'), ('5', '4', '2'), ('5', '4', '3'), ('5', '4', '6'), ('5', '4', '7'), ('5', '4', '8'), ('5', '4', '9'), ('5', '6', '0'), ('5', '6', '1'), ('5', '6', '2'), ('5', '6', '3'), ('5', '6', '4'), ('5', '6', '7'), ('5', '6', '8'), ('5', '6', '9'), ('5', '7', '0'), ('5', '7', '1'), ('5', '7', '2'), ('5', '7', '3'), ('5', '7', '4'), ('5', '7', '6'), ('5', '7', '8'), ('5', '7', '9'), ('5', '8', '0'), ('5', '8', '1'), ('5', '8', '2'), ('5', '8', '3'), ('5', '8', '4'), ('5', '8', '6'), ('5', '8', '7'), ('5', '8', '9'), ('5', '9', '0'), ('5', '9', '1'), ('5', '9', '2'), ('5', '9', '3'), ('5', '9', '4'), ('5', '9', '6'), ('5', '9', '7'), ('5', '9', '8'), ('6', '0', '1'), ('6', '0', '2'), ('6', '0', '3'), ('6', '0', '4'), ('6', '0', '5'), ('6', '0', '7'), ('6', '0', '8'), ('6', '0', '9'), ('6', '1', '0'), ('6', '1', '2'), ('6', '1', '3'), ('6', '1', '4'), ('6', '1', '5'), ('6', '1', '7'), ('6', '1', '8'), ('6', '1', '9'), ('6', '2', '0'), ('6', '2', '1'), ('6', '2', '3'), ('6', '2', '4'), ('6', '2', '5'), ('6', '2', '7'), ('6', '2', '8'), ('6', '2', '9'), ('6', '3', '0'), ('6', '3', '1'), ('6', '3', '2'), ('6', '3', '4'), ('6', '3', '5'), ('6', '3', '7'), ('6', '3', '8'), ('6', '3', '9'), ('6', '4', '0'), ('6', '4', '1'), ('6', '4', '2'), ('6', '4', '3'), ('6', '4', '5'), ('6', '4', '7'), ('6', '4', '8'), ('6', '4', '9'), ('6', '5', '0'), ('6', '5', '1'), ('6', '5', '2'), ('6', '5', '3'), ('6', '5', '4'), ('6', '5', '7'), ('6', '5', '8'), ('6', '5', '9'), ('6', '7', '0'), ('6', '7', '1'), ('6', '7', '2'), ('6', '7', '3'), ('6', '7', '4'), ('6', '7', '5'), ('6', '7', '8'), ('6', '7', '9'), ('6', '8', '0'), ('6', '8', '1'), ('6', '8', '2'), ('6', '8', '3'), ('6', '8', '4'), ('6', '8', '5'), ('6', '8', '7'), ('6', '8', '9'), ('6', '9', '0'), ('6', '9', '1'), ('6', '9', '2'), ('6', '9', '3'), ('6', '9', '4'), ('6', '9', '5'), ('6', '9', '7'), ('6', '9', '8'), ('7', '0', '1'), ('7', '0', '2'), ('7', '0', '3'), ('7', '0', '4'), ('7', '0', '5'), ('7', '0', '6'), ('7', '0', '8'), ('7', '0', '9'), ('7', '1', '0'), ('7', '1', '2'), ('7', '1', '3'), ('7', '1', '4'), ('7', '1', '5'), ('7', '1', '6'), ('7', '1', '8'), ('7', '1', '9'), ('7', '2', '0'), ('7', '2', '1'), ('7', '2', '3'), ('7', '2', '4'), ('7', '2', '5'), ('7', '2', '6'), ('7', '2', '8'), ('7', '2', '9'), ('7', '3', '0'), ('7', '3', '1'), ('7', '3', '2'), ('7', '3', '4'), ('7', '3', '5'), ('7', '3', '6'), ('7', '3', '8'), ('7', '3', '9'), ('7', '4', '0'), ('7', '4', '1'), ('7', '4', '2'), ('7', '4', '3'), ('7', '4', '5'), ('7', '4', '6'), ('7', '4', '8'), ('7', '4', '9'), ('7', '5', '0'), ('7', '5', '1'), ('7', '5', '2'), ('7', '5', '3'), ('7', '5', '4'), ('7', '5', '6'), ('7', '5', '8'), ('7', '5', '9'), ('7', '6', '0'), ('7', '6', '1'), ('7', '6', '2'), ('7', '6', '3'), ('7', '6', '4'), ('7', '6', '5'), ('7', '6', '8'), ('7', '6', '9'), ('7', '8', '0'), ('7', '8', '1'), ('7', '8', '2'), ('7', '8', '3'), ('7', '8', '4'), ('7', '8', '5'), ('7', '8', '6'), ('7', '8', '9'), ('7', '9', '0'), ('7', '9', '1'), ('7', '9', '2'), ('7', '9', '3'), ('7', '9', '4'), ('7', '9', '5'), ('7', '9', '6'), ('7', '9', '8'), ('8', '0', '1'), ('8', '0', '2'), ('8', '0', '3'), ('8', '0', '4'), ('8', '0', '5'), ('8', '0', '6'), ('8', '0', '7'), ('8', '0', '9'), ('8', '1', '0'), ('8', '1', '2'), ('8', '1', '3'), ('8', '1', '4'), ('8', '1', '5'), ('8', '1', '6'), ('8', '1', '7'), ('8', '1', '9'), ('8', '2', '0'), ('8', '2', '1'), ('8', '2', '3'), ('8', '2', '4'), ('8', '2', '5'), ('8', '2', '6'), ('8', '2', '7'), ('8', '2', '9'), ('8', '3', '0'), ('8', '3', '1'), ('8', '3', '2'), ('8', '3', '4'), ('8', '3', '5'), ('8', '3', '6'), ('8', '3', '7'), ('8', '3', '9'), ('8', '4', '0'), ('8', '4', '1'), ('8', '4', '2'), ('8', '4', '3'), ('8', '4', '5'), ('8', '4', '6'), ('8', '4', '7'), ('8', '4', '9'), ('8', '5', '0'), ('8', '5', '1'), ('8', '5', '2'), ('8', '5', '3'), ('8', '5', '4'), ('8', '5', '6'), ('8', '5', '7'), ('8', '5', '9'), ('8', '6', '0'), ('8', '6', '1'), ('8', '6', '2'), ('8', '6', '3'), ('8', '6', '4'), ('8', '6', '5'), ('8', '6', '7'), ('8', '6', '9'), ('8', '7', '0'), ('8', '7', '1'), ('8', '7', '2'), ('8', '7', '3'), ('8', '7', '4'), ('8', '7', '5'), ('8', '7', '6'), ('8', '7', '9'), ('8', '9', '0'), ('8', '9', '1'), ('8', '9', '2'), ('8', '9', '3'), ('8', '9', '4'), ('8', '9', '5'), ('8', '9', '6'), ('8', '9', '7'), ('9', '0', '1'), ('9', '0', '2'), ('9', '0', '3'), ('9', '0', '4'), ('9', '0', '5'), ('9', '0', '6'), ('9', '0', '7'), ('9', '0', '8'), ('9', '1', '0'), ('9', '1', '2'), ('9', '1', '3'), ('9', '1', '4'), ('9', '1', '5'), ('9', '1', '6'), ('9', '1', '7'), ('9', '1', '8'), ('9', '2', '0'), ('9', '2', '1'), ('9', '2', '3'), ('9', '2', '4'), ('9', '2', '5'), ('9', '2', '6'), ('9', '2', '7'), ('9', '2', '8'), ('9', '3', '0'), ('9', '3', '1'), ('9', '3', '2'), ('9', '3', '4'), ('9', '3', '5'), ('9', '3', '6'), ('9', '3', '7'), ('9', '3', '8'), ('9', '4', '0'), ('9', '4', '1'), ('9', '4', '2'), ('9', '4', '3'), ('9', '4', '5'), ('9', '4', '6'), ('9', '4', '7'), ('9', '4', '8'), ('9', '5', '0'), ('9', '5', '1'), ('9', '5', '2'), ('9', '5', '3'), ('9', '5', '4'), ('9', '5', '6'), ('9', '5', '7'), ('9', '5', '8'), ('9', '6', '0'), ('9', '6', '1'), ('9', '6', '2'), ('9', '6', '3'), ('9', '6', '4'), ('9', '6', '5'), ('9', '6', '7'), ('9', '6', '8'), ('9', '7', '0'), ('9', '7', '1'), ('9', '7', '2'), ('9', '7', '3'), ('9', '7', '4'), ('9', '7', '5'), ('9', '7', '6'), ('9', '7', '8'), ('9', '8', '0'), ('9', '8', '1'), ('9', '8', '2'), ('9', '8', '3'), ('9', '8', '4'), ('9', '8', '5'), ('9', '8', '6'), ('9', '8', '7')]
>>> passwords = []
>>> for p in list(permutations(s, 3)):
	passwords.append(''.join(p))

	
>>> passwords
['012', '013', '014', '015', '016', '017', '018', '019', '021', '023', '024', '025', '026', '027', '028', '029', '031', '032', '034', '035', '036', '037', '038', '039', '041', '042', '043', '045', '046', '047', '048', '049', '051', '052', '053', '054', '056', '057', '058', '059', '061', '062', '063', '064', '065', '067', '068', '069', '071', '072', '073', '074', '075', '076', '078', '079', '081', '082', '083', '084', '085', '086', '087', '089', '091', '092', '093', '094', '095', '096', '097', '098', '102', '103', '104', '105', '106', '107', '108', '109', '120', '123', '124', '125', '126', '127', '128', '129', '130', '132', '134', '135', '136', '137', '138', '139', '140', '142', '143', '145', '146', '147', '148', '149', '150', '152', '153', '154', '156', '157', '158', '159', '160', '162', '163', '164', '165', '167', '168', '169', '170', '172', '173', '174', '175', '176', '178', '179', '180', '182', '183', '184', '185', '186', '187', '189', '190', '192', '193', '194', '195', '196', '197', '198', '201', '203', '204', '205', '206', '207', '208', '209', '210', '213', '214', '215', '216', '217', '218', '219', '230', '231', '234', '235', '236', '237', '238', '239', '240', '241', '243', '245', '246', '247', '248', '249', '250', '251', '253', '254', '256', '257', '258', '259', '260', '261', '263', '264', '265', '267', '268', '269', '270', '271', '273', '274', '275', '276', '278', '279', '280', '281', '283', '284', '285', '286', '287', '289', '290', '291', '293', '294', '295', '296', '297', '298', '301', '302', '304', '305', '306', '307', '308', '309', '310', '312', '314', '315', '316', '317', '318', '319', '320', '321', '324', '325', '326', '327', '328', '329', '340', '341', '342', '345', '346', '347', '348', '349', '350', '351', '352', '354', '356', '357', '358', '359', '360', '361', '362', '364', '365', '367', '368', '369', '370', '371', '372', '374', '375', '376', '378', '379', '380', '381', '382', '384', '385', '386', '387', '389', '390', '391', '392', '394', '395', '396', '397', '398', '401', '402', '403', '405', '406', '407', '408', '409', '410', '412', '413', '415', '416', '417', '418', '419', '420', '421', '423', '425', '426', '427', '428', '429', '430', '431', '432', '435', '436', '437', '438', '439', '450', '451', '452', '453', '456', '457', '458', '459', '460', '461', '462', '463', '465', '467', '468', '469', '470', '471', '472', '473', '475', '476', '478', '479', '480', '481', '482', '483', '485', '486', '487', '489', '490', '491', '492', '493', '495', '496', '497', '498', '501', '502', '503', '504', '506', '507', '508', '509', '510', '512', '513', '514', '516', '517', '518', '519', '520', '521', '523', '524', '526', '527', '528', '529', '530', '531', '532', '534', '536', '537', '538', '539', '540', '541', '542', '543', '546', '547', '548', '549', '560', '561', '562', '563', '564', '567', '568', '569', '570', '571', '572', '573', '574', '576', '578', '579', '580', '581', '582', '583', '584', '586', '587', '589', '590', '591', '592', '593', '594', '596', '597', '598', '601', '602', '603', '604', '605', '607', '608', '609', '610', '612', '613', '614', '615', '617', '618', '619', '620', '621', '623', '624', '625', '627', '628', '629', '630', '631', '632', '634', '635', '637', '638', '639', '640', '641', '642', '643', '645', '647', '648', '649', '650', '651', '652', '653', '654', '657', '658', '659', '670', '671', '672', '673', '674', '675', '678', '679', '680', '681', '682', '683', '684', '685', '687', '689', '690', '691', '692', '693', '694', '695', '697', '698', '701', '702', '703', '704', '705', '706', '708', '709', '710', '712', '713', '714', '715', '716', '718', '719', '720', '721', '723', '724', '725', '726', '728', '729', '730', '731', '732', '734', '735', '736', '738', '739', '740', '741', '742', '743', '745', '746', '748', '749', '750', '751', '752', '753', '754', '756', '758', '759', '760', '761', '762', '763', '764', '765', '768', '769', '780', '781', '782', '783', '784', '785', '786', '789', '790', '791', '792', '793', '794', '795', '796', '798', '801', '802', '803', '804', '805', '806', '807', '809', '810', '812', '813', '814', '815', '816', '817', '819', '820', '821', '823', '824', '825', '826', '827', '829', '830', '831', '832', '834', '835', '836', '837', '839', '840', '841', '842', '843', '845', '846', '847', '849', '850', '851', '852', '853', '854', '856', '857', '859', '860', '861', '862', '863', '864', '865', '867', '869', '870', '871', '872', '873', '874', '875', '876', '879', '890', '891', '892', '893', '894', '895', '896', '897', '901', '902', '903', '904', '905', '906', '907', '908', '910', '912', '913', '914', '915', '916', '917', '918', '920', '921', '923', '924', '925', '926', '927', '928', '930', '931', '932', '934', '935', '936', '937', '938', '940', '941', '942', '943', '945', '946', '947', '948', '950', '951', '952', '953', '954', '956', '957', '958', '960', '961', '962', '963', '964', '965', '967', '968', '970', '971', '972', '973', '974', '975', '976', '978', '980', '981', '982', '983', '984', '985', '986', '987']
>>> s
'0123456789'
>>> pass = []
SyntaxError: invalid syntax
>>> passw = []
>>> for c in list(combinations(s, 3)):
	passw.append(''.join(c))

	
>>> passw
['012', '013', '014', '015', '016', '017', '018', '019', '023', '024', '025', '026', '027', '028', '029', '034', '035', '036', '037', '038', '039', '045', '046', '047', '048', '049', '056', '057', '058', '059', '067', '068', '069', '078', '079', '089', '123', '124', '125', '126', '127', '128', '129', '134', '135', '136', '137', '138', '139', '145', '146', '147', '148', '149', '156', '157', '158', '159', '167', '168', '169', '178', '179', '189', '234', '235', '236', '237', '238', '239', '245', '246', '247', '248', '249', '256', '257', '258', '259', '267', '268', '269', '278', '279', '289', '345', '346', '347', '348', '349', '356', '357', '358', '359', '367', '368', '369', '378', '379', '389', '456', '457', '458', '459', '467', '468', '469', '478', '479', '489', '567', '568', '569', '578', '579', '589', '678', '679', '689', '789']
>>> 
>>> 
>>> # ------------------------------------------ date and time
>>> 
>>> from datetime import datetime
>>> t = datetime.now()
>>> t
datetime.datetime(2020, 12, 10, 15, 39, 33, 3316)
>>> 
>>> t.year
2020
>>> type(t)
<class 'datetime.datetime'>
>>> t.month
12
>>> t.day
10
>>> t.minute
39
>>> t.hour
15
>>> t.second
33
>>> 
>>> # Thursday, 10 December 2020, 15:339:33
>>> def covert2format():
	pass

>>> t.strftime("%A")
'Thursday'
>>> f = "%A, %d %B %Y, %I:%M:%S %p"
>>> t.strftime(f)
'Thursday, 10 December 2020, 03:39:33 PM'
>>> type(f)
<class 'str'>
>>> 
>>> t1 = datetime.now()
>>> t1
datetime.datetime(2020, 12, 10, 15, 46, 46, 248583)
>>> 
>>> t1 - t
datetime.timedelta(seconds=433, microseconds=245267)
>>> 
>>> # -------------------------------------- comprehensions
>>> 
>>> 
>>> evens = []
>>> for i in range(100):
	if(i % 2 == 0):
		evens.append(i)

		
>>> evens
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
>>> 
>>> list(filter(lambda x : not x % 2, range(100)))
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
>>> 
>>> L = [x for x in range(100) if x % 2 == 0]
>>> L
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
>>> 
>>> 
>>> # [<expr> <loop> <condition>]
>>> 
>>> L = [(x, x**2, x**3) for x in range(1, 11)]
>>> L
[(1, 1, 1), (2, 4, 8), (3, 9, 27), (4, 16, 64), (5, 25, 125), (6, 36, 216), (7, 49, 343), (8, 64, 512), (9, 81, 729), (10, 100, 1000)]
>>> 
>>> L = ["red", "green", "blue"]
>>> T = ( i.capitalize() for i in L )
>>> T
<generator object <genexpr> at 0x0000016F85296840>
>>> list(T)
['Red', 'Green', 'Blue']
>>> 
>>> D = {s:len(s) for s in L}
>>> D
{'red': 3, 'green': 5, 'blue': 4}
>>> 
>>> N = [1, 2, 3, 4, 5, 6, 7]
>>> C1 = [x**2 for x in N if x % 3 == 0]
>>> C1
[9, 36]
>>> C2 = [x**2 if x % 3 == 0 else x for x in N]
>>> C2
[1, 2, 9, 4, 5, 36, 7]
>>> 
>>> 
>>> # -------------------------------------- any(), all()
>>> 
>>> L = [1, 2, 3, 5]
>>> any(L)
True
>>> L1 = [0, 0, 0, 1]
>>> any(L1)
True
>>> all(L1)
False
>>> all(L)
True
>>> 
>>> any([13 % i for i in range(2, 13)])
True
>>> T = [13 % i for i in range(2, 13)]
>>> T
[1, 1, 1, 3, 1, 6, 5, 4, 3, 2, 1]
>>> [12 % i for i in range(2, 12)]
[0, 0, 0, 2, 0, 5, 4, 3, 2, 1]
>>> all([12 % i for i in range(2, 12)])
False
>>> all([13 % i for i in range(2, 13)])
True
>>> 
>>> 
>>> N = 12
>>> all([12 % i for i in range(2, 12)])
False
>>> all([N % i for i in range(2, N)])
False
>>> N = 13
>>> all([N % i for i in range(2, N)])
True
>>> P = [N for N in range(1, 100) if all([N % i for i in range(2, N)])]
>>> P
[1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
>>> 