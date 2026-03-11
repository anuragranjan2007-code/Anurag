name = input("Enter your full name: ")

vowels = "aeiouAEIOU"
count = 0

for ch in name:
    if ch in vowels:
        count += 1

print("Total number of vowels:", count)

