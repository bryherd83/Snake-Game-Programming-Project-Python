"""
main.py
Entry point for the Snake game. Builds the game objects and opens the window.
All objects are created here and passed down (dependency injection), so no
class has to build its own collaborators.
(The text menu from Main.java will be added in a later sprint.)
"""

from display import Display
from game_board import GameBoard
from snake import Snake
from snake_food import SnakeFood

ROWS = 24  # Board size; will come from board_settings.txt in Sprint 3
COLS = 32

# Only start the game when this file is run, not when it is imported
if __name__ == "__main__":
    snake = Snake(ROWS // 2, COLS // 2)
    # Food gets the snake's body so it does not spawn on the snake
    food = SnakeFood(ROWS, COLS, snake.body)
    Display(GameBoard(ROWS, COLS, snake, food)).run()
