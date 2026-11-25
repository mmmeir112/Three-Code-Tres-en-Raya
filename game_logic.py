import sys

# DF3 · RF-06 y RF-07. Estado inicial de DF3_fin.rap.
c1, c2, c3 = "X", "O", "X"
c4, c5, c6 = "O", "O", "O"
c7, c8, c9 = "O", "X", "X"
estado = "continua"

# Las pruebas pueden proporcionar otro tablero en la línea de comandos.
if len(sys.argv) == 2:
    tablero_prueba = sys.argv[1]
    if len(tablero_prueba) != 9:
        sys.exit("El tablero de prueba requiere nueve casillas.")
    for posicion, valor in enumerate(tablero_prueba, start=1):
        if valor not in ("X", "O", str(posicion)):
            sys.exit("Cada casilla debe contener X, O o el número de su posición.")
    c1, c2, c3, c4, c5, c6, c7, c8, c9 = tablero_prueba

print("DF3 · Fin de la partida")
print(c1 + c2 + c3, c4 + c5 + c6, c7 + c8 + c9, sep=" / ")

# RF-06: primero las ocho líneas de X, después las ocho de O.
if (
    (c1 == "X" and c2 == "X" and c3 == "X")
    or (c4 == "X" and c5 == "X" and c6 == "X")
    or (c7 == "X" and c8 == "X" and c9 == "X")
    or (c1 == "X" and c4 == "X" and c7 == "X")
    or (c2 == "X" and c5 == "X" and c8 == "X")
    or (c3 == "X" and c6 == "X" and c9 == "X")
    or (c1 == "X" and c5 == "X" and c9 == "X")
    or (c3 == "X" and c5 == "X" and c7 == "X")
):
    estado = "gana_j1"
    print("¡Ha ganado el Jugador 1!")
elif (
    (c1 == "O" and c2 == "O" and c3 == "O")
    or (c4 == "O" and c5 == "O" and c6 == "O")
    or (c7 == "O" and c8 == "O" and c9 == "O")
    or (c1 == "O" and c4 == "O" and c7 == "O")
    or (c2 == "O" and c5 == "O" and c8 == "O")
    or (c3 == "O" and c6 == "O" and c9 == "O")
    or (c1 == "O" and c5 == "O" and c9 == "O")
    or (c3 == "O" and c5 == "O" and c7 == "O")
):
    estado = "gana_j2"
    print("¡Ha ganado el Jugador 2!")
# RF-07: hay empate si ninguna casilla conserva su número inicial.
elif (
    c1 != "1" and c2 != "2" and c3 != "3"
    and c4 != "4" and c5 != "5" and c6 != "6"
    and c7 != "7" and c8 != "8" and c9 != "9"
):
    estado = "empate"
    print("¡Empate! El tablero está lleno.")
else:
    estado = "continua"
    print("La partida continúa.")
