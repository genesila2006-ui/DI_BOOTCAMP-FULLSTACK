# Here are the Python solutions for the two challenges from your Developers Institute page:

# Challenge 1: Multiples of a Number

# Python
# Ask user for number and length
number = int(input("Enter a number: "))
length = int(input("Enter length: "))

# Generate multiples using a loop
multiples = []
for i in range(1, length + 1):
    multiples.append(number * i)

print(multiples)
# Challenge 2: Remove Consecutive Duplicate Letters

# Python
# Ask user for a word
user_word = input("Enter a word: ")

# Process string to remove consecutive duplicates
result = ""

for char in user_word:
    # Add character if the result string is empty or if it's different from the last added character
    if not result or char != result[-1]:
        result += char

print(result)