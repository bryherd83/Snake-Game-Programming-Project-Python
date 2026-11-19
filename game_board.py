"""
game_board.py
The play area: board size, the snake, the food, and the game rules.
Has no drawing or keyboard code, so it can change without touching Display.
"""


class GameBoard:
    """
    Owns the board size, the snake, and the food (composition: a board
    must have both), and runs the game one step at a time.
    """

    def __init__(self, rows, cols, snake, food):
        """
        Creates a rows x cols board that plays with the given snake and food.
        snake and food are built in main.py and passed in (dependency
        injection), so tests can hand in their own and GameBoard does not
        depend on how they are made.
        """
        self._rows = rows
        self._cols = cols
        self._snake = snake
        self._food = food
        self._game_over = False

    def step(self):
        """
        Moves the snake one step, ends the game on a crash, and eats food.
        Same order as actionPerformed in Display.java.
        """
        if self._game_over:
            return
        self._snake.move()
        if self._is_outside(*self._snake.head) or self._snake.hits_self():
            self._game_over = True
            return
        # Head on the food: grow and move the food to a new empty cell
        if self._snake.head == (self._food.row, self._food.col):
            self._snake.grow()
            self._food.respawn(self._rows, self._cols, self._snake.body)

    def steer(self, d_row, d_col):
        """Turns the snake, unless the game is over."""
        if not self._game_over:
            self._snake.set_direction(d_row, d_col)

    def _is_outside(self, row, col):
        """Returns True if (row, col) is off the board."""
        return not (0 <= row < self._rows and 0 <= col < self._cols)

    # Getters

    @property
    def rows(self):
        """Returns the number of rows on the board."""
        return self._rows

    @property
    def cols(self):
        """Returns the number of columns on the board."""
        return self._cols

    @property
    def snake_body(self):
        """Returns the snake's cells as a tuple of (row, col), head first."""
        return self._snake.body

    @property
    def snake_direction(self):
        """Returns the snake's direction as (row step, col step)."""
        return self._snake.dir_row, self._snake.dir_col

    @property
    def food_position(self):
        """Returns the food's (row, col), or None if it has no cell yet."""
        if self._food.row is None:
            return None
        return self._food.row, self._food.col

    @property
    def game_over(self):
        """Returns True once the snake has crashed."""
        return self._game_over
