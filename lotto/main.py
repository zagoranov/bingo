import sys
from bingos import *


def main():
    player = Human(input('Enter your name:'))
    npc = NPC("Arthur")
    print(f'Hello, {player.name}, I am {npc.name}, lets start the game.')
    npc.set_card(npc.get_card())
    player.set_card(npc.get_card())
    while True:
        player.show_card()
        number = npc.toss_a_number()
        have = input('Do you have it? y/n/q')
        if have == 'y':
            if player.add_to_hand(number):
                if npc.check_hand(player):
                    player.card = npc.get_card()
        elif have == 'q':
            sys.exit(2)


if __name__ == '__main__':
    main()
