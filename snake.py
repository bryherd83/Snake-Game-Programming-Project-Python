"""
snake.py
Stores the snake body as a list of (row, col) grid positions.
Handles movement, growth, and direction changes.
"""


class Snake:
    """A snake on the game grid made of (row, col) segments."""
    def __init__(self, start_row, start_col):
        """Creates a 3-segment snake at the given position, moving right."""
        # Start with 3 segments so the snake can be seen as the game starts.
        self._body = [(start_row, start_col),
                      (start_row, start_col - 1),
                      (start_row, start_col - 2)]
        # Start moving right
        self._dir_row = 0
        self._dir_col = 1

    def move(self):
        """Moves the snake one step in the current direction."""
        head_row, head_col = self._body[0]
        self._body.insert(0, (head_row + self._dir_row, head_col + self._dir_col))
        self._body.pop()

    def grow(self):
        """Grows the snake by duplicating the tail segment."""
        self._body.append(self._body[-1])

    def set_direction(self, d_row, d_col):
        """
        Sets the direction. Prevents reversing directly into the body.
        Called from display.py on keypress.
        """
        # Ignore if trying to reverse
        if d_row == -self._dir_row and d_col == -self._dir_col:
            return
        self._dir_row = d_row
        self._dir_col = d_col

    # Getters 

    @property
    def body(self):
        """Returns the full list of body segments as (row, col) pairs."""
        return self._body

    @property
    def head(self):
        """Returns the head position as (row, col)."""
        return self._body[0]

    @property
    def dir_row(self):
        """Returns the row direction (-1 up, 0 none, 1 down)."""
        return self._dir_row

    @property
    def dir_col(self):
        """Returns the column direction (-1 left, 0 none, 1 right)."""
        return self._dir_col
