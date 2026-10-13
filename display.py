"""
display.py
Opens the game window and draws the snake and food.
Sprint 1: static display only (no movement or controls yet).
"""

import pygame
from snake import Snake
from snake_food import SnakeFood

TILE = 24 # One grid cell = TILE Pixels on Screen
ROWS = 24 # for now until GameBoard is ported to py
COLS = 32

#Colors (same values as java)
C_BG = (13, 17, 13)
C_GRID = (22, 30, 22)
C_HEAD = (0, 255, 80)
C_BODY = (0, 200, 55)
C_FOOD = (255, 55, 55)

class Display:
    """The game window. Draws the board, snake, and food."""

    def __init__(self):
        """Opens the window and creates the snake and food."""
        pygame.init()
        self.width = COLS * TILE
        self.height = ROWS * TILE
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake")

        # Start the snake in the middle
        self.snake = Snake(ROWS // 2, COLS // 2)
        # So the food does not spawn on the snake
        self.food = SnakeFood(ROWS, COLS, self.snake.body)

    def run(self):
        """Runs the game loop."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(C_BG)
            self.draw_grid()
            self.draw_food()
            self.draw_snake()
            pygame.display.flip()
        pygame.quit()

    def draw_grid(self):
        """Draws the grid."""
        # Vertical lines, one per column edge
        for c in range(COLS + 1):
            x = c * TILE
            pygame.draw.line(self.screen, C_GRID, (x, 0), (x, self.height))
        # Horizontal lines, one per row edge
        for r in range(ROWS + 1):
            y = r * TILE
            pygame.draw.line(self.screen, C_GRID, (0, y), (self.width, y))
    def draw_food(self):
        """Draws the food."""
        x = self.food.col * TILE
        y = self.food.row * TILE
        center = (x + TILE // 2, y + TILE // 2)
        pygame.draw.circle(self.screen, C_FOOD, center, TILE // 2)
    def draw_snake(self):
        """Draws the snake."""
        for i, (row, col) in enumerate(self.snake.body):
            x = col * TILE
            y = row * TILE
            if i == 0:
                color = C_HEAD
            else:
                color = C_BODY
            center = (x + TILE // 2, y + TILE // 2)
            pygame.draw.circle(self.screen, color, center, TILE // 2)
