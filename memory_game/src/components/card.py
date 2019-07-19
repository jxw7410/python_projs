class Card:
    def __init__(self, value):
        self.value = value
        self.is_reveal = False

    # Special Methods
    def __str__(self):
        return f"{ str(self.value) + ('' if self.value > 9 else ' ')}"

    def __eq__(self, other):
        return self.value == other.value

    # Public Methods
    def hide(self):
        self.is_reveal = False

    def reveal(self):
        self.is_reveal = True
