# Write a class to hold player information, e.g. what room they are in
# currently.
import sys
import time
from person import Person
from termcolor import cprint


class Player(Person):
    def __init__(self, room, inventory=[]):
        super().__init__('you', 10, 2, 50)   # att, def, hp
        self.room = room
        self.inventory = inventory
        self.new_room = True

    def move(self, dir):
        try:
            next = getattr(self.room, dir)
            # print('next:', next)
            self.room = next
            self.new_room = True
        except AttributeError:
            cprint('You cannot go that way!', 'red')

    def get_inv(self):
        return self.inventory if len(self.inventory) \
                else 'Your inventory is empty'

    def get_item(self, item):
        found = False
        # I'm sure there's a better way to do this...
        for i in self.room.items:
            if i.name == item:
                self.room.items.remove(i)
                self.inventory.append(i)
                found = True
                cprint(f'You pick up the {i.name} '
                       'and stuff it in your sack', 'green')
                i.on_take()
        if not found:
            cprint(f'I do not see a {item} here', 'red')

    def drop_item(self, item):
        dropped = False
        for i in self.inventory:
            if i.name == item:
                self.room.items.append(i)
                self.inventory.remove(i)
                dropped = True
                cprint(f'You have dropped {i.name}.' 
                       'Hope you won\'t need that!', 'yellow')
                i.on_drop()
        if not dropped:
            cprint(f'You can\'t drop what you never had...', 'red')

    def fight(self, defender):
        found = False
        for monster in self.room.monsters:
            if monster.name == defender:
                found = True
                defender = monster
                while self.hitpoints > 0 and defender.hitpoints > 0:
                    dmg = self.attack(defender)
                    print(f'{self.name} attack for {dmg} points of damage!')
                    if defender.hitpoints <= 0:
                        self.room.monsters.remove(defender)
                        del defender
                        break
                    time.sleep(1)
                    dmg = defender.attack(self)
                    print(f'{defender.name} attacks for {dmg} points of damage!')
                    if self.hitpoints <= 0:
                        break
                    time.sleep(1)
        if not found:
            print(f'There is no {defender} here')

    def die(self):
        print('You have suffered yet another stupid death.')
        print('Please play again.')
        sys.exit()
        
