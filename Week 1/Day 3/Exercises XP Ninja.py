# Python
# 1. Original string
cars_str = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"

# 2. Convert into a list
manufacturers = [name.strip() for name in cars_str.split(",")]

# 3. Print company count
print(f"There are {len(manufacturers)} manufacturers in the list.")

# 4. Print list in reverse/descending order (Z-A)
sorted_descending = sorted(manufacturers, reverse=True)
print("Descending order (Z-A):", sorted_descending)

# 5. Letter counts using list comprehension
with_o = len([m for m in manufacturers if 'o' in m.lower()])
without_i = len([m for m in manufacturers if 'i' not in m.lower()])

print(f"Manufacturers with 'o': {with_o}")
print(f"Manufacturers without 'i': {without_i}")

# --- Bonus 1: Remove duplicates ---
duplicates_list = ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]

# Remove duplicates programmatically using set
unique_manufacturers = list(set(duplicates_list))

# Print comma-separated string and updated count
companies_str = ", ".join(unique_manufacturers)
print("\nCompanies without duplicates:", companies_str)
print(f"There are now {len(unique_manufacturers)} unique companies in the list.")

# --- Bonus 2: Ascending order with reversed letters ---
# Sort ascending (A-Z) and reverse the characters of each manufacturer name
reversed_names_asc = [m[::-1] for m in sorted(manufacturers)]
print("Sorted A-Z with reversed letters:", reversed_names_asc)
# Explanation of Key Methods Used:
# split(","): Converts the comma-separated string into a list automatically.

# sorted(..., reverse=True): Sorts the strings in alphabetical descending order.

# set(): Removes duplicate elements automatically since sets only store unique items.

# m[::-1]: Uses Python string slicing to reverse the order of characters in a string.