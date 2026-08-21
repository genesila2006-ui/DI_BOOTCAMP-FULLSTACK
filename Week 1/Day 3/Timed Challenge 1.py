# Python
REverseinp = input()

# Split the sentence into words, reverse the list, and join back into a string
words = REverseinp.split()
reversed = " ".join(words[::-1])

# Print the reversed sentence
print(reversed)
# Explanation:
# split(): Breaks the input string into a list of individual words based on whitespace.

# [::-1]: Uses list slicing to reverse the order of the words in the list.

# " ".join(...): Combines the reversed list of words back into a single string separated by spaces.