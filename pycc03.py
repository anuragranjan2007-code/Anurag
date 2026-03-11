n = int(input("Enter 4 digit number: "))

a = n // 1000      # thousand digit
b = n % 10          # unit digit

# middle part
mid = (n % 1000) // 10

# swap
new = b*1000 + mid*10 + a

print("After swap:", new)
