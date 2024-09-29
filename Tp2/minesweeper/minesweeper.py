import itertools
import random


class Minesweeper():
    
    def __init__(self, height=8, width=8, mines=8):
        """
        Inicializa un nuevo juego de Buscaminas con las dimensiones dadas.
        Args:
            height (int): Altura del tablero.
            width (int): Ancho del tablero.
            mines (int): Número de minas en el tablero.
        Atributos:
            height (int): Altura del tablero.
            width (int): Ancho del tablero.
            mines (set): Conjunto de coordenadas de las minas en el tablero.
            board (list): Matriz que representa el tablero con minas.
            mines_found (set): Conjunto de coordenadas de las minas encontradas.
        """
        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Imprime una representación del juego en texto mostrando las minas.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Devuelve el número de minas adyacentes a una celda dada, sin incluir la celda en sí.

        Args:
            cell (tuple): Coordenadas (fila, columna) de la celda.

        Returns:
            int: Número de minas adyacentes a la celda.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Comprueba si se han encontrado todas las minas en el tablero.

        Returns:
            bool: True si se han encontrado todas las minas, False en caso contrario.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Clase que representa una sentencia lógica sobre el juego del Buscaminas.
    Una sentencia consta de un conjunto de celdas del tablero 
    y el número de minas en esas celdas.
    """

    def __init__(self, cells, count):
        """
        Inicializa una nueva sentencia con el conjunto de celdas y el el número de minas.
        Args:
            cells (set): Conjunto de coordenadas de celdas del tablero.
            count (int): Número de minas en las celdas dadas.
        """
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Devuelve el conjunto de todas las celdas en la sentencia que se sabe que son minas.

        Returns:
            set: Conjunto de celdas conocidas como minas.
        """
        #solo puedo estar seguro si las celdas contienen minas 
        # si la sentencia contiene el mismo numero de celdas que el contador de minas
        #EJ: A, B, C = 1
        #No puedo afirmar nada dado que cualquiera de las 3 podria contener la mina, 
        # por lo que devuelvo un set vacio
        if len(self.cells) == self.count:
            return self.cells.copy()
        return set()

    def known_safes(self):
        """
        Devuelve el conjunto de todas las celdas en la sentencia que se sabe que son seguras.

        Returns:
            set: Conjunto de celdas conocidas como seguras.
        """
        #solo puedo estar seguro si las celdas son seguras si el contador de minas es 0
        if self.count == 0:
            return self.cells.copy()
        return set()

    def mark_mine(self, cell):
        """
        Actualiza la representación interna del conocimiento 
        dado que puedo afirmar que una celda es una mina.

        Args:
            cell (tupla): Coordenadas (fila, columna) de la celda conocida como mina.
        """
        if cell in self.cells:
            self.cells.remove(cell)
            self.count -= 1

    def mark_safe(self, cell):
        """
        Actualiza la representación interna del conocimiento 
        dado que puedo afirmar que una celda es segura.

        Args:
            cell (tupla): Coordenadas (fila, columna) de la celda conocida como segura.
        """
        if cell in self.cells:
            self.cells.remove(cell)


