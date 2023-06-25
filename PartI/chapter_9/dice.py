from random import randint
class Die:
    def __init__(self, sides=6):
        """"""
        self.sides = sides
        return

    def roll_die(self):
        return print(randint(1, self.sides))

rolling = Die()

# Rolling the Die 10 times
"""
for i in range(10):
    rolling.roll_die()
"""

rolling = Die(10)
"""
for i in range(10):
    rolling.roll_die()
"""

rolling = Die(20)
for i in range(10):
    rolling.roll_die()
