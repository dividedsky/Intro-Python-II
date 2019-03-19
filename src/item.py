class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take():
        pass
    
    def on_drop():
        pass


class Torch(Item):
    name = 'torch'
    description = 'The flame flickers brightly'

    def __init__(self, name, description):
        super().__init__(name, description)
        self.light = 100

    def on_take():
        print('You feel more at ease with a light source equipped.')

    def on_drop():
        print('It is unwise to drop your source of light')

