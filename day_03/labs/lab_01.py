
class datalist(object):

    # Data
    def __init__(self):
        self.L = []

    # Functions

    def __str__(self):
        return str(self.L)


    def listAdd(self, dataitem, pos = -1): # listAdd(3, 4), listAdd(2, 3)
        #print("Current Position: " + str(pos))
        try:
            if(pos >= 0 and pos < len(self.L)):
                self.L.insert(pos, dataitem)
                return True
            elif(pos == -1):
                self.L.append(dataitem)
                return True
            else:
                return False
        except:
            return "Exception"

    def listRem(obj, pos = -1): # pos = -1
        pass

    def listFind(obj):
        pass

    def listClr():
        pass

    def listGet():
        pass

    def listSize():
        pass


# ------------------------------ Test code
import random

if __name__ == "__main__":

    '''
    d1 = datalist();
    for i in range(20):
        d1.listAdd(random.randint(1, 100), i - 1)
    
    print(d1)

    d2 = datalist();
    for i in range(20):
        d2.listAdd(random.randint(1, 100))
    
    print(d1)

    d3 = datalist();
    for i in range(20):
        d3.listAdd(random.randint(1, 100))
    
    print(d3)
    '''

    objs = []
    n = 1
    for i in range(100):
        obj = datalist()
        for i in range(10):
            obj.listAdd(n)
        objs.append(obj)
        n += 1

    for obj in objs:
        print(obj)