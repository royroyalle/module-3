def givchange():
    change = amount - product
    return change
product = 200
amount = int(input("Please pay for the prduct you have bought"))
if amount >200 and amount <1000:
    print(givchange())
elif amount ==200:
    print("You have been given no change")
elif amount < 200:
    print("You have to give more money")
else:
    print("Sorry, The shopkeeper got no change from the", amount, "dollars you have given")
