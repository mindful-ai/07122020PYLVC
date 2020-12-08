# Write a program to create a multiplication table
# for the user input number

num = int(input("Enter a number: "))
print("Multiplication Table of", num)
for i in range(1, 11):
    print(num,"X",i,"=",num * i)
