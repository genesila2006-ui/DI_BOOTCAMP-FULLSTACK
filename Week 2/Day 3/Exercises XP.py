class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __repr__(self):
        return f"Currency('{self.currency}', {self.amount})"

    def __add__(self, other):
        if isinstance(other, Currency) and self.currency == other.currency:
            return Currency(self.currency, self.amount + other.amount)
        else:
            raise TypeError("Cannot add different currencies")

    def __iadd__(self, other):
        if isinstance(other, Currency) and self.currency == other.currency:
            self.amount += other.amount
            return self
        else:
            raise TypeError("Cannot add different currencies")