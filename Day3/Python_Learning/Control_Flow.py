kaarthi = int(input("Enter your number: "))
print("The number you entered is: ", kaarthi)
if kaarthi > 0:
    print("The number is positive.")
elif kaarthi < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

    amount = float(input("Enter the amount: "))
    print("The amount you entered is: ", amount)
if amount < 30:
    print("You can have tea.")   
elif amount < 50:
    print("You can have coffee.")
else:
    print("You can have both tea and coffee.")