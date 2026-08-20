import random

# 1. Ask for User Input
user_string = input("Enter a string that is exactly 10 characters long: ")

# 2. Check the Length of the String
if len(user_string) < 10:
    print("String not long enough.")
elif len(user_string) > 10:
    print("String too long.")
else:
    print("Perfect string")

    # 3. Print the First and Last Characters
    print(f"First character: {user_string[0]}")
    print(f"Last character: {user_string[-1]}")

    # 4. Build the String Character by Character
    print("\nProgressive construction:")
    current_string = ""
    for char in user_string:
        current_string += char
        print(current_string)

    # 5. Bonus: Jumble the String
    char_list = list(user_string)
    random.shuffle(char_list)
    jumbled_string = "".join(char_list)
    print(f"\nJumbled string: {jumbled_string}")