 # PROYECTO INTEGRADOR - TRES EN RAYA
# FASE 3 - ENTORNO DE TRABAJO
# DF1: MENU PRINCIPAL
# RF-01: Mostrar el menu principal
# RF-08: Permitir salir del programa

opcion = ""

while opcion != "SALIR":

    print("\n===== TRES EN RAYA =====")
    print("1. JUGAR")
    print("2. SALIR")

    opcion = input("Elija una opcion: ").strip().upper()

    if opcion == "1" or opcion == "JUGAR":

        print("\nHas seleccionado JUGAR.")
        print("Esta funcionalidad estara disponible proximamente.")

    elif opcion == "2" or opcion == "SALIR":

        opcion = "SALIR"
        print("\nGracias por jugar Tres en Raya.")

    else:

        print("\nOpción no válida. Ingrese JUGAR o SALIR.")