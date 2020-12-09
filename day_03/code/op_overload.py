class complex(object):
    def __init__(self, x=0, y=0):
        self.real = x
        self.img = y

    
    def __str__(self):
        return str(self.real) + " + j" + str(self.img)
    

    # c1 complex(3, 4) => 3 + j4
    # c2 complex(4, 5) => 4 + j5
    # c1 + c2 X no allowed
    # Overload __add__ to make it happen
    # c3 = c1 + c2 => self -> c1, other -> c2

    
    def __add__(self, other):   
        newreal = self.real + other.real
        newimg = self.img + other.img
        return complex(newreal, newimg)

    def __sub__(self, other):   
        newreal = self.real - other.real
        newimg = self.img - other.img
        return complex(newreal, newimg)
    

c1 = complex(3, 4)
c2 = complex(4, 5)
print(c1)
print(c2)

c3 = c1 + c2
print(c3)

c4 = c1 - c3
print(c4)