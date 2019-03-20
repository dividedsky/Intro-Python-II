import random


class Person():
    def __init__(self, name, att, defense, hitpoints, inventory=[]):
        self.name = name
        self.att = att
        self.defense = defense
        self.hitpoints = hitpoints
        self.inventory = inventory

    def __del__(self):
        print('deleted')

    def attack(self, defender):
        dmg = random.randrange(self.att)
        dmg -= defender.defense
        defender.takedamage(dmg)
        return dmg

    def takedamage(self, dmg):
        self.hitpoints -= dmg
        if self.hitpoints <= 0:
            self.die()
            return

    def die(self):
        print(f'{self.name} has been defeated!')
