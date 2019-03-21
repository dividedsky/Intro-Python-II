from termcolor import cprint
import random
from room import Room

exit = Room(
    "Cave Exit",
    """
    You have managed to escape the cave!
    """,
)


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
        cprint(f"You eqip the {self.name} and feel more robust", "green")


class Rope(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

    def on_use(self, player):
        if player.room.name == "Grand Overlook":
            player.room.n_to = exit
            player.room.description = """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance. Your rope is attached to the other side, and you could cross the chasm if you wished."""

            print(
                "You fling the rope across the chasm. Incrediby, it loops securely around a rock. You can now exit this simple game!"
            )
        else:
            options = [
                "You take a break and jump rope before returning to your adventure",
                "You consider hanging yourself, but decide to move on",
                "It's a rope! Wow.",
            ]
            choice = random.randrange(len(options))
            print(options[choice])


rope = Rope("sturdy rope", "It's a very long rope. Who knows why a dragon had it?")

pancake = Food("pancake", 5, "a delicious pancake")
cake = Food("birthday cake", 10, "this cake is not a lie")
pie = Food("apple pie", 10, "just like Mom made it")

shield = Armor("rusty shield", "an old and battered shield", 10)
gold = Item("pile of gold", "it's really quite a bit of gold")
