# Estados independientes para probar DF2 y DF3 como en RAPTOR.
# Un número representa una casilla libre. X y O representan casillas ocupadas.
TABLERO_DF2 = "X234O6789"
JUGADOR_DF2 = 1


def mostrar_tablero(tablero):
    # RF-03 · Muestra tres filas y conserva el número de cada casilla libre.
    for inicio in (0, 3, 6):
        print(" | ".join(tablero[inicio:inicio + 3]))


def pedir_jugada(tablero, jugador):
    # DF2 · RF-02 y RF-05. Un error mantiene al mismo jugador en el turno.
    simbolo = "X" if jugador == 1 else "O"
    print(f"Turno del Jugador {jugador} ({simbolo})")
    while True:
        entrada = input("Elige una casilla del 1 al 9: ").strip()
        if len(entrada) != 1 or entrada not in "123456789":
            print("¡Jugada inválida! Escribe un número del 1 al 9.")
            continue
        posicion = int(entrada)
        if tablero[posicion - 1] in ("X", "O"):
            print("¡Jugada inválida! La casilla está ocupada.")
            continue
        return posicion


# ==============================================================================
# game_logic.py · Traducción de DF3 (Fin de la partida) · RF-06, RF-07
# ==============================================================================


def evaluar_fin_partida(c1, c2, c3, c4, c5, c6, c7, c8, c9):
    """Evalúa DF3 y retorna: 'gana_j1', 'gana_j2', 'empate' o 'continua'."""
    estado = "continua"

    # RF-06: Verifica si el Jugador 1 (X) alineó 3 símbolos en fila, columna o diagonal
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
        print("Ha ganado el Jugador 1")
        return estado

    # RF-06: Verifica si el Jugador 2 (O) alineó 3 símbolos en fila, columna o diagonal
    if (
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
        print("Ha ganado el Jugador 2")
        return estado

    # RF-07: Si las 9 casillas están llenas sin ganador, declara empate; si no, continúa
    if (
        c1 != "1" and c2 != "2" and c3 != "3"
        and c4 != "4" and c5 != "5" and c6 != "6"
        and c7 != "7" and c8 != "8" and c9 != "9"
    ):
        estado = "empate"
        print("¡Empate! El tablero está lleno.")
    else:
        estado = "continua"
        print("La partida continúa.")

    return estado


# Estado inicial de ejemplo para verificar fin de partida (RF-06, RF-07)
# Valores iniciales extraídos de DF3_fin.rap
c1, c2, c3 = "X", "O", "X"
c4, c5, c6 = "O", "O", "O"
c7, c8, c9 = "O", "X", "X"

if __name__ == "__main__":
    print("DF2 · Validación de una jugada")
    mostrar_tablero(TABLERO_DF2)
    posicion = pedir_jugada(TABLERO_DF2, JUGADOR_DF2)
    print(f"Jugada válida en la casilla {posicion}.")

    print("--- Evaluación DF3 (Estado inicial de ejemplo) ---")
    resultado_df3 = evaluar_fin_partida(c1, c2, c3, c4, c5, c6, c7, c8, c9)
    print("Estado resultante:", resultado_df3)

    # Pruebas de los 4 resultados posibles de DF3 (RF-06, RF-07)
    print("\n--- Pruebas de los 4 resultados posibles (DF3) ---")
    print("1. Caso gana Jugador 1:", evaluar_fin_partida("X", "X", "X", "4", "O", "6", "7", "8", "O"))
    print("2. Caso gana Jugador 2:", evaluar_fin_partida("X", "O", "X", "O", "O", "O", "O", "X", "X"))
    print("3. Caso empate:", evaluar_fin_partida("X", "O", "X", "X", "O", "O", "O", "X", "X"))
    print("4. Caso continúa:", evaluar_fin_partida("X", "O", "3", "4", "X", "6", "7", "8", "O"))
