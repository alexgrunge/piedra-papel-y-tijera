import random

reultado = random.randint(1,3)



jugador_mano= str(input(" escribe, piedra, papel o tijera "))

if reultado == 1:
    resultado = "piedra"
elif reultado == 2:
    resultado = "papel"
elif reultado == 3:
    resultado = "tijera"

if jugador_mano == resultado:
    print("empate")
elif jugador_mano == "piedra" and resultado == "papel":
    print("papel.. perdiste")
elif jugador_mano == "piedra" and resultado == "tijera":
    print("tijera...ganaste")

elif jugador_mano == "papel" and resultado == "tijera":
    print("tijera.. perdiste")
elif jugador_mano == "papel" and resultado == "piedra":
    print("piedra.. ganaste")

elif jugador_mano == "tijera" and resultado == "piedra":
    print("piedra... perdiste")
elif jugador_mano == "tijera" and resultado == "papel":
    print("papel.. ganaste")