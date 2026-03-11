lst = list(map(int, input("Enter list: ").split()))
i = int(input("First index: "))
j = int(input("Second index: "))

if i < len(lst) and j < len(lst):
    lst[i], lst[j] = lst[j], lst[i]
    print(lst)
else:
    print("Invalid index")
