#Este modulo crea el objeto deck o mazo de cartas

import random
from Card import Card

class Deck:
    def __init__(self):
        self.cards = []

    def generate(self):
        for value in range(1, 14):
            for suit in range(4):
                self.cards.append(Card(value, suit))

    def draw(self, num_cards):
        cards = []
        for _ in range(num_cards):
            card = random.choice(self.cards)
            self.cards.remove(card)
            cards.append(card)
        return cards

    def count(self):
        return len(self.cards)
