from collections import deque
import sys
import random


class Player:
    def __init__(self, name):
        self.name = name
        self.card = list()

    def set_card(self, card):
        self.card = card
        print(f'{self.name} got new card')
        self.show_card()

    def show_card(self):
        print(f'Card of {self.name} has numbers: {self.card}')

class Human(Player):
    def __init__(self, name):
        super().__init__(name)
        self.hand = list()

    def add_to_hand(self, number):
        self.hand.append(number)
        if len(self.hand) == 5:
            print("You have full card")
            return True
        return False


class NPC(Player):
    def __init__(self, name):
        super().__init__(name)
        self.deq = self.shuffle_numbers()
        self.sbros = deque([])

    def shuffle_numbers(self):
        mylist = list(range(10, 99, 1))
        random.shuffle(mylist)
        return deque(mylist)

    def get_card(self):
        return list(random.sample(range(10, 99), 5))

    def check_number(self, number):
        if number in self.card:
            self.card.remove(number)
            print("Its my number!!")
            if len(self.card) == 0:
                print("Bingo!!! I have won!")
                self.card = self.get_card()

    def toss_a_number(self):
        if self.deq.count == 0:
            self.deq = self.shuffle_numbers()
        number = self.deq.pop()
        self.sbros.append(number)
        print("The number is:", number)
        self.check_number(number)
        return number

    def check_hand(self, player):
        if len(set(player.card) & set(player.hand)) == 5:
            print("Yes, you have won!")
            return True
        else:
            print("You have cheated!")
            return False


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
