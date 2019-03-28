# Implement a class to hold room information. This should have name and
# description attributes.
from termcolor import cprint
import random


class Room():
    def __init__(self, name, description, items=[], monsters=[]):
        self.name = name
        self.description = description
        self.items = items
        self.light = random.randrange(100)
        self.monsters = monsters
    
    def print_room(self):
        cprint('****{}****'.format(self.name.upper()), 'red')
        cprint(self.description, 'green')

        if len(self.items):
            cprint('You see here:', 'yellow')
            for item in self.items:
                cprint(item.name, 'yellow')

        if len(self.monsters):
            for monster in self.monsters:
                cprint(f'There is a {monster.name} here!', 'red')
