# Get the water in Kilograms, initial & final temperature from the user:
water = float(input('Please Enter the water in Kilograms: '))
initialTemperature = float(input('Please Enter the initial temperature: '))
finalTemperature = float(input('Please Enter the final temperature: '))

Energy =  1.00 *(finalTemperature - initialTemperature ) * 4184


print("The Energy needed is = %.2f" %Energy)
