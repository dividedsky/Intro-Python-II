# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items
    
    def print_room(self):
        print('****{}****'.format(self.name.upper()))
        print(self.description)

        if len(self.items):
            print('You see here:')
            for item in self.items:
                print(item)
