# should parser be a class? just making a function for now


def parser(command, player):
    player.new_room = False
    length = len(command.split())
    # one-word commands
    if length == 1:
        if command in 'nsew':
            player.move(command + '_to')
        elif command == 'i':
            print(player.get_inv())
        elif command == 'l':
            player.room.print_room()
        else:
            print(f'I do not understand the command: {command}')

    # complex commands
    elif length == 2:
        args = command.split()
        verb = args[0]
        if (verb == 'get'):
            item = args[1]
            player.get_item(item)

