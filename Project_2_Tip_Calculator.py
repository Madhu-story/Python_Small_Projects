print("----------------Tip Bill Calculator----------------")

# To calculate the amount of the bill in hotel.
# Get the total bill, then add tip to the bill, then split it between the friends and 
# calculator amount to be paid by each person.

print('Welcome to "The Grand"')

bill = float(input("How much is the total bill? $"))
split = int(input("How many people to split the bill? "))
tip_choose = input("Would you like to give tip? Type 'Y' for yes and 'N' for no: ").capitalize()


if tip_choose == "Y" and split != 0:
    tip = int(input("How much tip would you like to add? 10, 12, 15 or customize the tip percentage? ")) 
    amount = (bill/split)*((tip/100)+1)

elif tip_choose == "Y" and split == 0:
    tip = int(input("How much tip would you like to add? 10, 12, 15 or customize the tip percentage? "))
    amount = bill * ((tip/100)+1)  

elif tip_choose == "N" and split != 0:
    amount = (bill/split)

else:
    amount = bill
   
amount = "{:.2f}".format(amount)
print()
print("------------Your Bill Status----------------")
print(f"Total amount: ${bill}")
if tip_choose == "Y":
    print(f"Tip: {tip}%")
if split != 0:
    print(f"Bill is split among: {split}")
    print(f"Each person pays ${amount}.")
else:
    print(f"Amount to pay: ${amount}.")