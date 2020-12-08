Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L = ["Ram", 35, "Bangalore", "India", "Oracle"]
>>> L[0]
'Ram'
>>> D = {"name":"Ram", "age":35, "Place":"Bangalore", "Country":"India", "Company":"Oracle"}
>>> D
{'name': 'Ram', 'age': 35, 'Place': 'Bangalore', 'Country': 'India', 'Company': 'Oracle'}
>>> D["name"]
'Ram'
>>> D["age"]
35
>>> 
>>> # ---------------------- adding and removeing elements
>>> 
>>> D["salary"]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    D["salary"]
KeyError: 'salary'
>>> D["salary"] = "1000000"
>>> D
{'name': 'Ram', 'age': 35, 'Place': 'Bangalore', 'Country': 'India', 'Company': 'Oracle', 'salary': '1000000'}
>>> D.setdefault("name")
'Ram'
>>> D["name"]
'Ram'
>>> D.setdefault("dob", "23-12-1998")
'23-12-1998'
>>> D
{'name': 'Ram', 'age': 35, 'Place': 'Bangalore', 'Country': 'India', 'Company': 'Oracle', 'salary': '1000000', 'dob': '23-12-1998'}
>>> # D["dob"] = "23-12-1998"
>>> 
>>> D.pop("age")
35
>>> D
{'name': 'Ram', 'Place': 'Bangalore', 'Country': 'India', 'Company': 'Oracle', 'salary': '1000000', 'dob': '23-12-1998'}
>>> 
>>> 
>>> # --------------------------------- keys and values
>>> 
>>> D.keys()
dict_keys(['name', 'Place', 'Country', 'Company', 'salary', 'dob'])
>>> D.values()
dict_values(['Ram', 'Bangalore', 'India', 'Oracle', '1000000', '23-12-1998'])
>>> D.items()
dict_items([('name', 'Ram'), ('Place', 'Bangalore'), ('Country', 'India'), ('Company', 'Oracle'), ('salary', '1000000'), ('dob', '23-12-1998')])
>>> 
>>> 
>>> # --------------------------- searching
>>> 
>>> "name" in D
True
>>> "rank" in D
False
>>> 
>>> 
>>> # ---------------------------- updating
>>> 
>>> D1 = {"Addr":"4th Cross, 13th Main, J P Nagar", "hobbies" : "cricket" }
>>> D.update(D1)
>>> D
{'name': 'Ram', 'Place': 'Bangalore', 'Country': 'India', 'Company': 'Oracle', 'salary': '1000000', 'dob': '23-12-1998', 'Addr': '4th Cross, 13th Main, J P Nagar', 'hobbies': 'cricket'}
>>> 
