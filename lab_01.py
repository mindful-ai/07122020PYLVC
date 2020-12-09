class datalist(object):

    # Data
    def __init__(self):
        self.L = []

    # Functions
    def listAdd(obj, pos = -1): # listAdd(3, 4), listAdd(2, 3)
        pass

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

if __name__ == "__main__":

    d1 = datalist();
    for i in range(20):
        d1.listAdd(random.randint(1, 100))
    
    print(d1)

    d2 = datalist();
    for i in range(20):
        d2.listAdd(random.randint(1, 100))
    
    print(d1)

    d3 = datalist();
    for i in range(20):
        d3.listAdd(random.randint(1, 100))
    
    print(d3)