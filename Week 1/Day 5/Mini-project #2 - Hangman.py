import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist) 

### YOUR CODE STARTS FROM HERE ###

guessed_letters = []
attempts_left = 6

print("Welcome to Hangman!")

while attempts_left > 0:
    # Build current display of the word
    display = ""
    for char in word:
        if char == ' ':
            display += "  "  # Spaces in multi-word items like 'credit card'
        elif char in guessed_letters:
            display += char + " "
        else:
            display += "_ "

    print(f"\nWord: {display}")
    print(f"Attempts remaining: {attempts_left}")
    print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")

    # Check if user has guessed all hidden letters
    word_letters = [char for char in word if char != ' ']
    if all(char in guessed_letters for char in word_letters):
        print(f"\nCongratulations! You guessed the word: '{word}'")
        break

    # Get player's input
    guess = input("Guess a letter: ").lower().strip()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input! Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try a different letter.")
        continue

    # Process guess
    guessed_letters.append(guess)

    if guess in word:
        print(f"Good job! '{guess}' is in the word.")
    else:
        attempts_left -= 1
        print(f"Sorry, '{guess}' is not in the word.")

# If player ran out of attempts
if attempts_left == 0:
    print(f"\nGame Over! You ran out of attempts. The word was '{word}'.")