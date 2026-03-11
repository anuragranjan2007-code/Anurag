# Sorted list
lst = [1, 2, 3, 4, 5]

# Input positions
i = int(input("Enter first index: "))
j = int(input("Enter second index: "))

# Swap
lst[i], lst[j] = lst[j], lst[i]

print("List after swapping:", lst)
