#Este es el modulo principal desde el cual se corre el programa y se llaman los modulos para poder cargar y jugar.

from deck import Deck
from player import Player
from utils import guardar_datos, cargar_datos

class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.deck.generate()
        self.player = None

    def display_menu(self):
        logo = """
        .------.            _     _            _    _            _    
        |A_  _ |.          | |   | |          | |  (_)          | |   
        |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
        | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
        |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
        `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
              |  \/ K|                            _/ |                
              `------'                           |__/           
        """
        print("\n----- BLACKJACK ♥♦♣♠ MENU -----")
        print(logo)
        print("a. Seleccionar usuario o crear uno nuevo")
        print("b. Nuevo juego")
        print("c. Estadísticas")
        print("d. Salir")

    def select_or_create_user(self):
        name = input("Ingrese su nombre de usuario: ")
        self.player = Player(False, self.deck)
        self.player.set_name(name)
        print(f"Usuario seleccionado/creado: {self.player.get_name()}")

    def new_game(self):
        if self.player is None:
            print("Por favor, seleccione un usuario primero.")
            return

        dealer = Player(True, self.deck)
        player = self.player

        print("\nIniciando nuevo juego...")
        print("\nRepartiendo cartas...\n")

        dealer.deal()
        player.deal()

        dealer.show()
        player.show()

        while True:
            cmd = input(" Sigues jugando,¿Deseas pedir una carta (Hit) o parar (Stand)? ").lower()

            if cmd == "hit":
                bust = player.hit()
                player.show()

                if bust == 1:
                    print(" OH NO! ¡Te pasaste de 21! ¡Has perdido!")
                    player.add_stat("loss")
                    guardar_datos("estadisticas.txt", f"{self.player.get_name()} - Perdió", append=True)  # Guardar nombre y resultado en formato .txt
                    break
            elif cmd == "stand":
                print("\n")
                dealer.show()

                # Mostrar las cartas del jugador
                print("Cartas del Jugador")
                for card in player.cards:
                    card.show()

                # Mostrar las cartas del dealer
                print("Cartas del Dealer")
                for card in dealer.cards:
                    card.show()

                while dealer.check_score() < 17:
                    if dealer.hit() == 1:
                        dealer.show()
                        print("¡La casa se pasó de 21! ¡Has ganado!")
                        player.add_stat("El jugador gana!")
                        guardar_datos("estadisticas.txt", f"{self.player.get_name()} - Ganó", append=True)  # Guardar nombre y resultado en formato .txt
                        return
                    dealer.show()

                if dealer.check_score() == player.check_score():
                    print("Es un empate. ¡Mejor suerte para la próxima!")
                    player.add_stat("EMPATE!")
                    guardar_datos("estadisticas.txt", f"{self.player.get_name()} - Empate", append=True)  # Guardar nombre y resultado en formato .txt
                elif dealer.check_score() > player.check_score():
                    print("La casa gana. ¡Has perdido!")
                    player.add_stat("Has perdido!")
                    guardar_datos("estadisticas.txt", f"{self.player.get_name()} - Perdió", append=True)  # Guardar nombre y resultado en formato .txt
                elif dealer.check_score() < player.check_score():
                    print("¡Has ganado! ¡Felicidades!")
                    player.add_stat("El jugador gana")
                    guardar_datos("estadisticas.txt", f"{self.player.get_name()} - Ganó", append=True)  # Guardar nombre y resultado en formato .txt
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    def show_statistics(self):
        if self.player is None:
            print("Por favor, seleccione un usuario primero.")
            return

        print(f"\nEstadísticas de {self.player.get_name()}:")

        # Leer el contenido del archivo estadisticas.txt
        stats = cargar_datos("estadisticas.txt")

        if stats is None or len(stats) == 0:
            print("No hay estadísticas disponibles.")
        else:
            # Ordenar la lista por nombre de usuario y resultado del juego
            sorted_stats = sorted(stats)

            # Mostrar los resultados ordenados
            for index, stat in enumerate(sorted_stats, start=1):
                print(f"Juego {index}: {stat}")

    def play(self):
        while True:
            self.display_menu()
            option = input("Seleccione una opción: ").lower()

            if option == "a":
                self.select_or_create_user()
            elif option == "b":
                self.new_game()
            elif option == "c":
                self.show_statistics()
            elif option == "d":
                break
            else:
                print("Opción inválida. Intente nuevamente.")

        print("Gracias por jugar Blackjack. ¡Hasta luego!")


b = Blackjack()
b.play()
