#Este modulo contiene la informacion para crear el objeto Carta

class Card:
    def __init__(self, value, suit):
        self.cost = value
        self.value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'][value-1]
        self.suit = '♥♦♣♠'[suit]

# Funcion para crear la carta o que imprima una carta https://stackoverflow.com/questions/74023710/printing-on-same-line-for-python
    def show(self):
        print(f"┌───────┐")
        print(f"| {self.value:<2}    |")
        print(f"|       |")
        print(f"|   {self.suit}   |")
        print(f"|       |")
        print(f"|    {self.value:>2} |")
        print(f"└───────┘")


    def price(self):
        if self.cost >= 10:
            return 10
        elif self.cost == 1:
            return 11
        return self.cost