class MinesweeperAI():
    """
    Clase que representa una IA que puede jugar al Buscaminas.
    """

    def __init__(self, height=8, width=8):
        """
        Inicializa la IA jugadora de Buscaminas.

        Args:
            height (int): Altura del tablero.
            width (int): Ancho del tablero.

        Atributos:
            height (int): Altura del tablero.
            width (int): Ancho del tablero.
            moves_made (set): Conjunto de celdas donde se ha hecho un movimiento.
            mines (set): Conjunto de celdas conocidas como minas.
            safes (set): Conjunto de celdas conocidas como seguras.
            knowledge (list): Lista de sentencias lógicas sobre el juego.
        """
        
        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marca una celda como mina y actualiza todo el conocimiento.

        Args:
            cell (tupla): Coordenadas (fila, columna) de la celda conocida como mina.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)
        #print("mina encontrada en " + str(cell[0]+1) + str(cell[1]+1))

    def mark_safe(self, cell):
        """
        Marca una celda como segura y actualiza todo el conocimiento.

        Args:
            cell (tupla): Coordenadas (fila, columna) de la celda conocida como segura.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)


    def add_knowledge(self, cell, count):
        """
        Se llama cuando el tablero Buscaminas nos dice, para una celda segura determinada, 
        cuántas celdas vecinas tienen minas.

        Esta función:
            1) marca la celda como un movimiento que se ha realizado
            2) marca la celda como segura
            3) agrega una nueva oración a la base de conocimientos de la IA
               basado en el valor de "celda" y "recuento"
            4) marca celdas adicionales como seguras o como minas
               si se puede concluir basándose en la base de conocimientos de la IA
            5) agrega nuevas oraciones a la base de conocimientos de la IA
               si pueden inferirse del conocimiento existente
        """
        # 1. Marca la celda como un movimiento realizado y como segura
        self.moves_made.add(cell)
        self.mark_safe(cell)
    
        # 2. Identificar las celdas vecinas
        nearby_cells = set(
            (i, j) for i in range(max(0, cell[0] - 1), min(self.height, cell[0] + 2))
            for j in range(max(0, cell[1] - 1), min(self.width, cell[1] + 2))
            if (i, j) != cell and (i, j) not in self.safes
        )

        # 3. Agregar nueva sentencia
        new_sentence = Sentence(nearby_cells, count)
        self.knowledge.append(new_sentence)

        # 4. Actualizar conocimiento de minas y celdas seguras
        self._update_knowledge()

        # 5. Generar nuevas sentencias a partir de las existentes
        self._infer_new_sentences()

    def _update_knowledge(self):
        """
        Actualiza el conocimiento de la IA basado en las celdas seguras y minas conocidas.
        """
        # Actualizar celdas seguras y minas conocidas
        for sentence in self.knowledge:
            for safe_cell in sentence.known_safes():
                self.mark_safe(safe_cell)
            for mine_cell in sentence.known_mines():
                self.mark_mine(mine_cell)

        # Eliminar sentencias vacías
        self.knowledge = [sentence for sentence in self.knowledge if sentence.cells]

    def _infer_new_sentences(self):
        """
        Genera nuevas sentencias a partir de las actuales, identificando subconjuntos entre ellas.
        """
        new_sentences = []
        for sentence1 in self.knowledge:
            for sentence2 in self.knowledge:
                if sentence1 == sentence2:
                    continue
                # Si una sentencia es subconjunto de otra, generar nueva sentencia
                if sentence1.cells.issubset(sentence2.cells):
                    inferred_cells = sentence2.cells - sentence1.cells
                    inferred_count = sentence2.count - sentence1.count
                    new_sentence = Sentence(inferred_cells, inferred_count)

                    if new_sentence not in self.knowledge and new_sentence not in new_sentences:
                        new_sentences.append(new_sentence)
        
        # Agregar nuevas sentencias al conocimiento y verificar si generan nueva información
        for new_sentence in new_sentences:
            self.knowledge.append(new_sentence)
            self._update_knowledge()

    

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        # Crear una lista de celdas seguras que no se han movido
        safe_moves = []
        for cell in self.safes:
            if cell not in self.moves_made:
                safe_moves.append(cell)
        
        # Si hay celdas seguras, elegir una aleatoriamente
        if safe_moves:
            return random.choice(safe_moves)
        
        # Si no hay movimientos seguros, retornar None
        return None

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        # Crear una lista de celdas que no se han movido y no son minas
        possible_moves = []
        for i in range(self.height):
            for j in range(self.width):
                cell = (i, j)
                if cell not in self.moves_made and cell not in self.mines:
                    possible_moves.append(cell)
        
        # Si hay movimientos posibles, elegir uno aleatoriamente
        if possible_moves:
            return random.choice(possible_moves)
        
        # Si no hay movimientos posibles, retornar None
        return None