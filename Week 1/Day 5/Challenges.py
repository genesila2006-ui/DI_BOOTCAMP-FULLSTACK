my_list = [10, 20, 30, 40]
index = 2
item = 25

my_list.insert(index, item)
print(my_list)  # [10, 20, 25, 30, 40]
#Exercise 2

#Python
text = "Hello world! How are you?"
space_count = text.count(" ")
print(space_count)  # 4
#Exercise 3

#Python
text = "Hello World!"
upper_count = sum(1 for char in text if char.isupper())
lower_count = sum(1 for char in text if char.islower())

print(f"Upper case: {upper_count}, Lower case: {lower_count}")
#Exercise 4

#Python
def my_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total
#Exercise 5

#Python
def find_max(lst):
    if not lst:
        return None
    max_num = lst[0]
    for num in lst[1:]:
        if num > max_num:
            max_num = num
    return max_num
#Exercise 6

#Python
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
#Exercise 7

#Python
def list_count(lst, target):
    count = 0
    for item in lst:
        if item == target:
            count += 1
    return count
#Exercise 8

#Python
def norm(lst):
    sum_of_squares = sum(x**2 for x in lst)
    return sum_of_squares**0.5
#Exercise 9

#Python
def is_mono(arr):
    increasing = all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
    decreasing = all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))
    return increasing or decreasing
#Exercise 10

#Python
def print_longest_word(words):
    if not words:
        return
    longest = max(words, key=len)
    print(longest)
#Exercise 11

#Python
data = [1, "apple", 2, "banana", 3, "cherry"]

integers = [x for x in data if isinstance(x, int)]
strings = [x for x in data if isinstance(x, str)]
#Exercise 12

#Python
def is_palindrome(s):
    return s == s[::-1]
#Exercise 13

#   Python
def sum_over_k(sentence, k):
    words = sentence.split()
    return sum(1 for word in words if len(word) > k)
#Exercise 14

#   Python
def dict_avg(d):
    if not d:
        return 0
    return sum(d.values()) / len(d)
#Exercise 15

#   Python
def common_div(a, b):
    divisors = []
    min_num = min(a, b)
    for i in range(2, min_num + 1):
        if a % i == 0 and b % i == 0:
            divisors.append(i)
    return divisors
#Exercise 16

#   Python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
#Exercise 17

#   Python
def weird_print(lst):
    result = [val for idx, val in enumerate(lst) if idx % 2 == 0 and val % 2 == 0]
    print(result)
#Exercise 18

#   Python
def type_count(**kwargs):
    counts = {}
    for value in kwargs.values():
        t_name = type(value).__name__
        counts[t_name] = counts.get(t_name, 0) + 1
    
    return ", ".join(f"{t}: {c}" for t, c in counts.items())
#Exercise 19

#   Python
def my_split(text, delimiter=None):
    result = []
    current = []

    if delimiter is None:
        in_space = False
        for char in text:
            if char.isspace():
                if not in_space and current:
                    result.append("".join(current))
                    current = []
                in_space = True
            else:
                in_space = False
                current.append(char)
        if current:
            result.append("".join(current))
    else:
        for char in text:
            if char == delimiter:
                result.append("".join(current))
                current = []
            else:
                current.append(char)
        result.append("".join(current))

    return result
#Exercise 20

#   Python
def mask_password(password):
    return "*" * len(password)