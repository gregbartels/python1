#Este modulo contiene el menu y el arranque del juego


from deck import Deck
from player import Player


        #Inicia el juego de Blackjack.
        
class BlackjackGame:
    def __init__(self):
        self.deck = None
        self.player = None
        self.stats = []

    def start(self):
        print("¡Bienvenido a Blackjack!")
        self.deck = Deck()
        self.menu()

    def menu(self):
        while True:
            print("\n----- Menú -----")
            print("a. Seleccionar usuario o crear uno nuevo")
            print("b. Nuevo juego")
            print("c. Estadísticas")
            print("d. Salir")
            option = input("Seleccione una opción: ").lower()

            if option == "a":
                self.select_or_create_user()

            elif option == "b":
                if self.player is None:
                    print("Por favor, seleccione un usuario primero.")
                else:
                    self.play_game()

            elif option == "c":
                if self.player is None:
                    print("Por favor, seleccione un usuario primero.")
                else:
                    self.show_statistics()

            elif option == "d":
                break

            else:
                print("Opción inválida. Intente nuevamente.")

    def select_or_create_user(self):
        name = input("Ingrese su nombre de usuario: ")
        self.player = Player(name)
        print(f"Usuario seleccionado/creado: {self.player}")

    def play_game(self):
        self.reset_hands()
        self.deal_initial_cards()

        if self.check_blackjack():
            return

        while True:
            choice = input

