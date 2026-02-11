print("----------------Tip Bill Calculator----------------")

# To calculate the amount of the bill in hotel.
# Get the total bill, then add tip to the bill, then split it between the friends and 
# calculator amount to be paid by each person.

print('Welcome to "The Grand"')

bill = float(input("How much is the total bill? $"))
split = int(input("How many people to split the bill? "))
tip_choose = input("Would you like to give tip? Type 'Y' for yes and 'N' for no: ").capitalize()
if tip_choose == "Y":
    tip = int(input("How much tip would you like to add? 10, 12 or 15%? ")) 
    amount = (bill/split)*((tip/100)+1)
else:
    amount = (bill/split)
amount = "{:.2f}".format(amount)
print(f"Each person should pay ${amount}.")