# Program to check if a number is prime or not

# Input

n = int(input("Enter a number: "))

# Process

prime = True
for i in range(2, n):
    if(n % i == 0):
        prime = False
        break
    
# Output

if(prime): #if(prime == True):
    print("The number is prime")
else:
    print("The number is not prime")
