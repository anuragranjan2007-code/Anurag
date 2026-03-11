
num1 = float(input("Enter the first number (dividend): "))
num2 = float(input("Enter the second number (divisor): "))
if num2 != 0:
    remainder = num1 % num2
    print("The remainder is:", remainder)
else:
    print("Division by zero is not allowed.")
