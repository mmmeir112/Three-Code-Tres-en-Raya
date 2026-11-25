# Tres en raya

Proyecto integrador de primer nivel · Lógica de Programación · UIDE · Paralelo B  
**Equipo Three Code · Fase 3 · Entorno de trabajo**

Dos jugadores comparten un tablero de nueve casillas. El Jugador 1 usa X y el Jugador 2 usa O. Gana quien completa una fila, columna o diagonal. La Fase 3 implementa el menú y dos demostraciones independientes del diseño en RAPTOR: la validación de una jugada y la evaluación del fin de la partida. El modo local por turnos y la conexión en red LAN corresponden a la Fase 4.

## Integrantes

- Emily Ashqui
- Meir Fernández
- Javier Paguay

## Prerrequisitos

- **Python 3.14** (cualquier versión 3.14.x).
- Una terminal abierta en la carpeta del proyecto. En Windows se puede usar PowerShell.
- El proyecto utiliza funciones incorporadas de Python. No requiere instalar paquetes con `pip`.

Comprueba qué versión ejecutará la terminal:

```console
python --version
```

El resultado debe comenzar por `Python 3.14.`. Si tienes varias versiones en Windows, prueba `py -3.14 --version` y usa `py -3.14` en lugar de `python` en los comandos siguientes.

## Cómo ejecutarlo

Desde la raíz del **repositorio grupal**, ejecuta cada programa por separado.

**1. Menú principal**

```console
python juego.py
```

Escribe `1` para elegir Jugar y volver al menú. Escribe `2` para salir.

**2. Validación y fin de la partida**

```console
python game_logic.py
```

En DF2, el tablero de ejemplo es `X23 / 4O6 / 789`. Introduce `A` para obtener el aviso de formato, `5` para probar una casilla ocupada y `4` para aceptar una casilla libre. El turno sigue perteneciendo al Jugador 1 durante los reintentos.

A continuación, DF3 evalúa su propio tablero de ejemplo, `XOX / OOO / OXX`. El resultado es **«¡Ha ganado el Jugador 2!»** porque O ocupa las casillas 4, 5 y 6. Aunque el tablero está lleno, la fila ganadora tiene prioridad sobre el empate.

## Estructura del repositorio

| Archivo | Qué hace | Estado |
|---|---|---|
| `juego.py` | Presenta Jugar y Salir. Repite el menú mientras el usuario siga dentro del programa. | Menú terminado |
| `game_logic.py` | Valida la entrada y la ocupación de la casilla (DF2). Evalúa victoria, empate o continuación (DF3). | DF2 y DF3 terminados |
| `server.py` | Describe el servidor del Jugador 1, que guardará el tablero y validará las jugadas. | Comentario de Fase 3 |
| `client.py` | Describe el cliente del Jugador 2, que enviará jugadas y mostrará el resultado. | Comentario de Fase 3 |
| `diseno/` | Contiene los originales de DF1, DF2 y DF3 en formato RAPTOR. | Tres diagramas incluidos |
| `pruebas_df3.py` | Ejecuta los cuatro escenarios de DF3 y compara los mensajes obtenidos con los esperados. | Cuatro casos comprobados |
| `LICENSE` | Contiene el texto completo de la licencia MIT. | Incluido |

## Del diseño al código

Las líneas corresponden a la versión integrada de Three Code.

| Diagrama de la Fase 2 | Archivo y líneas | Qué cambió al traducirlo |
|---|---|---|
| DF1 · Partida completa (menú) · RF-01 y RF-08 | `juego.py`, 1–11 | El bucle del menú pasó a `while`. Jugar muestra un mensaje y Salir termina la repetición. |
| DF2 · Validación de la jugada · RF-05 | `game_logic.py`, 3–20 | Se lee la casilla como texto antes de convertirla a entero. La posición 1 corresponde al índice 0. Si falla el formato o la casilla está ocupada, se vuelve a pedir la jugada al mismo jugador. |
| DF3 · Fin de la partida · RF-06 y RF-07 | `game_logic.py`, 22–76 | Se conservan las variables c1 a c9. Los tres rombos pasan a una cadena de `if`, `elif` y `else`. Se comprueban las ocho líneas de X, luego las ocho de O y finalmente si cada casilla cambió su número por una marca. Cada rama asigna a `estado` el mismo valor que en RAPTOR. |

### Pruebas de DF3

Cada grupo de tres caracteres representa una fila. Los números identifican las casillas libres.

| Tablero de prueba | Condición comprobada | Resultado obtenido |
|---|---|---|
| `XXX / OO6 / 789` | X completa la primera fila. | ¡Ha ganado el Jugador 1! |
| `XX3 / OOO / 7X9` | O completa la segunda fila. | ¡Ha ganado el Jugador 2! |
| `XOX / XOO / OXX` | Las nueve casillas están ocupadas y nadie tiene línea. | ¡Empate! El tablero está lleno. |
| `X23 / O56 / 789` | Quedan casillas libres y nadie tiene línea. | La partida continúa. |

Para repetir los cuatro casos y comparar automáticamente cada salida con el resultado esperado:

```console
python pruebas_df3.py
```

## Video explicativo

**Enlace al video del equipo:** pendiente de incorporar después de la grabación.

En un máximo de cinco minutos, los tres integrantes demostrarán el menú, una jugada inválida y el fin de la partida, y explicarán cómo se tradujo uno de los diagramas de RAPTOR a Python.

## Licencia

Three Code distribuye el proyecto bajo la licencia de código abierto MIT. El texto completo está en [LICENSE](LICENSE).

## Declaración de autoría

El diseño del juego y los diagramas de RAPTOR son obra del equipo Three Code. La implementación de esta fase se basa en ese diseño y se elaboró con la asistencia de IA descrita en los créditos. La responsabilidad asignada a Javier Paguay comprende DF3, las pruebas de sus cuatro resultados, el README y la licencia.

## Créditos

| Recurso (código, librería, imagen…) | Autor o fuente | Dónde se usa | Licencia |
|---|---|---|---|
| Diagramas de la Fase 2 | Three Code | Carpeta `diseno/` y diseño de DF1, DF2 y DF3 | MIT del proyecto |
| Intérprete y funciones incorporadas de Python | Python Software Foundation y colaboradores | Entrada por teclado, comparaciones y salida en consola | Python Software Foundation License |
| Plantilla del README de la Fase 3 | Docente de Lógica de Programación, UIDE | Organización de este documento | Material del curso, sin licencia indicada |

La interfaz es de texto. El proyecto no incorpora imágenes, sonidos ni bibliotecas externas.

### Uso de IA

| Herramienta | Para qué la usamos | Qué revisamos o cambiamos nosotros |
|---|---|---|
| Gemini · Fase 2 | Apoyo con la sintaxis en RAPTOR, la prueba de escritorio y las tablas. | Según el informe de la Fase 2, el equipo probó los cuatro resultados y ajustó los estados de ejemplo, los mensajes y los nombres de las variables. |
| ChatGPT · Fase 3 | Apoyo en la traducción a Python, la ejecución de las pruebas y la redacción del README. | Javier aportó los archivos originales y la plantilla del docente, y especificó Python 3.14 y pidió conservar las decisiones de RAPTOR sin definir funciones. |
