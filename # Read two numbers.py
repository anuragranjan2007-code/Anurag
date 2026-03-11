# Read two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Check if num1 is a multiple of num2
if num1 % num2 == 0:
    print(f"{num1} is a multiple of {num2}")
else:
    print(f"{num1} is not a multiple of {num2}")
