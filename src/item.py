from termcolor import cprint


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self, player):
        print(f"You pick up the {self.name}")

    def on_drop(self):
        pass

    def on_use(self, player):
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

    def on_use(self):
        pass


class Food(Item):
    def __init__(self, name, nutrition, description="It's just normal food"):
        super().__init__(name, description)
        self.nutrition = nutrition

    def on_use(self, player):
        player.hitpoints += self.nutrition
        print(f"You eat the {self.name} and gain {self.nutrition} hitpoints")
        player.inventory.remove(self)


class Armor(Item):
    def __init__(self, name, description="some generic armor", armor_class=1):
        super().__init__(name, description)
        self.armor_class = armor_class

    def on_take(self, player):
        player.defense += self.armor_class
        cprint(f"You eqip the ${self.name} and feel more robust", "green")


pancake = Food("pancake", 5, "a delicious pancake")
cake = Food("birthday cake", 10, "this cake is not a lie")
pie = Food("apple pie", 10, "just like Mom made it")

shield = Armor("rusty shield", "an old and battered shield", 10)
gold = Item("pile of gold", "it's really quite a bit of gold")
