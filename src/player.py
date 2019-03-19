# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, room):
        self.room = room

    def move(self, dir):
        try:
            next = getattr(self.room, dir)
            print('next:', next)
            self.room = next
        except AttributeError:
            print('You cannot go that way!')
        
