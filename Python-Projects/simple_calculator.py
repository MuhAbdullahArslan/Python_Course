num1 = int(input("Enter the number : "))
num2 = int(input("Enter the number : "))

operator = input("Enter the operator (+,-,/,*,**,%): ")

if operator == '+':
    print(num1 + num2)
elif operator == "-":
    print(num1 + num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "**":
    print(num1 ** num2)
elif operator == "%":
    print(num1 % num2)
else:
    print("Invalid Operator")

