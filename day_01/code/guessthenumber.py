# Program to guess a randomly selected number

import random

# Input

# Generate a random number
rn = random.randint(1, 10)

# Pick one number from the user asking him to guess
print("The computer picked a random number between 1 and 10")
un = int(input("Guess?? "))

# Processing

# Check if the user guessed the correct number

# Output

# Print the result

if(rn == un):
    print("You guessed correctly")
else:
    print("Sorry! Better luck next time")



        

