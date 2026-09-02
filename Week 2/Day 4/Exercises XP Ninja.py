# Exercise 1 : Restaurant Menu Manager - Regular Expressions
# Instructions
# Goal: The Manager wants to have a special Valentine's night, but there are some rules.
#
#
#
# Create a new list of special Valentine's day items inside the json file. For now the list should be empty.
#
# Ask to the manager for a new Valentine item to add, if the item is correct (ie. follows the rules below), then add it to the list inside the json file.
# Each word in the item name should begin with an uppercase letter and because it's Valentines Day, the first word needs to begin with a capital "V".
#
# If the name contains connection words, they should begin in lowercase.
# Example: Vegetable Soup of Valentines-day
#
# The name of the meal needs to contain at least two "e", and no numbers.
#
# The price needs to match the following pattern: XX,14, where X are numbers.
#
# Create an algorithm that displays a heart made of stars (*), when the menu is showed.

import json
import re

# TODO: Implement Exercise 1


# Exercise 2 : Dungeons & Dragons
# Instructions
# For a game of Dungeons & Dragons, each player starts by generating a character they can play with.
# This character has, among other things, six attributes/stats:
# - Strength
# - Dexterity
# - Constitution
# - Intelligence
# - Wisdom
# - Charisma
#
# These six abilities have scores that are determined randomly. You do this by rolling four 6-sided dice
# and record the sum of the largest three dice. You do this six times, once for each ability.
# For example, the six throws of four dice may look like:
# 5, 3, 1, 6: You discard the 1 and sum 5 + 3 + 6 = 14, which you assign to strength.
# 3, 2, 5, 3: You discard the 2 and sum 3 + 5 + 3 = 11, which you assign to dexterity.
# 1, 1, 1, 1: You discard the 1 and sum 1 + 1 + 1 = 3, which you assign to constitution.
# 2, 1, 6, 6: You discard the 1 and sum 2 + 6 + 6 = 14, which you assign to intelligence.
# 3, 5, 3, 4: You discard the 3 and sum 5 + 3 + 4 = 12, which you assign to wisdom.
# 6, 6, 6, 6: You discard the 6 and sum 6 + 6 + 6 = 18, which you assign to charisma.
#
# Create a class called Character and a class called Game for this exercise.
#
# The point of this exercise is to generate characters for players looking to start a game quickly.
# Start by asking the user how many players are playing.
# Each user then creates his/her character, let them establish what the characters name and age are.
# Output the characters created into the following formats:
# txt: a nicely formatted text file for the players to use
# json: a json file of all the characters and attributes
#
# Hint: the Character class should be in charge of creating characters, the Game class should be in charge
# of how many times the Character gets instantiated and of exporting the data in json or txt

import random

class Character:
    """Class to represent a Dungeons & Dragons character."""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.abilities = self._generate_abilities()

    def _generate_abilities(self):
        """Generate the six character abilities by rolling four 6-sided dice."""
        abilities = {}
        ability_names = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

        for ability in ability_names:
            rolls = [random.randint(1, 6) for _ in range(4)]
            rolls.sort()
            score = sum(rolls[1:])
            abilities[ability] = score

        return abilities


class Game:
    """Class to manage the game and character creation."""

    def __init__(self):
        self.characters = []

    def start(self):
        """Start the game and create characters for players."""
        num_players = int(input("How many players are playing? "))

        for i in range(num_players):
            print(f"\n--- Creating Character {i + 1} ---")
            name = input("Enter character name: ")
            age = int(input("Enter character age: "))
            character = Character(name, age)
            self.characters.append(character)

        self.export_characters()

    def export_characters(self):
        """Export characters to both txt and json formats."""
        self._export_to_txt()
        self._export_to_json()

    def _export_to_txt(self):
        """Export characters to a text file."""
        with open("characters.txt", "w") as f:
            for character in self.characters:
                f.write(f"Character: {character.name}\n")
                f.write(f"Age: {character.age}\n")
                f.write("Abilities:\n")
                for ability, score in character.abilities.items():
                    f.write(f"  {ability}: {score}\n")
                f.write("\n")

    def _export_to_json(self):
        """Export characters to a JSON file."""
        characters_data = []
        for character in self.characters:
            characters_data.append({
                "name": character.name,
                "age": character.age,
                "abilities": character.abilities
            })

        with open("characters.json", "w") as f:
            json.dump(characters_data, f, indent=4)


if __name__ == "__main__":
    game = Game()
    game.start()
