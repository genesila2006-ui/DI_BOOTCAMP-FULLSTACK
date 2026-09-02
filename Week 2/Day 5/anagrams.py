import anagram_checker


def get_valid_word():
    """Read and validate one alphabetic word from the user."""
    while True:
        word = input("Enter a word: ").strip()

        if len(word.split()) != 1:
            print("Error: please enter only one word.")
        elif not word.isalpha():
            print("Error: please use alphabetic characters only.")
        else:
            return word


def display_word_information(word, checker):
    """Display validity and anagrams for a word."""
    anagrams = checker.get_anagrams(word)
    validity = "a valid" if checker.is_valid_word(word) else "not a valid"

    print(f'\nYOUR WORD: "{word.upper()}"')
    print(f"This is {validity} English word.")
    if anagrams:
        print(f"Anagrams for your word: {', '.join(anagrams)}")
    else:
        print("Anagrams for your word: none found")
    print()


def main():
    checker = anagram_checker.AnagramChecker()

    while True:
        print("1. Enter a word")
        print("2. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            display_word_information(get_valid_word(), checker)
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Error: please choose 1 or 2.\n")


if __name__ == "__main__":
    main()
