import random
seguirJugando="si"

while True:
    eleccion = ["piedra", "papel", "tijeras"]
    player = None
    while player not in eleccion:
        player = input("Elija : piedra , papel o tijeras ").lower()

    computer = random.choice(eleccion)
    print("Jugador: "+player)
    print("Computadora: "+computer)
    if player=="piedra":
        if computer == player:
            print("Empate")
        elif computer=="papel":
            print("Perdiste")
        elif computer=="tijeras":
            print("Ganaste")

    elif player == "papel":
        if computer == player:
            print("Empate")
        elif computer == "tijeras":
            print("Perdiste")
        elif computer == "piedra":
            print("Ganaste")
    elif player == "tijeras":
        if computer == player:
            print("Empate")
        elif computer == "piedra":
            print("Perdiste")
        elif computer == "papel":
            print("Ganaste")
    seguir_jugando = input("¿Desea seguir jugando? (si/no) ").lower()
    if seguirJugando != "si":
        break