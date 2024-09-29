# TP2: Implementación del Juego Buscaminas con IA

Este trabajo práctico consiste en la implementación del clásico juego de **Buscaminas**, incluyendo una clase de Inteligencia Artificial (IA) que juega de manera autónoma. La IA intenta resolver el tablero de buscaminas utilizando deducción lógica para evitar minas y ganar el juego.

## Descripción

El juego de Buscaminas se juega en un tablero rectangular donde algunas celdas contienen minas. El objetivo del jugador es descubrir todas las celdas vacías sin detonar ninguna mina. El número de minas vecinas de una celda revelada se muestra como una pista, y la IA del proyecto intenta utilizar esta información para deducir la posición de las minas.

Este proyecto contiene una clase principal que maneja la lógica del juego y una clase que implementa una IA para resolverlo.

## Funcionalidades Principales

- **Clase `Minesweeper`**: Representa el tablero de juego, inicializa el tablero con minas aleatorias, maneja las interacciones del usuario y verifica el estado del juego.
- **Clase `MinesweeperAI`**: Implementa una IA que intenta deducir la ubicación de las minas utilizando reglas lógicas basadas en las pistas numéricas de las celdas descubiertas.
- **Interacción Humano-Computadora**: El usuario puede jugar manualmente, o permitir que la IA juegue de forma automática.
- **Determinación de Ganador/Perdedor**: La IA o el usuario ganan si descubren todas las celdas seguras sin detonar una mina. Pierden si descubren una mina.

## Estructura del Código

- `Minesweeper.__init__(height, width, mines)`: Inicializa un nuevo tablero de Buscaminas con las dimensiones y cantidad de minas especificadas.
- `Minesweeper.print()`: Imprime el estado actual del tablero.
- `Minesweeper.is_mine(cell)`: Devuelve `True` si la celda contiene una mina, `False` en caso contrario.
- `Minesweeper.nearby_mines(cell)`: Devuelve el número de minas adyacentes a la celda dada.
- `MinesweeperAI.add_knowledge(cell, count)`: Agrega nuevo conocimiento a la IA después de descubrir una celda y el número de minas cercanas.
- `MinesweeperAI.make_safe_move()`: Devuelve una celda segura para moverse, si existe.
- `MinesweeperAI.make_random_move()`: Hace un movimiento aleatorio si no se puede deducir un movimiento seguro.

## Ejecución

### Dependencias

El proyecto no requiere librerías externas, solo el uso de las librerías estándar de Python.

### Cómo ejecutar el programa

1. Clona el repositorio o descarga los archivos necesarios.
2. Navega a la carpeta `Tp2/minesweeper` en tu terminal.
3. Ejecuta el archivo `runner.py` para iniciar el juego de Buscaminas:

```bash
python runner.py
```

Puedes interactuar con el juego manualmente o permitir que la IA realice los movimientos.

## Ejemplo de uso

Una vez iniciado el juego, puedes jugar manualmente seleccionando celdas o dejar que la IA intente resolver el tablero. La IA irá deduciendo la ubicación de las minas basándose en las celdas descubiertas.

## Notas

- El tamaño predeterminado del tablero es de 8x8 con 8 minas, pero esto puede configurarse al iniciar la clase `Minesweeper`.
- La IA no siempre gana, pero intenta utilizar toda la información disponible para evitar las minas. En algunos casos, tendrá que hacer movimientos aleatorios si no puede deducir la ubicación de una mina con certeza.
