from math import floor

# DF2: Validación de la jugada (RF-05)
tablero = "X234O6789"
turno = 1
casilla_num = 0
es_valida = False

if turno == 1:
    simbolo_actual = "X"
else:
    simbolo_actual = "O"

while not es_valida:
    entrada = input("Ingrese una casilla del 1 al 9: ")

    # Si se escribe una letra, el 0 lleva al aviso de posición inválida.
    try:
        casilla_num = float(entrada)
    except ValueError:
        casilla_num = 0

    if 1 <= casilla_num <= 9 and casilla_num == floor(casilla_num):
        casilla_num = int(casilla_num)

        # La casilla 1 del diagrama corresponde al índice 0 en Python.
        contenido_casilla = tablero[casilla_num - 1]

        if contenido_casilla != "X" and contenido_casilla != "O":
            es_valida = True
            print("Jugada valida. La posicion esta libre.")
        else:
            es_valida = False
            print("Casilla ocupada. Intente nuevamente.")
    else:
        print("Posicion invalida. Ingrese un numero entero del 1 al 9.")
        es_valida = False

print("Posicion aceptada:", casilla_num)