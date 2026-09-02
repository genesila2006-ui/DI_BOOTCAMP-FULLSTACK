class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Step 1: Create cat objects
cat1 = Cat("Whiskers", 3)
cat2 = Cat("Felix", 7)
cat3 = Cat("Mittens", 5)

# Step 2: Create a function to find the oldest cat
def find_oldest_cat(c1, c2, c3):
    cats = [c1, c2, c3]
    oldest = cats[0]
    for cat in cats[1:]:
        if cat.age > oldest.age:
            oldest = cat
    return oldest

# Step 3: Print the oldest cat's details
oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")
# Exercise 2: Dogs

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

# Step 2 & 3: Create objects and call methods
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)

print(f"David's dog: {davids_dog.name}, Height: {davids_dog.height}cm")
davids_dog.bark()
davids_dog.jump()

print(f"Sarah's dog: {sarahs_dog.name}, Height: {sarahs_dog.height}cm")
sarahs_dog.bark()
sarahs_dog.jump()

# Step 4: Compare sizes
if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger than {sarahs_dog.name}.")
elif sarahs_dog.height > davids_dog.height:
    print(f"{sarahs_dog.name} is bigger than {davids_dog.name}.")
else:
    print(f"Both dogs are the same size.")
# Exercise 3: Who's the Song Producer?

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway = Song([
    "There’s a lady who's sure",
    "all that glitters is gold",
    "and she’s buying a stairway to heaven"
])

stairway.sing_me_a_song()
# Exercise 4: Afternoon at the Zoo

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
        self.grouped_animals = {}

    # Standard method (or use *args for Bonus below)
    def add_animal(self, *new_animals):
        for animal in new_animals:
            if animal not in self.animals:
                self.animals.append(animal)

    def get_animals(self):
        print(f"Animals in {self.name}: {', '.join(self.animals)}")

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        self.animals.sort()
        self.grouped_animals = {}
        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter not in self.grouped_animals:
                self.grouped_animals[first_letter] = [animal]
            else:
                self.grouped_animals[first_letter].append(animal)
        return self.grouped_animals

    def get_groups(self):
        for letter, animal_list in self.grouped_animals.items():
            print(f"{letter}: {animal_list}")

# Test the implementation
brooklyn_safari = Zoo("Brooklyn Safari")

# Adding multiple animals using the *args bonus feature
brooklyn_safari.add_animal("Giraffe", "Bear", "Baboon", "Cat", "Cougar", "Lion", "Zebra")
brooklyn_safari.get_animals()

brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()

brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()