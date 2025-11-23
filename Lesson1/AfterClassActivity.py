def circ():
    return 2 * pie * r
def circ2():
    return pie * d
pie = 3.14159
print("Welcome to Circumference Calculator")
print("Do you have a radius?")
a = str(input("Enter Yes OR No:"))
if a == "Yes" or a == "yes":
    r = int(input("Enter the Radius:"))
    print("Answer is:")
    print(circ())
if a == "No" or a == "no":
    d = int(input("Enter the Diameter:"))
    print("Answer is:")
    print(circ2())
elif a != "No" and a != "no" and a!="Yes" and a!= "yes":
    print("Invaild")



