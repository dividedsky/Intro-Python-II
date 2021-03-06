# should parser be a class? just making a function for now
import sys
from show_help import show_help


def parser(command, player):
    player.new_room = False
    length = len(command.split())
    # one-word commands
    if length == 1:
        if command in "nsew":
            player.move(command + "_to")
        elif command == "i" or command == "inv":
            player.get_inv()
        elif command == "l" or command == "look":
            player.room.print_room()
        elif command == "status" or command == "st":
            player.get_status()
        elif command == "q" or command == "quit":
            print("Bye!")
            sys.exit()
        elif command == "?" or command == "help":
            show_help()
        else:
            print(
                f"I do not understand the command: {command}. Enter '?' to see a list of commands I understand"
            )

    # complex commands
    elif length >= 2:
        args = command.split()
        verb = args[0]
        noun = " ".join(args[1:])
        # pick up item
        if verb == "get" or verb == "take":
            player.get_item(noun)
        elif verb == "drop":
            player.drop_item(noun)
        elif verb == "attack" or verb == "kill":
            player.fight(noun)
        elif verb == "eat" or verb == "use":
            player.use_item(noun)
        elif verb == "look" or verb == "inspect":
            player.inspect_item(noun)
        else:
            print("I'm not sure what you mean. Try '?' to see my limited vocabulary.")

    else:
        print("I don't understand what you want to do.")
