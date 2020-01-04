class Player:
    """Общий класс предок"""
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
    """Это класс с отвечающий за игрока-человека."""
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
    """Это класс с отвечающий за игрока-npc."""    
    def __init__(self, name):
        super().__init__(name)
        self.deq = self.shuffle_numbers()
        self.discharged = deque([])

    def shuffle_numbers(self):
        templist = list(range(10, 99, 1))
        random.shuffle(templist)
        return deque(templist)

    def get_card(self):
        return list(random.sample(range(10, 99), 5))

    def check_number(self, number):
        """Игрок npc проверяет номер для себя"""
        if number in self.card:
            self.card.remove(number)
            print("Its my number!!")
            if len(self.card) == 0:
                print("Bingo!!! I have won!")
                self.card = self.get_card()

    def toss_a_number(self):
        """Выдаем новый номер"""
        if self.deq.count == 0:
            self.deq = self.shuffle_numbers()
        number = self.deq.pop()
        self.discharged.append(number)
        print("The number is:", number)
        self.check_number(number)
        return number

    def check_hand(self, player):
        """Проверяем данные игрока-человека"""
        if len(set(player.card) & set(player.hand)) == 5:
            print("Yes, you have won!")
            return True
        print("You have cheated!")
        return False


