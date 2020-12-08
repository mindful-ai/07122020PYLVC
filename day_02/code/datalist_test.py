#import datalist as dl
#from datalist import listAdd, listGet

from datalist import *


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
