from termcolor import cprint


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self, player):
        print(f"You pick up the {self.name}")

    def on_drop(self):
        pass


class Torch(Item):
    name = "torch"
    description = "The flame flickers brightly"

    def __init__(self, name, description):
        super().__init__(name, description)
        self.light = 100

    def on_take(self):
        print("You feel more at ease with a light source equipped.")

    def on_drop():
        print("It is unwise to drop your source of light")


class Sword(Item):
    name = "sword"
    description = "It\s quite pointy"

    def __init__(self, name, description):
        super().__init__(name, description)
        self.attack_value = 20
        self.damage_value = 8

    def on_take(player):
        player.att += 20
        cprint("You wield the sword in your hand", "green")


class Food(Item):
    def __init__(self, name, nutrition, description="It's just normal food"):
        self.name = name
        self.nutrition = nutrition
        self.description = description

    def on_use(self, player):
        player.hitpoints += self.nutrition
        print(f"You eat the {self.name} and gain {self.nutrition} hitpoints")
        player.inventory.remove(self)


pancake = Food("pancake", 5, "a delicious pancake")
