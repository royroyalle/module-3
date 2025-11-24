it = input("Please enter a word to check if it has A in it:")
for i in it:
    if i == "A" or i == "a":
        print("Letter A is found")
        break
    else:
        print("Letter A is not found")