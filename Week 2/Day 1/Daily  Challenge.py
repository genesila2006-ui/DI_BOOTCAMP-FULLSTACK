class Farm:
    # Step 2: __init__ Method
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    # Step 3 & Step 8 (Bonus): Updated add_animal to support positional args & **kwargs
    def add_animal(self, animal_type=None, count=1, **kwargs):
        # Handles single animal additions: macdonald.add_animal('cow', 5)
        if animal_type:
            if animal_type in self.animals:
                self.animals[animal_type] += count
            else:
                self.animals[animal_type] = count

        # Handles multiple animals via **kwargs: macdonald.add_animal(cow=5, sheep=2)
        for animal, quantity in kwargs.items():
            if animal in self.animals:
                self.animals[animal] += quantity
            else:
                self.animals[animal] = quantity

    # Step 4: get_info Method
    def get_info(self):
        info = f"{self.name}'s farm\n\n"
        for animal, count in self.animals.items():
            info += f"{animal:<7} : {count}\n"
        info += "\n    E-I-E-I-0!"
        return info

    # Step 6 (Bonus): get_animal_types Method
    def get_animal_types(self):
        return sorted(list(self.animals.keys()))

    # Step 7 (Bonus): get_short_info Method
    def get_short_info(self):
        types = self.get_animal_types()
        formatted_animals = []

        for animal in types:
            # Pluralize animal name if count > 1
            if self.animals[animal] > 1:
                formatted_animals.append(f"{animal}s")
            else:
                formatted_animals.append(animal)

        # Join animals with commas and "and" for the last item
        if len(formatted_animals) > 1:
            animal_str = ", ".join(formatted_animals[:-1]) + f" and {formatted_animals[-1]}"
        else:
            animal_str = formatted_animals[0]

        return f"{self.name}'s farm has {animal_str}."


# --- Step 5: Testing the Code ---

macdonald = Farm("McDonald")

# Standard add_animal calls
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

# Printing full info
print(macdonald.get_info())
print("\n" + "="*30 + "\n")

# Testing Bonus Methods
print("Animal Types (Sorted):", macdonald.get_animal_types())
print(macdonald.get_short_info())

# Testing upgraded add_animal with **kwargs
macdonald.add_animal(horse=1, duck=3)
print("\nAfter adding kwargs animals:")
print(macdonald.get_short_info())