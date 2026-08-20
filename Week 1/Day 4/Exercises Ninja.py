def get_full_name(first_name, last_name, middle_name=""):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


# Examples
print(
    get_full_name(
        first_name="john", middle_name="hooker", last_name="lee"
    )
)  # John Hooker Lee
print(get_full_name(first_name="bruce", last_name="lee"))  # Bruce Lee
# Exercise 2: From English to Morse

# Python
MORSE_CODE_DICT = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
}

# Reverse dictionary for decoding
REVERSE_MORSE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}


def english_to_morse(text):
    words = text.upper().split(' ')
    morse_words = []
    for word in words:
        morse_letters = [MORSE_CODE_DICT[char] for char in word if char in MORSE_CODE_DICT]
        morse_words.append(' '.join(morse_letters))
    return ' / '.join(morse_words)


def morse_to_english(morse_text):
    words = morse_text.split(' / ')
    english_words = []
    for word in words:
        letters = word.split(' ')
        english_letters = [REVERSE_MORSE_DICT[code] for code in letters if code in REVERSE_MORSE_DICT]
        english_words.append(''.join(english_letters))
    return ' '.join(english_words)


# Examples
morse = english_to_morse('Hello World')
print(morse)  # .... . .-.. .-.. --- / .-- --- .-. .-.. -..
print(morse_to_english(morse))  # HELLO WORLD
# Exercise 3: Box of stars

# Python
def box_printer(*args):
    if not args:
        return

    max_length = max(len(s) for s in args)
    border = '*' * (max_length + 4)

    print(border)
    for word in args:
        print(f'* {word.ljust(max_length)} *')
    print(border)


# Example
box_printer('Hello', 'World', 'in', 'reallylongword', 'a', 'frame')
# Exercise 4: What is the purpose of this code?

# Purpose: The function implements the Insertion Sort algorithm. It sorts an unsorted list of numbers in ascending order in-place.

# How it works: It iterates through the list starting from the second element, compares the current value with the elements before it, and shifts larger elements one position to the right until it finds the correct spot to insert the current value.

# Output: [17, 20, 26, 31, 44, 54, 55, 77, 93]