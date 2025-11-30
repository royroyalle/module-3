try:
    num1, num2 = eval(input("Enter two numbers, seperate them with a comma:"))
    res = num1 / num2
except ZeroDivisionError:
    print("Divison by zero error")
except SyntaxError:
    print("Syntax Error has been made. Remember to seperate the numbers")
except:
    print("Wrong Input")
else:
    print("No exceptions")
finally:
    print("This code will execute")