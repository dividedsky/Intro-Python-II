import random


class Person():
    def __init__(self, name, att, defense, hitpoints):
        self.name = name
        self.att = att
        self.defense = defense
        self.hitpoints = hitpoints

    def attack(self, defender):
        dmg = random.randrange(self.att)
        dmg -= defender.defense
        defender.takedamage(dmg)

    def takedamage(self, dmg):
        self.hitpoints -= dmg
        if self.hitpoints <= 0:
            self.die()

    def die(self):
        print(f'{self.name} has been defeated!')
