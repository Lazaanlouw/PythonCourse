try:
    number = int(input("Enter a Number: "))
    print(number)
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("Invalid Input")
