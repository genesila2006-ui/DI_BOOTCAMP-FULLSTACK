from pathlib import Path


class AnagramChecker:
    """Check words and find their anagrams from a word list."""

    def __init__(self, word_list_path=None):
        if word_list_path is None:
            word_list_path = Path(__file__).with_name("sowpods.txt")

        with open(word_list_path, "r", encoding="utf-8") as file:
            self.word_list = {
                line.strip().lower()
                for line in file
                if line.strip()
            }

    def is_valid_word(self, word):
        """Return True when word exists in the loaded word list."""
        return word.strip().lower() in self.word_list

    @staticmethod
    def is_anagram(word1, word2):
        """Return True when two words contain the same letters."""
        first = word1.strip().lower()
        second = word2.strip().lower()
        return sorted(first) == sorted(second)

    def get_anagrams(self, word):
        """Return all different word-list entries that are anagrams of word."""
        normalized_word = word.strip().lower()
        return sorted(
            candidate
            for candidate in self.word_list
            if candidate != normalized_word
            and self.is_anagram(normalized_word, candidate)
        )
