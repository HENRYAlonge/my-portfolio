num1 = float(input("Enter the value for the first number:"))
num2 = float(input("Enter the value for the second number:"))
operation = input("choose an operator (+, *, /, -,):")
valid = True

if operation == "+":
    result = num1 + num2
elif operation == "*":
    result = num1 * num2
elif operation == "-":
    result = num1 - num2
elif operation == "/":
 if  num2 !=0:
     result = num1 / num2
 else:
    result = "Not divisible by zero"
    valid = False
else:
    result = "Invalid operator"
    valid = False

if valid:
    print("Result:",result)
else:
    print(result)







