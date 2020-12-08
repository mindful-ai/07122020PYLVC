# Program to check if a number is prime or not
# PYTHONIC way!!

# Input

n = int(input("Enter a number: "))

# Process
# Using the loop else block -> compatible with for and while

for i in range(2, n):
    if(n % i == 0):
        print("The number is not prime")
        break
else:
    print("The number is prime")

    
