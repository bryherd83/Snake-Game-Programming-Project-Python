"""
snake_food.py
Tracks the food position as (row, col) grid coords.
Respawns in a random empty cell when the snake eats the food.
"""

import random


class SnakeFood:
    """A piece of food on the game grid that the snake can eat."""

    def __init__(self, board_rows, board_cols, snake_body=None):
        """Creates the food and places it in a random empty cell."""
        # No position until respawn() finds an empty cell
        self._row = None
        self._col = None
        self.respawn(board_rows, board_cols, snake_body)

    def respawn(self, board_rows, board_cols, snake_body=None):
        """
        Moves the food to a new random cell that the snake is not in.
        board_rows: total rows on the board (including walls)
        board_cols: total cols on the board (including walls)
        snake_body: snake segments to avoid; leave as None if not needed
        Returns True if the food moved, False if the board has no empty cell.
        """
        # A set makes each "is the snake here?" check fast, even for a long snake
        occupied = set(snake_body) if snake_body else set()
        # List every empty cell inside the walls, then pick one at random.
        # This never loops forever, even when the snake fills the board.
        free_cells = [(r, c)
                      for r in range(1, board_rows - 1)
                      for c in range(1, board_cols - 1)
                      if (r, c) not in occupied]
        # No empty cell left: keep the food where it is and tell the caller
        if not free_cells:
            return False
        self._row, self._col = random.choice(free_cells)
        return True

    # Getters

    @property
    def row(self):
        """Returns the food's row on the grid."""
        return self._row

    @property
    def col(self):
        """Returns the food's col on the grid."""
        return self._col
