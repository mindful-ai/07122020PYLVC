# Program to collect several number from the user
# Print the maximum, minimum, average and extract the prime numbers

import primes_lib

print('-'*20 + "New Project")
print("primes-reuse.py" + " ---> " + str(__name__))

# Inputs

data = []
print("Enter your numbers (q to quit)")
while True:
    uin = input("# ")
    if(uin.lower() == 'q'):
        break
    elif(uin.isdigit()):
        data.append(int(uin))

print('-'*60)
print("You have entered the following numbers: ")
print(data)

# Processing

primes  = []

maximum = max(data)
minimum = min(data)
average = sum(data) / len(data)
for item in data:
    if(primes_lib.checkprime(item)):
        primes.append(item)

# Output

print('-'*60)
print("MAXIMUM  :", maximum)
print("MINIMUM  :", minimum)
print("AVERAGE  :", average)
print("PRIMES   :", primes)
