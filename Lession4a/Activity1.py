try:
    num = int(input("Please enter a number"))
    print("The number is", num) 
except ValueError as exe:
    print("Exception", exe)