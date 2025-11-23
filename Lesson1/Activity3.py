def add(r, s):
    return r + s
def sub(r, s):
    return r - s
def mul(r, s):
    return r*s
def div(r, s):
    return r/s
print("Welcome to the Calculator, Please enter the current operation required:")
print("\n Addition")
print("\n Substraction")
print("\n Multiplication")
print("\n Divison")
abc = input("Enter:")
num1 = int(input("Enter your first number"))
num2 = int(input("\n Enter your second number"))

if abc == 'Addition':
    print("Your answer is:", add(num1, num2))
elif abc == 'Substraction' or abc =='substraction':
    print("Your anwer is:", sub(num1, num2))
elif abc == 'Multiplication' or abc == 'multiplication':
    print("Your anwer is:", mul(num1, num2))
elif abc == 'Divison' or abc =='divison':
    print("Your anwer is:", div(num1, num2))
else:
    print("Invaild Inputs")