# Program to manage a data list


# ------------------------------- Core Dev Team

L = []

'''
L1 = []
L2 = []
L3 = []


L = [ [], [], [], [] ]
D = { 'name':[], 'age':[] }
UD = {}

'''
def listAdd(obj, pos = -1): # listAdd(3, 4), listAdd(2, 3)
    try:
        if(pos >= 0 and pos < len(L)):
            L.insert(pos, obj)
            return True
        elif(pos == -1):
            L.append(obj)
            return True
        else:
            return False
    except:
        return "Exception"

def listRem(obj, pos = -1): # pos = -1
    if(pos >= 0 and pos < len(L)):
        L.pop(pos)
        return True
    elif(pos == -1):
        L.remove(obj)
        return True
    else:
        return False

def listFind(obj):
    T = []
    for index in range(0, len(L)):
        if(L[index] == obj):
            T.append(index)
    return tuple(T)

def listClr():
    L = []

def listGet():
    return tuple(L)

def listSize():
    return len(L)


# ------------------------ Test/Application code

import random

if __name__ == "__main__":

    # Populating the list with few random numbers
    for i in range(20):
        listAdd(random.randint(1, 100))
        
    listAdd(11, 1)
    listAdd(22, 2)
    listAdd(33, 3)

    print(listAdd(44, -4))
    

    # Print the list
    print(listGet())

    # Remove 1, 2
    print(listRem(11))
    print(listRem(22, 1))
        
    # Print the list
    print(listGet())

    # Finding 55
    for i in range(5):
        index = random.randint(0, listSize())
        listAdd(55, index)
        
    # Print the list
    print(listGet())
    print("Number of 55s in the list: ", len(listFind(55)))
