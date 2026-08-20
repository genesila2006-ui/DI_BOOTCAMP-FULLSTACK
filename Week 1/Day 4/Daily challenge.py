def count_occurrences(string, char):
    return string.count(char)


# --- Tests ---
# Test 1
s1 = "Programming is cool!"
c1 = "o"
print(f"String: {s1}\nCharacter: {c1}\n{count_occurrences(s1, c1)}\n")

# Test 2
s2 = "This is a great example"
c2 = "y"
print(f"String: {s2}\nCharacter: {c2}\n{count_occurrences(s2, c2)}")
# Interactive Version (Takes User Input):

# Python
string_input = input("Enter a string: ")
char_input = input("Enter a character to count: ")

occurrences = string_input.count(char_input)
print(f"Number of occurrences: {occurrences}")