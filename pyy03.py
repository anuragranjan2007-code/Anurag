numbers = [-5, 10, -3, 7, -2, 8, -1]

sum_negative = 0

for num in numbers:
    if num < 0:
        sum_negative += num

print("Sum of all negative numbers:", sum_negative)
