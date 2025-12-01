try:
    age = int(input("Enter Age"))
    if age == str:
        raise ValueError
    elif age%2==0:
        print("Your Age is even")
    else:
        print("Age is odd")
except ValueError:
    print("You have typed something other than a number")