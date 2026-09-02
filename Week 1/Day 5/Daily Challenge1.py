# Step 1: Get Input
user_input = input("Enter comma-separated words: ")

# Step 2: Split the String
words_list = user_input.split(",")

# Step 3: Sort the List
words_list.sort()

# Step 4: Join the Sorted List
result = ",".join(words_list)

# Step 5: Print the Result
print(result)
# Challenge 2: Longest Word

# Python
def longest_word(sentence):
    # Step 2: Split the Sentence into Words
    words = sentence.split()

    # Step 3: Initialize Variables
    longest = ""

    # Step 4 & 5: Iterate Through the Words and Compare Lengths
    for word in words:
        if len(word) > len(longest):
            longest = word

    # Step 6: Return the Longest Word
    return longest


# Example tests matching expected outputs:
print(longest_word("Margaret's toy is a pretty doll."))  # Margaret's
print(longest_word("A thing of beauty is a joy forever."))  # forever.
print(longest_word("Forgetfulness is by all means powerless!"))  # Forgetfulness