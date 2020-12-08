def getFibo(n):
    F=[0,1]
    for i in range(1,n-1):
        F.insert(i+1,int(F[i-1])+int(F[i]))        
    return tuple(F)



def getfibo(n):
    F = []
    x = 0
    F.append(x)
    y = 1
    F.append(y)
    for i in range(n - 2):
        z = x + y
        F.append(z)
        x = y
        y = z
    return F

if __name__=="__main__":

    print(getfibo(9))
