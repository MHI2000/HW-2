# Get the integer number from the user:

number = int(input("Please Enter  number between 0 and 1000: "))
sum = 0

while(number > 0):
    dog = number % 10
    sum = sum + dog
    number = number //10

print(" The Sum of the digits is = %d" %sum)
