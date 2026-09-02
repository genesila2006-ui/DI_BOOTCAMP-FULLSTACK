"""OOP quiz and a simple deck of cards implementation."""

import random


# Exercise 1: OOP quiz
#
# A class is a blueprint that defines data and behavior for objects.
# An instance is one object created from a class.
# Encapsulation keeps data and the methods that use it together, while
# controlling how that data is accessed.
# Abstraction exposes the important interface while hiding implementation
# details.
# Inheritance lets a class reuse or extend another class's behavior.
# Multiple inheritance lets a class inherit from more than one parent class.
# Polymorphism lets different classes respond to the same method call in their
# own way.
# Method resolution order (MRO) is the order Python follows when searching for
# a method or attribute through a class's inheritance hierarchy.


class Card:
	"""Represent one playing card."""

	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def __str__(self):
		return f"{self.value} of {self.suit}"

	def __repr__(self):
		return f"Card({self.suit!r}, {self.value!r})"


class Deck:
	"""Represent and manage a standard 52-card deck."""

	SUITS = ("Hearts", "Diamonds", "Clubs", "Spades")
	VALUES = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

	def __init__(self):
		self.cards = []
		self.shuffle()

	def shuffle(self):
		"""Reset the deck to 52 cards and rearrange it randomly."""
		self.cards = [
			Card(suit, value)
			for suit in self.SUITS
			for value in self.VALUES
		]
		random.shuffle(self.cards)

	def deal(self):
		"""Remove and return one card, or return None if the deck is empty."""
		return self.cards.pop() if self.cards else None


if __name__ == "__main__":
	deck = Deck()
	print(f"Deck created with {len(deck.cards)} cards.")
	print(f"Dealt card: {deck.deal()}")
	print(f"Cards remaining: {len(deck.cards)}")
