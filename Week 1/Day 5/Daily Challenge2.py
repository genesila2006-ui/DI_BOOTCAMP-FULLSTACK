import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number = 3728

# Using a set for fast O(1) lookups
seen = set()
pairs = set()

for number in list_of_numbers:
    complement = target_number - number
    if complement in seen:
        # Store as a sorted tuple so pairs like (a, b) and (b, a) aren't duplicated
        pairs.add(tuple(sorted((number, complement))))
    seen.add(number)

# Display results
print(f"Found {len(pairs)} unique pairs that sum to {target_number}:\n")
for num1, num2 in pairs:
    print(f"{num1} and {num2} sum to {target_number}")