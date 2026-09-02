import re
import string
from collections import Counter


class Text:
	"""Analyze text supplied directly or loaded from a file."""

	def __init__(self, text):
		self.text = text

	def _words(self):
		return re.findall(r"\b[\w']+\b", self.text.lower())

	def word_frequency(self, word):
		"""Return the number of times word appears, or None if it is absent."""
		count = self._words().count(word.lower())
		return count if count else None

	def most_common_word(self):
		"""Return the most frequent word, or None when the text is empty."""
		frequencies = Counter(self._words())
		return frequencies.most_common(1)[0][0] if frequencies else None

	def unique_words(self):
		"""Return the unique words in alphabetical order."""
		return sorted(set(self._words()))

	@classmethod
	def from_file(cls, file_path):
		"""Create a Text instance from the contents of file_path."""
		with open(file_path, "r", encoding="utf-8") as file:
			return cls(file.read())


class TextModification(Text):
	"""Text analyzer with common text-cleaning operations."""

	STOP_WORDS = {
		"a", "an", "and", "are", "as", "at", "be", "by", "for", "from",
		"has", "he", "in", "is", "it", "its", "of", "on", "that", "the",
		"this", "to", "was", "were", "will", "with", "i", "you", "your",
	}

	def remove_punctuation(self):
		"""Remove punctuation and return the updated text."""
		translation_table = str.maketrans("", "", string.punctuation)
		self.text = self.text.translate(translation_table)
		return self.text

	def remove_stop_words(self):
		"""Remove common English stop words and return the updated text."""
		words = self.text.split()
		self.text = " ".join(
			word for word in words if word.lower().strip(string.punctuation) not in self.STOP_WORDS
		)
		return self.text

	def remove_special_characters(self):
		"""Remove non-alphanumeric characters and return the updated text."""
		self.text = re.sub(r"[^\w\s]", "", self.text)
		return self.text
