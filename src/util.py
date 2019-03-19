import os
import sys


def clear_screen():
    if sys.path == 'windows':
        os.system('cls')
    else:
        os.system('clear')
