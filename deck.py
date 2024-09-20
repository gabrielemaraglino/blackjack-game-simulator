import random
from card import Card 

class Deck:
    def __init__(self):
        self.cards = []

    def generate(self):
        for i in range(1, 14):
            for j in range(4):
                self.cards.append(Card(i, j))

    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw(self, card_num):
        cards = []
        for i in range(card_num):
            card = self.cards.pop()
            cards.append(card)
        return cards

