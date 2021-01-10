import random


class Dice:
    def rolls(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print("dice rolls..")
print(dice.rolls())
