# Juego de Blackjack

Esta es una implementación de línea de comandos del clásico juego de cartas Blackjack.

El concepto del juego se toma como base los diferentes formas de poder ejemplificar por medio de la programacion por objetos un juego famoso aplicando los diferentes conceptos vistos en clase, la idea primordial es simular un juego de "21" o blackjack.

## Cómo jugar

1. Instala Python 3.x si aún no lo has hecho.
2. Clona este repositorio o descarga el archivo `blackjack.py`.
3. Abre una terminal o símbolo del sistema y navega hasta el directorio donde se encuentra `blackjack.py`.
4. Ejecuta el comando `python blackjack.py` para iniciar el juego.
5. Sigue las instrucciones en pantalla para jugar el juego.
una vez iniciado encontraras el siguiente menu:


----- BLACKJACK ♥♦♣♠ MENU -----

        .------.            _     _            _    _            _
        |A_  _ |.          | |   | |          | |  (_)          | |
        |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
        | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
        |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
        `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
              |  \/ K|                            _/ |
              `------'                           |__/

a. Seleccionar usuario o crear uno nuevo
b. Nuevo juego
c. Estadísticas
d. Salir
Seleccione una opción:




* Debes ingresar un nombre de usuario ( opcion a) de lo contrario el menu volvera a aparecer sin dejarte iniciar el juego.

* Una vez cargado el nombre podras ver desplegado tu usuario  cn la leyenda " Usuario seleccionado/creado:XXXXXX".

* Selecciona la opcion b d para crear un nuevo juego, esta opcion tambien sirve para volver a jugar con el mismo usuario luego de cada partida.

* La opcion c muestra las estadisticas y adicionalmente, con cada partida de juego se genera un archivo llamado "Estadisticas.txt" donde se almacena todas las partidas jugadas y su resultado.

*  La opcion d es para salir del juego.



## Reglas y jugabilidad

- El Blackjack es un juego de cartas en el que el objetivo es tener una mano con un valor lo más cercano posible a 21 sin pasarse.
- El jugador compite contra el crupier, quien representa a la casa.
- Al comienzo del juego, cada jugador recibe dos cartas.
- Los jugadores pueden elegir "pedir" (recibir otra carta) o "plantarse" (dejar de recibir cartas).
- Si el valor de la mano de un jugador supera 21, pierde el juego.
- El crupier debe pedir cartas hasta que el valor de su mano sea 17 o más.
- El jugador gana si su valor de mano es mayor que el del crupier sin pasarse de 21.
- Reglas y estrategias más detalladas se pueden encontrar en el código fuente del juego.

## Clases

1. `Deck`: Representa una baraja de cartas. Puede generarse y barajarse.
2. `Player`: Representa un jugador en el juego. Tiene una mano de cartas y puede realizar acciones como repartir, pedir cartas y mostrar la mano.
3. `Blackjack`: La clase principal que orquesta el juego. Maneja el menú, la entrada del usuario y la lógica del juego.


## Estadísticas

Las estadísticas del jugador se almacenan en el archivo `estadisticas.txt`. El resultado de cada juego (ganar, perder o empatar) se registra junto al nombre del jugador.

## Contribuciones

¡Las contribuciones a este proyecto son bienvenidas! Si tienes alguna sugerencia o encuentras algún problema, no dudes en abrir un problema o enviar una solicitud para mejorar el juego.



## Creditos

* Logo python  https://ascii.co.uk/art/blackjack
* dibujo de las cartas en python https://stackoverflow.com/questions/74023710/printing-on-same-line-for-python

