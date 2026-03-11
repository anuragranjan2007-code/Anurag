# Take input from user
text = input("Enter a string: ")

# Split string into words
words = text.split()

# Create empty dictionary
freq = {}

# Count frequency of each word
for word in words:
    freq[word] = freq.get(word, 0) + 1

# Print result
print("Word Frequency:")
for word, count in freq.items():
    print(word, ":", count)