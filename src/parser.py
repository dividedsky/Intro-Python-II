# should parser be a class? just making a function for now


def parser(command, player):
    player.new_room = False
    length = len(command.split())
    # one-word commands
    if length == 1:
        if command in 'nsew':
            player.move(command + '_to')
        elif command == 'i' or command == 'inv':
            print(player.get_inv())
        elif command == 'l' or command == 'look':
            player.room.print_room()
        else:
            print(f'I do not understand the command: {command}')

    # complex commands
    elif length == 2:
        args = command.split()
        verb = args[0]
        item = args[1]
        # pick up item
        if (verb == 'get' or verb == 'take'):
            player.get_item(item)
        elif verb == 'drop':
            player.drop_item(item)
