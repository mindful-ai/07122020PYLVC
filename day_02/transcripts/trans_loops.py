Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = "python"
>>> L = ["red", "green", "blue"]
>>> S = set("aeoiu")
>>> D = {"name":"manoj", "age":35, "country": "India"}
>>> 
>>> 
>>> for ch in s:
	print(ch)

	
p
y
t
h
o
n
>>> for item in L:
	print(item.upper())

	
RED
GREEN
BLUE
>>> S
{'e', 'o', 'u', 'i', 'a'}
>>> for i in S:
	print(i, end=' ')

	
e o u i a 
>>> D
{'name': 'manoj', 'age': 35, 'country': 'India'}
>>> for k in D:
	print(k)

	
name
age
country
>>> for v in D.values():
	print(v)

	
manoj
35
India
>>> 
>>> for i in D.items():
	print(i)

	
('name', 'manoj')
('age', 35)
('country', 'India')
>>> 
>>> 
>>> # ----------------
>>> 
>>> 
>>> D
{'name': 'manoj', 'age': 35, 'country': 'India'}
>>> newD = {}
>>> 
>>> for k, v in D.items():
	print(k + " ----> " + str(v))

	
name ----> manoj
age ----> 35
country ----> India
>>> for k, v in D.items():
	newD.setdefault(v, k)

	
'name'
'age'
'country'
>>> newD
{'manoj': 'name', 35: 'age', 'India': 'country'}
>>> 
>>> 
>>> D
{'name': 'manoj', 'age': 35, 'country': 'India'}
>>> D.setdefault("company", "oracle")
'oracle'
>>> D
{'name': 'manoj', 'age': 35, 'country': 'India', 'company': 'oracle'}
>>> 
>>> 
>>> # ----------------------
>>> 
>>> N = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> 
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(10, 20))
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> list(range(10, 20, 2))
[10, 12, 14, 16, 18]
>>> 
KeyboardInterrupt
>>> list(range(20, 10, -1))
[20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
>>> 
>>> 
>>> print( str(5) + ' X ' + str(1) + ' = ' + str(5 * 1))
5 X 1 = 5
>>> for i in range(1, 11):
	print( str(5) + ' X ' + str(1) + ' = ' + str(5 * 1))

	
5 X 1 = 5
5 X 1 = 5
5 X 1 = 5
5 X 1 = 5
5 X 1 = 5
5 X 1 = 5
5 X 1 = 5
5 X 1 = 5
5 X 1 = 5
5 X 1 = 5
>>> for i in range(1, 11):
	print( str(5) + ' X ' + str(i) + ' = ' + str(5 * i))

	
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50
>>> print( 5 + ' X ' + str(1) + ' = ' + str(5 * 1))
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    print( 5 + ' X ' + str(1) + ' = ' + str(5 * 1))
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> print( str(5) + ' X ' + str(1) + ' = ' + str(5 * 1))
5 X 1 = 5
>>> 
===== RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/labs/lab_02.py =====
Enter a number: 4
Multiplication Table of 4
4 X 1 = 4
4 X 2 = 8
4 X 3 = 12
4 X 4 = 16
4 X 5 = 20
4 X 6 = 24
4 X 7 = 28
4 X 8 = 32
4 X 9 = 36
4 X 10 = 40
>>> 
>>> 
>>> # ------------------- Multiplication table with while loop
>>> 
>>> i = 1
>>> while i <= 10:
	print( str(5) + ' X ' + str(i) + ' = ' + str(5 * i))
	i = i + 1

	
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50
>>> 
>>> # ------------------------ Loop control statements
>>> 
>>> s = "computer"
>>> for c in s:
	print(c, end=" " )

	
c o m p u t e r 
>>> 
>>> for c in s:
	if(c == 'p'):
		break
	print(c, end=" ")

	
c o m 
>>> for c in s:
	if(c == 'p'):
		continue
	print(c, end=" ")

	
c o m u t e r 
>>> 
===== RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/primes.py =====
Enter a number: 5
The number is prime
>>> 
===== RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/primes.py =====
Enter a number: 4
The number is not prime
>>> 
===== RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/primes.py =====
Enter a number: 2
The number is prime
>>> 
===== RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/primes.py =====
Enter a number: 1
The number is prime
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/primes-pythonic.py 
Enter a number: 5
The number is prime
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/primes-pythonic.py 
Enter a number: 4
The number is not prime
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/primes-pythonic.py 
Enter a number: 2
The number is prime
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/primes-pythonic.py 
Enter a number: 1
The number is prime
>>> print('-'*60)
------------------------------------------------------------
>>> 
==== RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/primes-.py ====
Enter your numbers (q to quit)
# 12
# 34
# 45
# 56
# 67
# 78
# 89
# sdfg
# sfghb
# bxzcvb
# a
# qt
# *&^%
# 234
# 1.2.
# 4
# 5
# 6
# 7
# q
------------------------------------------------------------
You have entered the following numbers: 
[12, 34, 45, 56, 67, 78, 89, 234, 4, 5, 6, 7]
>>> 
==== RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/primes-.py ====
Enter your numbers (q to quit)
# 12
# 32
# 435
# 56
# 67
# 78
# 45
# 435
# 3
# 4
# 345
# gdsf
# 
# fgb
# b
# 
# 
# sdfg
# cxvb
# 5
# 
# 36
