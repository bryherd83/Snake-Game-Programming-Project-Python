"""
snake.py
Stores the snake body as (row, col) grid positions.
Handles movement, growth, and direction changes.
"""

from collections import deque


class Snake:
    """A snake on the game grid made of (row, col) segments."""
    def __init__(self, start_row, start_col):
        """Creates a 3-segment snake at the given position, moving right."""
        # Start with 3 segments so the snake can be seen as the game starts.
        # deque: adding a head and removing the tail are both fast,
        # no matter how long the snake gets (a list shifts every item)
        self._body = deque([(start_row, start_col),
                            (start_row, start_col - 1),
                            (start_row, start_col - 2)])
        # Same cells as a set, so "is this cell part of the snake?" is fast
        self._cells = set(self._body)
        # Steps left where the tail stays put (that is how the snake grows)
        self._grow_pending = 0
        self._hit_self = False
        # Start moving right
        self._dir_row = 0
        self._dir_col = 1
        # Direction of the last step taken; used to block reversing
        self._moved_dir = (0, 1)

    def move(self):
        """Moves the snake one step in the current direction."""
        head_row, head_col = self._body[0]
        new_head = (head_row + self._dir_row, head_col + self._dir_col)
        if self._grow_pending:
            self._grow_pending -= 1
        else:
            # Tail leaves first, so the head may move into the old tail cell
            self._cells.discard(self._body.pop())
        self._hit_self = new_head in self._cells
        self._body.appendleft(new_head)
        self._cells.add(new_head)
        self._moved_dir = (self._dir_row, self._dir_col)

    def grow(self):
        """Grows the snake by one segment on its next move."""
        self._grow_pending += 1

    def set_direction(self, d_row, d_col):
        """
        Sets the direction. Prevents reversing directly into the body.
        Called from GameBoard.steer() when a movement key is pressed.
        """
        # Ignore if trying to reverse. Compare with the last step taken, not
        # the last key, so two quick keys (up then left while going right)
        # cannot turn the snake back into itself before it moves.
        if (d_row, d_col) == (-self._moved_dir[0], -self._moved_dir[1]):
            return
        self._dir_row = d_row
        self._dir_col = d_col

    def hits_self(self):
        """Returns True if the last move put the head on the snake's body."""
        return self._hit_self

    # Getters 

    @property
    def body(self):
        """
        Returns the body segments as a tuple of (row, col) pairs, head first.
        A tuple is a copy that cannot be changed, so code outside Snake
        cannot move or delete segments by accident (encapsulation).
        """
        return tuple(self._body)

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
