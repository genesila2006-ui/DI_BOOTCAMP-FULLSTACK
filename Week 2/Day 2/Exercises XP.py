class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Step 1: Create the Siamese class
class Siamese(Cat):
    pass

# Step 2: Create a list of cat instances
bengal_obj = Bengal("Leo", 3)
chartreux_obj = Chartreux("Felix", 5)
siamese_obj = Siamese("Simba", 2)

all_cats = [bengal_obj, chartreux_obj, siamese_obj]

# Step 3: Create a Pets instance
sara_pets = Pets(all_cats)

# Step 4: Take cats for a walk
sara_pets.walk()
# Exercise 2: Dogs

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if my_power > other_power:
            return f"{self.name} won the fight!"
        elif other_power > my_power:
            return f"{other_dog.name} won the fight!"
        else:
            return "It's a tie!"

# Step 2 & 3: Instantiate and test
dog1 = Dog("Rex", 4, 20)
dog2 = Dog("Spot", 2, 15)
dog3 = Dog("Max", 5, 30)

print(dog1.bark())
print(f"{dog2.name}'s speed: {dog2.run_speed()}")
print(dog1.fight(dog2))
# Exercise 3: Dogs Domesticated

import random
# Assuming Dog class is imported from Exercise 2:
# from exercise2 import Dog

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        # Extracts dog names whether passed as Dog objects or strings
        names = [self.name]
        for arg in args:
            if isinstance(arg, Dog):
                names.append(arg.name)
            else:
                names.append(str(arg))
        print(f"{', '.join(names)} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")
        else:
            print(f"{self.name} is not trained yet!")

# Step 3: Test PetDog Methods
pet1 = PetDog("Fido", 3, 12)
pet2 = PetDog("Buddy", 2, 10)

pet1.train()
pet1.play(pet2, "Max")
pet1.do_a_trick()
# Exercise 4: Family and Person Classes

class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        return self.age >= 18

class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        new_person = Person(first_name, age)
        new_person.last_name = self.last_name
        self.members.append(new_person)
        print(f"Congratulations to the {self.last_name} family on the birth of {first_name}!")

    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print(f"Person named {first_name} is not in this family.")

    def family_presentation(self):
        print(f"\n--- The {self.last_name} Family ---")
        for member in self.members:
            print(f"Name: {member.first_name} {member.last_name}, Age: {member.age}")

# Testing the implementation
smith_family = Family("Smith")
smith_family.born("John", 45)
smith_family.born("Jane", 42)
smith_family.born("Alice", 20)
smith_family.born("Tom", 15)

smith_family.family_presentation()
smith_family.check_majority("Alice")
smith_family.check_majority("Tom")