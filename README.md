# Tres en raya · Three Code
Lógica de Programación, UIDE · Paralelo 01-SIN-B · Fase 3

Dos personas comparten un tablero de nueve casillas. El Jugador 1 usa X y el Jugador 2 usa O. Gana quien complete una fila, columna o diagonal. Esta fase presenta el menú y dos pruebas independientes de la lógica. El bucle de turnos y la conexión en red corresponden a la Fase 4.

## Integrantes y responsabilidades acordadas

| Integrante | Responsabilidad |
| --- | --- |
| Emily Ashqui | Menú DF1, archivos de servidor y cliente, diagramas de RAPTOR |
| Meir Fernández | Validación DF2, organización de GitHub y edición del video |
| Javier Paguay | Fin de partida DF3, pruebas de resultados, README y licencia |

## Ejecución

Con Python 3 instalado, abre una terminal en la carpeta que contiene los cuatro archivos Python y ejecuta:

```sh
python juego.py
```

Escribe 1 para ver el mensaje de Jugar. El menú vuelve a aparecer. Escribe 2 para salir. Luego ejecuta:

```sh
python game_logic.py
```

En DF2, prueba A, 0, 5 y 2, presionando Enter después de cada valor. Los dos primeros se rechazan por formato o rango, la casilla 5 está ocupada y la 2 está libre. DF3 evalúa después su propio ejemplo y ejecuta los cuatro casos de Javier. En Windows también puedes usar la orden py en lugar de python.

## Del diagrama al código

| Diagrama de la Fase 2 | Archivo y líneas | Qué cambió |
| --- | --- | --- |
| DF1 · Menú | juego.py, 7–29 | La lectura de la opción pasa a input. El ciclo while vuelve a mostrar el menú y termina cuando la opción vale SALIR. |
| DF2 · Validación | game_logic.py, 3–28 y 89–93 | La entrada se comprueba como texto antes de convertirla a entero. La posición visible se reduce en uno para consultar el tablero. continue vuelve a pedir la jugada al mismo jugador. |
| DF3 · Fin de la partida | game_logic.py, 34–87 y 95–104 | Se conservan las nueve variables y las ocho combinaciones de victoria para cada símbolo. Se comprueba la victoria antes del empate. Si quedan espacios y nadie ganó, la partida continúa. |

Los tres archivos originales están en [diseno](diseno/). En [DF2_validacion.rap](diseno/DF2_validacion.rap), el tablero arranca en `X234O6789` con turno 1. RAPTOR lee `casilla_num`, comprueba el rango y usa `floor` para comprobar que sea entero. Python lee el texto antes de convertirlo para manejar también entradas como A, caso marcado con una cruz en la sección 3.1 de la Fase 2. En RAPTOR la bandera `es_valida` permite salir del ciclo. En Python, `return posicion` termina la validación cuando la casilla está libre.

El estado inicial de [DF3_fin.rap](diseno/DF3_fin.rap) equivale a `XOXOOOOXX`. O completa la fila 4–5–6, por lo que el resultado es victoria del Jugador 2 incluso con el tablero lleno. Este es un estado fijo para probar la decisión.

Tras aceptar una casilla en DF2, las cuatro pruebas de DF3 imprimen gana_j1, gana_j2, empate y continua, en ese orden.

## Video explicativo

Enlace: [pendiente de grabación y publicación por el equipo].

## Autoría, créditos y licencia

Three Code definió el juego, las reglas, los requisitos y el reparto de tareas. Emily aportó el menú, el cliente, el servidor y los diagramas. Javier aportó DF3 y sus cuatro pruebas. ChatGPT (OpenAI) ayudó a traducir DF2, integrar los archivos y actualizar el README. Revisión y cambios realizados por los integrantes en Fase 3: [completar con las pruebas y modificaciones que el equipo realmente haya hecho].

En la Fase 2 el equipo declaró el uso de Gemini como apoyo para revisar condiciones de RAPTOR, organizar la prueba de escritorio y revisar las tablas. En la Fase 1 el equipo declaró el uso de Gemini para revisar la redacción y la correspondencia de requisitos y escenarios con la rúbrica. La implementación de Fase 3 solo usa funciones incorporadas de Python. No se incorporaron fragmentos de código de terceros, paquetes externos ni recursos visuales en esta versión.

El código se distribuye bajo la licencia de código abierto MIT. El texto de la licencia se encuentra en [LICENSE](LICENSE).
