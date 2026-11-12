"""
test_game.py
Unit tests for Snake, SnakeFood, and GameBoard. No window is needed.
Run with:  python -m unittest
"""

import unittest

from game_board import GameBoard
from snake import Snake
from snake_food import SnakeFood


class SnakeTests(unittest.TestCase):
    """Tests for movement, growth, turning, and self-collision."""

    def test_move_keeps_length(self):
        """A plain move shifts the snake one cell right and keeps 3 segments."""
        snake = Snake(5, 5)
        snake.move()
        self.assertEqual(snake.head, (5, 6))
        self.assertEqual(len(snake.body), 3)

    def test_grow_adds_one_segment_on_next_move(self):
        """grow() makes the next move keep the tail, so length goes 3 to 4."""
        snake = Snake(5, 5)
        snake.grow()
        snake.move()
        self.assertEqual(len(snake.body), 4)

    def test_body_is_read_only(self):
        """body returns a tuple, so callers cannot change the snake."""
        self.assertIsInstance(Snake(5, 5).body, tuple)

    def test_cannot_reverse_with_two_quick_keys(self):
        """Up then left while moving right must not turn the snake back."""
        snake = Snake(5, 5)
        snake.set_direction(-1, 0)
        snake.set_direction(0, -1)
        self.assertEqual((snake.dir_row, snake.dir_col), (-1, 0))

    def test_head_may_enter_cell_tail_is_leaving(self):
        """A 4-long snake circling a 2x2 square never hits itself."""
        snake = Snake(5, 5)
        snake.grow()
        snake.move()
        for d_row, d_col in [(1, 0), (0, -1), (-1, 0)]:
            snake.set_direction(d_row, d_col)
            snake.move()
            self.assertFalse(snake.hits_self())

    def test_hits_self(self):
        """A 5-long snake turning in a 2x2 square runs into its body."""
        snake = Snake(5, 5)
        snake.grow()
        snake.grow()
        snake.move()
        snake.move()
        for d_row, d_col in [(1, 0), (0, -1), (-1, 0)]:
            snake.set_direction(d_row, d_col)
            snake.move()
        self.assertTrue(snake.hits_self())


class SnakeFoodTests(unittest.TestCase):
    """Tests for food placement."""

    def test_spawns_inside_walls_and_off_snake(self):
        """With one free cell left inside the walls, food must go there."""
        taken = [(r, c) for r in range(1, 4) for c in range(1, 4) if (r, c) != (3, 3)]
        food = SnakeFood(5, 5, taken)
        self.assertEqual((food.row, food.col), (3, 3))

    def test_full_board_returns_false(self):
        """respawn() returns False and keeps its spot when no cell is free."""
        food = SnakeFood(5, 5)
        spot = (food.row, food.col)
        full = [(r, c) for r in range(1, 4) for c in range(1, 4)]
        self.assertFalse(food.respawn(5, 5, full))
        self.assertEqual((food.row, food.col), spot)


class GameBoardTests(unittest.TestCase):
    """Tests for the game rules in GameBoard.step()."""

    def place_food_ahead(self, board):
        """Moves the food to the cell right in front of the snake's head."""
        row, col = board.snake.head
        board.food.respawn(board.rows, board.cols,
                           [(r, c) for r in range(board.rows) for c in range(board.cols)
                            if (r, c) != (row, col + 1)])

    def test_eating_grows_snake_and_moves_food(self):
        """Stepping onto the food grows the snake and puts the food elsewhere."""
        board = GameBoard(24, 32)
        self.place_food_ahead(board)
        board.step()
        board.step()
        self.assertEqual(len(board.snake.body), 4)
        self.assertNotIn((board.food.row, board.food.col), board.snake.body)

    def test_leaving_board_ends_game(self):
        """Running right off the board sets game_over and ignores steering."""
        board = GameBoard(10, 10)
        for _ in range(10):
            board.step()
        self.assertTrue(board.game_over)
        board.steer(-1, 0)
        self.assertEqual(board.snake.dir_row, 0)


if __name__ == "__main__":
    unittest.main()
