# Python
x = int(input('Enter the Number:')) 

# Calculate the sum of proper divisors (excluding the number itself)
divisors_sum = sum(i for i in range(1, x) if x % i == 0)

# Print True if the sum equals x, else False
print(divisors_sum == x)
# Explanation
# range(1, x): Iterates through all potential divisors starting from 1 up to (but not including) x.

# x % i == 0: Checks if i divides x evenly without a remainder.

# sum(...): Adds up all valid proper divisors.

# divisors_sum == x: Evaluates whether the sum equals the original number, printing True or False.