Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> import os.path
>>> import shutil
>>> 
>>> # --- check where you are
>>> os.getcwd()
'C:\\Users\\Purushotham\\AppData\\Local\\Programs\\Python\\Python37'
>>> path = "C:\Users\Purushotham\Desktop\oracle\day_03\data"
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> path = "c:\text\read\next\unique\data.dat"
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 17-18: truncated \uXXXX escape
>>> path = "c:\text\read\next\znique\data.dat"
>>> print(path)
c:	extead
ext\znique\data.dat
>>> path = r"c:\text\read\next\znique\data.dat"
>>> print(path)
c:\text\read\next\znique\data.dat
>>> path = r"C:\Users\Purushotham\Desktop\oracle\day_03\data"
>>> os.chdir(path)
>>> os.getcwd()
'C:\\Users\\Purushotham\\Desktop\\oracle\\day_03\\data'
>>> 
>>> 
>>> # ---------------- to create directories as per the extensions
>>> 
>>> os.listdir(path)
['data1.txt', 'road.jpg', 'sunflower.jpg']
>>> files = os.listdir(path)
>>> files
['data1.txt', 'road.jpg', 'sunflower.jpg']
>>> 
>>> files[0]
'data1.txt'
>>> os.splitext(files[0])
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    os.splitext(files[0])
AttributeError: module 'os' has no attribute 'splitext'
>>> os.path.splitext(files[0])
('data1', '.txt')
>>> os.path.splitext(files[0])[1]
'.txt'
>>> os.path.splitext(files[0])[1][1:]
'txt'
>>> exts = []
>>> for file in files:
	exts.append(os.path.splitext(file)[1][1:])

	
>>> exts
['txt', 'jpg', 'jpg']
>>> set(exts)
{'txt', 'jpg'}
>>> for ext in set(exts):
	os.mkdir(ext)

	
>>> # move the files
>>> files
['data1.txt', 'road.jpg', 'sunflower.jpg']
>>> os.listdir()
['data1.txt', 'jpg', 'road.jpg', 'sunflower.jpg', 'txt']
>>> 
>>> 
>>> for file in files:
	newdir = os.path.splitext(file)[1][1:]
	dest = os.path.join(os.getcwd(), newdir, file)
	shutil.move(file, dest)

	
'C:\\Users\\Purushotham\\Desktop\\oracle\\day_03\\data\\txt\\data1.txt'
'C:\\Users\\Purushotham\\Desktop\\oracle\\day_03\\data\\jpg\\road.jpg'
'C:\\Users\\Purushotham\\Desktop\\oracle\\day_03\\data\\jpg\\sunflower.jpg'
>>> 
>>> 
>>> os.getcwd()
'C:\\Users\\Purushotham\\Desktop\\oracle\\day_03\\data'
>>> newdir
'jpg'
>>> file
'sunflower.jpg'
>>> os.path.join(os.getcwd(), newdir, file)
'C:\\Users\\Purushotham\\Desktop\\oracle\\day_03\\data\\jpg\\sunflower.jpg'
>>> type(newdir)
<class 'str'>
>>> os.getcwd() + "\\" + newdir + "\\" + file
'C:\\Users\\Purushotham\\Desktop\\oracle\\day_03\\data\\jpg\\sunflower.jpg'
>>> 
>>> 
>>> 

>>> # ---------------------------------------------------
>>> 
>>> 
>>> 
>>> 
