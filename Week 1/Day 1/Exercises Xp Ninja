# Exercise 1: Use the terminal

# Command: Open your terminal (or Command Prompt/PowerShell on Windows) and run python3 (or python on Windows) to start the interactive console.

# PATH Explanation: The PATH variable is an environment variable in your operating system that stores a list of directory locations. When you type a command like python3, the OS searches through these specified directories to find the executable file. Because the folder containing Python is listed in PATH, you can launch Python from any working directory without typing its full file location.

# Exercise 2: Alias

# An alias creates a custom shortcut or alternative name for a terminal command.

# Linux/macOS (Bash/Zsh): Run alias py='python3' in your shell or add it to ~/.bashrc / ~/.zshrc.

# Windows (PowerShell): Run Set-Alias -Name py -Value python.

# Note: On many Windows installations, the Python Launcher executable py.exe is installed by default, so typing py already launches Python out of the box.

# Exercise 3: Outputs

# Python
3 <= 3 < 9                         # Output: True (3 <= 3 is True and 3 < 9 is True)
3 == 3 == 3                        # Output: True (3 == 3 and 3 == 3)
bool(0)                            # Output: False (0 evaluates to False)
bool(5 == "5")                     # Output: False (5 == "5" is False)
bool(4 == 4) == bool("4" == "4")   # Output: True (True == True)
bool(bool(None))                   # Output: False (None becomes False, bool(False) is False)

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)                   # Output: x is True (True equals 1 in Python)
print("y is", y)                   # Output: y is False
print("a:", a)                     # Output: a: 5 (True acts as 1, so 1 + 4 = 5)
print("b:", b)                     # Output: b: 10 (False acts as 0, so 0 + 10 = 10)
# Exercise 4: How many characters in a sentence?

# Python
my_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
           sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
           Ut enim ad minim veniam, quis nostrud exercitation ullamco 
           laboris nisi ut aliquip ex ea commodo consequat. 
           Duis aute irure dolor in reprehenderit in voluptate velit 
           esse cillum dolore eu fugiat nulla pariatur. 
           Excepteur sint occaecat cupidatat non proident, 
           sunt in culpa qui officia deserunt mollit anim id est laborum."""

print(len(my_text))
# Exercise 5: Longest word without a specific character

# Python
longest_length = 0

while True:
    sentence = input("Enter a sentence without the character 'A' (or 'quit' to exit): ")
    
    if sentence.lower() == 'quit':
        break
        
    if 'a' in sentence.lower():
        print("Oops! Your sentence contains the letter 'A'. Try again.")
    else:
        current_length = len(sentence)
        if current_length > longest_length:
            longest_length = current_length
            print(f"Congratulations! You set a new record with {longest_length} characters!")
        else:
            print(f"Valid sentence, but your current record is {longest_length} characters.")