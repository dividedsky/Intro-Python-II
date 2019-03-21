import random


class Person:
    def __init__(self, name, att, defense, hitpoints, inventory=None):
        self.name = name
        self.att = att
        self.defense = defense
        self.hitpoints = hitpoints
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

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

    def use_item(self, item):
        # item is defined by name
        found = False
        for i in self.inventory:
            if i.name == item:
                found = True
                item = i
                item.on_use(self)
        if found is False:
            print("You don't have that item")

    def die(self):
        print(f"{self.name} has been defeated!")
        del self
