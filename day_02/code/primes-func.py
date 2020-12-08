# Program to collect several numbers from the user
# Then separate the prime numbers from them

def checkprime(n):
    for i in range(2, n):
        if(n % i == 0):
            return False
    else:
        return True

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

# Process

primes = []
for item in data:
    '''
    for i in range(2, item):
        if(item % i == 0):
            break
    else:
        primes.append(item)
    '''
    if(checkprime(item)):
        primes.append(item)
        
# Output

print('-'*60)
print("Extracted prime numbers: ")
print(primes)
