import unittest
import parser
from person import Person
from item import pancake
from player import Player


class TestItemMethods(unittest.TestCase):
    def test_attack(self):
        goblin = Person("goblin", 23, 0, 100)
        orc = Person("orc", 25, 0, 90)
        goblin.attack(orc)
        print(orc)
        self.assertTrue(orc.hitpoints < 90, f"orc hp: {orc.hitpoints}")
        orc.attack(goblin)
        print(goblin.hitpoints)
        self.assertTrue(goblin.hitpoints < 100, f"goblin hp: {goblin.hitpoints}")

    def test_food(self):
        player = Player("test_player")
        player.use_item(pancake)
        self.assertTrue(player.hitpoints > 30, "hp test")


if __name__ == "__main__":
    unittest.main()
