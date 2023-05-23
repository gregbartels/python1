#Este modulo contiene el codigo del jugador, como guardar la estadisticas de gane, empata o pierda y cargar los datos a el archivo estadistica.txt

from deck import Deck
from utils import guardar_datos

class Player:
    def __init__(self, isDealer, deck):
        self.cards = []
        self.isDealer = isDealer
        self.deck = deck
        self.score = 0
        self.name = ""
        self.stats = {}  # Diccionario para almacenar las estadísticas

    def hit(self):
        self.cards.extend(self.deck.draw(1))
        return self.check_score()

    def deal(self):
        self.cards = self.deck.draw(2)
        return self.check_score()

    def check_score(self):
        a_counter = 0
        self.score = 0
        for card in self.cards:
            if card.price() == 11:
                a_counter += 1
            self.score += card.price()

        while a_counter != 0 and self.score > 21:
            a_counter -= 1
            self.score -= 10

        return 1 if self.score > 21 else 0

    def show(self):
        if self.isDealer:
            if self.cards:
                print("Cartas del Dealer (La casa)")
                self.cards[0].show()  # Muestra solo la primera carta del dealer
            else:
                print("Cartas del Dealer (La casa)")
        else:
            print("Cartas del Jugador")
            for card in self.cards:
                card.show()

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def add_stat(self, stat):
        if self.name in self.stats:
            self.stats[self.name].append(stat)
        else:
            self.stats[self.name] = [stat]

        if stat == "loss":
            num_attempts = len(self.stats[self.name])
            stat_txt = f"El jugador {self.name} ha perdido el juego en el intento {num_attempts}"
            guardar_datos("estadisticas.txt", stat_txt, append=True)
        elif stat == "win":
            num_attempts = len(self.stats[self.name])
            stat_txt = f"El jugador {self.name} ha ganado el juego en el intento {num_attempts}"
            guardar_datos("estadisticas.txt", stat_txt, append=True)
        elif stat == "draw":
            num_attempts = len(self.stats[self.name])
            stat_txt = f"El jugador {self.name} ha empatado el juego en el intento {num_attempts}"
            guardar_datos("estadisticas.txt", stat_txt, append=True)

    def get_stats(self):
        if self.name in self.stats:
            return self.stats[self.name]
        else:
            return []

    def reset_stats(self):
        self.stats = {}
