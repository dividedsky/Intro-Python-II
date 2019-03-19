# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, room, inventory=[]):
        self.room = room
        self.inventory = inventory

    def move(self, dir):
        try:
            next = getattr(self.room, dir)
            print('next:', next)
            self.room = next
        except AttributeError:
            print('You cannot go that way!')

    def get_inv(self):
        return self.inventory if len(self.inventory) \
                else 'Your inventory is empty'

    def get_item(self, item):
        if item in self.room.items:
            self.room.items.remove(item)
            self.inventory.append(item)

        
