import random
from person import Person


goblin = Person('goblin', 8, 1, 30)


class Monster(Person):
    def __init__(self, name, att, defense):
        self.name = name
        self.hitpoints = 30
        self.damage = 0

    def attack(self, defender):
        dmg = random.randrange(self.damage)
        defender.hitpoints -= dmg
        if defender.hitpoints <= 0:
            defender.die()

    def die(self):
        print(f'{self.name} is defeated!')

