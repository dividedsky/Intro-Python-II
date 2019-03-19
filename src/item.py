class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Torch(Item):
    name = 'torch'
    description = 'The flame flickers brightly'

    def __init__(self, name, description):
        super().__init__(name, description)
        self.light = 100

