#Get the total from the user:
subtotal = float(input("Enter the subtotal:"))

gratuity = float(input("Enter the gratuity:"))

total=gratuity + subtotal* 0.15
bills= gratuity + subtotal
gratuity =0.15* bills
total = gratuity + bills


print( "gratuity: $", gratuity);
print( "total : $",total);

