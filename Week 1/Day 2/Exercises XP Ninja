# Exercise 1: Formula

# Python
import math

C = 50
H = 30

user_input = input("Enter comma-separated values for D: ")
d_values = user_input.split(",")

results = []
for d in d_values:
    D = float(d.strip())
    Q = math.sqrt((2 * C * D) / H)
    results.append(str(round(Q)))

print(",".join(results))
# Exercise 2: List of Integers

# Python
import random

# 1. Store the list of numbers in a variable
numbers = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]

# 2a. Print list in a single line
print("a. Numbers:", " ".join(map(str, numbers)))

# 2b. Sorted in descending order
print("b. Sorted descending:", sorted(numbers, reverse=True))

# 2c. Sum of all numbers
print("c. Sum:", sum(numbers))

# 3. First and last numbers
print("3. First and last:", [numbers[0], numbers[-1]])

# 4. Numbers greater than 50
print("4. Greater than 50:", [x for x in numbers if x > 50])

# 5. Numbers smaller than 10
print("5. Smaller than 10:", [x for x in numbers if x < 10])

# 6. Numbers squared
print("6. Squared:", " ".join(str(x**2) for x in numbers))

# 7. Without duplicates and count
unique_numbers = list(set(numbers))
print(f"7. Unique: {unique_numbers} (Count: {len(unique_numbers)})")

# 8. Average
print("8. Average:", sum(numbers) / len(numbers))

# 9. Largest number
print("9. Largest:", max(numbers))

# 10. Smallest number
print("10. Smallest:", min(numbers))

# 11. Bonus: Without built-in functions
total_sum = 0
largest = numbers[0]
smallest = numbers[0]
count = 0

for num in numbers:
    total_sum += num
    count += 1
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

avg = total_sum / count
print(f"11. Manual -> Sum: {total_sum}, Avg: {avg}, Max: {largest}, Min: {smallest}")

# 12. Bonus: Get user input (10 numbers)
# user_list = [int(input(f"Enter int {i+1} (-100 to 100): ")) for i in range(10)]

# 13. Bonus: Generate 10 random integers
rand_10 = [random.randint(-100, 100) for _ in range(10)]

# 14. Bonus: Random amount of integers (>= 50)
rand_amount = random.randint(50, 100)
rand_dynamic = [random.randint(-100, 100) for _ in range(rand_amount)]

# 15. Bonus: Answer
# Yes, the code will work dynamically regardless of list size because operations like sum(), len(), and loops adapt to list length.
# Exercise 3: Working on a paragraph

# Python
import re

paragraph = (
    "Python is an easy to learn, powerful programming language. "
    "It has efficient high-level data structures and a simple but effective approach to object-oriented programming. "
    "Python's elegant syntax and dynamic typing make it an ideal language for scripting."
)

chars_count = len(paragraph)
sentences_count = len(re.findall(r'[.!?]+', paragraph))
words = paragraph.split()
words_count = len(words)
unique_words_count = len(set(words))

# Bonuses
non_whitespace_count = len(paragraph.replace(" ", "").replace("\n", "").replace("\t", ""))
avg_words_per_sentence = words_count / sentences_count if sentences_count > 0 else 0
non_unique_words_count = words_count - unique_words_count

print(f"Total characters: {chars_count}")
print(f"Sentences: {sentences_count}")
print(f"Words: {words_count}")
print(f"Unique words: {unique_words_count}")
print(f"Non-whitespace characters: {non_whitespace_count}")
print(f"Average words per sentence: {avg_words_per_sentence:.2f}")
print(f"Non-unique words count: {non_unique_words_count}")
# Exercise 4: Frequency Of The Words

# Python
text_input = input("Enter a sentence: ")
words = text_input.split(" ")

word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

for word in sorted(word_counts.keys()):
    print(f"{word}:{word_counts[word]}")