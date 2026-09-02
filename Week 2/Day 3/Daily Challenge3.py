class user_data:
    """Store people and provide the required sorted output."""

    def __init__(self):
        self.people = []

    def add(self, name, age, score):
        """Add a person, normalizing numeric fields for accurate sorting."""
        self.people.append((name.strip(), int(age), int(score)))

    def sorted(self):
        """Return people sorted by name, then age, then score."""
        return sorted(self.people, key=lambda person: (person[0], person[1], person[2]))

    def as_strings(self):
        """Return sorted records with all values represented as strings."""
        return [(name, str(age), str(score))
                for name, age, score in self.sorted()]


user_data = user_data()

# 1. Collect inputs 5 times
for i in range(5):
    raw_input = input(f"Enter person {i+1} (Name, Age, Score separated by commas): ")
    name, age, score = [item.strip() for item in raw_input.split(',')]
    
    user_data.add(name, age, score)

# 2. Sort by priority: Name -> Age -> Score, then format the values.
output = user_data.as_strings()

print(output)
