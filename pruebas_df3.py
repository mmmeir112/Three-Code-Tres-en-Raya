"""Comprueba la salida del programa usando cuatro estados independientes."""
from pathlib import Path
import subprocess
import sys

programa = Path(__file__).with_name("game_logic.py")
casos = [
    ("XXXOO6789", "¡Ha ganado el Jugador 1!"),
    ("XX3OOO7X9", "¡Ha ganado el Jugador 2!"),
    ("XOXXOOOXX", "¡Empate! El tablero está lleno."),
    ("X23O56789", "La partida continúa."),
]
for tablero, esperado in casos:
    # El 4 es una entrada válida si se prueba la versión integrada con DF2.
    ejecucion = subprocess.run(
        [sys.executable, "-X", "utf8", str(programa), tablero],
        input="4\n", capture_output=True, encoding="utf-8", check=True,
    )
    obtenido = ejecucion.stdout.splitlines()[-1]
    if obtenido != esperado:
        sys.exit(f"Error en {tablero}. Se esperaba {esperado} y se obtuvo {obtenido}")
    print(f"{tablero[:3]} / {tablero[3:6]} / {tablero[6:]} → {obtenido}")
print("4 de 4 pruebas correctas.")
