# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, room, inventory=[]):
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
            print('You cannot go that way!')

    def get_inv(self):
        return self.inventory if len(self.inventory) \
                else 'Your inventory is empty'

    def get_item(self, item):
        print(f'trying to pick up {item}')
        found = False
        # I'm sure there's a better way to do this...
        for i in self.room.items:
            if i.name == item:
                self.room.items.remove(i)
                self.inventory.append(i)
                found = True
                print(f'You pick up the {i.name} and stuff it in your sack')
        if not found:
            print(f'I do not see a {item} here')

        
