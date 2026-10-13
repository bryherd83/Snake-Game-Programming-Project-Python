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
        self.respawn(board_rows, board_cols, snake_body)

    def respawn(self, board_rows, board_cols, snake_body=None):
        """
        Moves the food to a new random cell that the snake is not in.
        board_rows: total rows on the board (including walls)
        board_cols: total cols on the board (including walls)
        snake_body: snake segments to avoid; leave as None if not needed
        """
        # Python does not have a do while, so loop and break on a good spot
        while True:
            # Keep food inside walls
            new_row = random.randint(1, board_rows - 2)
            new_col = random.randint(1, board_cols - 2)
            if not self._is_on_snake(new_row, new_col, snake_body):
                break

        self._row = new_row
        self._col = new_col

    def _is_on_snake(self, r, c, snake_body):
        """Returns True if the given cell has the snake in it."""
        if snake_body is None:
            return False
        return (r, c) in snake_body

    # Getters

    @property
    def row(self):
        """Returns the food's row on the grid."""
        return self._row

    @property
    def col(self):
        """Returns the food's col on the grid."""
        return self._col
