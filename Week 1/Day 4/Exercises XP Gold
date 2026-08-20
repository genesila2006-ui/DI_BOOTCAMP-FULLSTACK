# Python
def calculate_special_sum(X):
    # Convert integer X to string to construct XX, XXX, XXXX
    x_str = str(X)
    
    term1 = int(x_str)
    term2 = int(x_str * 2)
    term3 = int(x_str * 3)
    term4 = int(x_str * 4)
    
    return term1 + term2 + term3 + term4

# Example test call
result = calculate_special_sum(3)
print(f"Output for X=3: {result}")  # Expected output: 3702
# Exercise 3: Double Dice

# Python
import random

def throw_dice():
    return random.randint(1, 6)

def throw_until_doubles():
    throw_count = 0
    while True:
        die1 = throw_dice()
        die2 = throw_dice()
        throw_count += 1
        
        if die1 == die2:
            break
            
    return throw_count

def main():
    results = []  # List collection to store throws per double
    
    # Throw doubles 100 times
    for _ in range(100):
        throws_needed = throw_until_doubles()
        results.append(throws_needed)
        
    total_throws = sum(results)
    average_throws = round(total_throws / len(results), 2)
    
    print(f"Total throws: {total_throws}")
    print(f"Average throws to reach doubles: {average_throws}")

# Run main function
main()