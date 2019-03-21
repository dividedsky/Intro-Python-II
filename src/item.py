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
        cprint(f"You pick up the {self.name}", "blue")

    def on_drop(self):
        pass

    def on_use(self, player):
        pass


class Lightsource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.light = 100

    def on_take(self, player):
        cprint("You feel more at ease with a light source equipped.", "green")

    def on_drop(self):
        cprint("It is unwise to drop your source of light", "blue")


class Sword(Item):
    def __init__(self, name, description, attack_value, damage_value):
        super().__init__(name, description)

    def on_take(self, player):
        player.att += 20
        cprint("You wield the sword in your hand and feel like a badass", "green")

    def on_use(self, player):
        pass


class Food(Item):
    def __init__(self, name, nutrition, description="It's just normal food"):
        super().__init__(name, description)
        self.nutrition = nutrition

    def on_use(self, player):
        player.hitpoints += self.nutrition
        cprint(f"You eat the {self.name} and gain {self.nutrition} hitpoints", "green")
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

            cprint(
                "You fling the rope across the chasm. Incrediby, it loops securely around a rock. You can now exit this simple game!",
                "green",
            )
        else:
            options = [
                "You take a break and jump rope before returning to your adventure",
                "You consider hanging yourself, but decide to move on",
                "It's a rope! Wow.",
            ]
            choice = random.randrange(len(options))
            cprint(options[choice], "blue")


rope = Rope("sturdy rope", "It's a very long rope. Who knows why a dragon had it?")
torch = Lightsource("torch", "the flame flickers brightly")
sword = Sword("dull sword", "It's dull but still pointy", 20, 8)

pancake = Food("pancake", 5, "a delicious pancake")
cake = Food("birthday cake", 10, "this cake is not a lie")
pie = Food("apple pie", 10, "just like Mom made it")

shield = Armor("rusty shield", "an old and battered shield", 10)
gold = Item("pile of gold", "it's really quite a bit of gold")
