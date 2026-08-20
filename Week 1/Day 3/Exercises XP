keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# Combine lists using zip() and dict()
res_dict = dict(zip(keys, values))
print(res_dict)
# Exercise 2: Cinemax #2

# Python
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_cost = 0

for name, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    
    print(f"{name.capitalize()} has to pay ${price}.")
    total_cost += price

print(f"Total family ticket cost: ${total_cost}")

# Bonus: User Input
user_family = {}
while True:
    name = input("Enter family member's name (or 'quit' to finish): ").strip()
    if name.lower() == 'quit':
        break
    age = int(input(f"Enter age for {name}: "))
    user_family[name] = age

user_total = 0
for name, age in user_family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    user_total += price

print(f"Calculated total for entered family: ${user_total}")
# Exercise 3: Zara

# Python
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

# 1. Change number_stores
brand["number_stores"] = 2

# 2. Print sentence about clients
clothes = ", ".join(brand["type_of_clothes"])
print(f"Zara produces clothing and goods for {clothes}.")

# 3. Add country_creation
brand["country_creation"] = "Spain"

# 4. Add "Desigual" if international_competitors exists
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

# 5. Delete creation_date
brand.pop("creation_date")

# 6. Print last item in international_competitors
print("Last competitor:", brand["international_competitors"][-1])

# 7. Print major colors in US
print("US major colors:", brand["major_color"]["US"])

# 8. Print number of keys
print("Number of keys:", len(brand))

# 9. Print all keys
print("Keys:", list(brand.keys()))

# Bonus: Merge dictionaries
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}
brand.update(more_on_zara)
print("Updated brand dictionary:", brand)
# Exercise 4: Disney Characters

# Python
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# 1. Character to index mapping
dict1 = {user: i for i, user in enumerate(users)}
print("1:", dict1)

# 2. Index to character mapping
dict2 = {i: user for i, user in enumerate(users)}
print("2:", dict2)

# 3. Alphabetically sorted characters mapped to indices
sorted_users = sorted(users)
dict3 = {user: i for i, user in enumerate(sorted_users)}
print("3:", dict3)