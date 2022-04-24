import random

class Die:
    def __init__(self, value = None):
        self.value = value

    def roll(self):
        self.value = random.randint(1,6)

    def __str__(self):
        return str(self.value)

    def __int__(self):
        return self.value

    def __eq__(self, other):
        return int(self) == int(other)
