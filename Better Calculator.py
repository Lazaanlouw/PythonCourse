
num1 = float(input("Please enter your first number: "))
op = input("Please enter a operator: ")
num2 = float(input("Please enter your second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid Operator")
    