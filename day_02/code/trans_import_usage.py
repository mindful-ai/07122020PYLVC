Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import datalist
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import datalist
ModuleNotFoundError: No module named 'datalist'
>>> import os
>>> os.chdir(r"C:\Users\Purushotham\Desktop\oracle\day_02\code")
>>> import datalist
>>> datalist.listAdd(10)
True
>>> datalist.getList()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    datalist.getList()
AttributeError: module 'datalist' has no attribute 'getList'
>>> datalist.listGet()
(10,)
>>> # ---------------------------
>>> 
>>> import datalist
>>> datalist.listAdd(12)
True
>>> datalist.listGet()
(10, 12)
>>> 
>>> import datalist as d
>>> d.listAdd(13, 1)
True
>>> d.listGet()
(10, 13, 12)
>>> listGet()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    listGet()
NameError: name 'listGet' is not defined
>>> 
>>> from datalist import listGet
>>> listGet
<function listGet at 0x00000232822ED598>
>>> listGet()
(10, 13, 12)
>>> 
>>> 
>>> from datalist import *
>>> listFind(13)
(1,)
>>> 
