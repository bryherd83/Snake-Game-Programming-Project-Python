"""
display.py
Opens the game window, draws the board, and turns keys and timer ticks
into GameBoard calls. Game rules live in game_board.py, not here.
"""

import pygame
from game_board import GameBoard

TILE = 24 # One grid cell = TILE Pixels on Screen
ROWS = 24 # Board size; will come from board_settings.txt in Sprint 3
COLS = 32
FPS = 60  # Max frames per second; stops the loop from using 100% CPU
MOVE_DELAY = 160  # ms between snake steps (same as baseSpeed in Display.java)
# Custom event the timer sends each time the snake should take a step
MOVE_EVENT = pygame.USEREVENT + 1

# Key -> (row step, col step). WASD and arrow keys, same as Display.java
DIRECTION_KEYS = {
    pygame.K_w: (-1, 0), pygame.K_UP: (-1, 0),
    pygame.K_s: (1, 0), pygame.K_DOWN: (1, 0),
    pygame.K_a: (0, -1), pygame.K_LEFT: (0, -1),
    pygame.K_d: (0, 1), pygame.K_RIGHT: (0, 1),
}

#Colors (same values as java)
C_BG = (13, 17, 13)
C_GRID = (22, 30, 22)
C_HEAD = (0, 255, 80)
C_FOOD = (255, 55, 55)
C_FOOD_SHINE = (255, 180, 180)
C_FOOD_GLOW = (255, 55, 55, 40)  # last number is alpha (see-through)
C_STEM = (90, 55, 15)
C_OUTLINE = (0, 70, 15)
C_EYE = (5, 5, 5)

class Display:
    """The game window. Draws the board and passes input to the GameBoard."""

    def __init__(self):
        """Opens the window and creates the game board."""
        pygame.init()
        # Display has a GameBoard; the board has the snake and food
        self.board = GameBoard(ROWS, COLS)
        self.width = self.board.cols * TILE
        self.height = self.board.rows * TILE
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake")
        # Clock limits how fast the game loop repeats
        self.clock = pygame.time.Clock()
        # Food glow: a see-through square, built once and reused every frame
        self.food_glow = pygame.Surface((TILE + 6, TILE + 6), pygame.SRCALPHA)
        pygame.draw.rect(self.food_glow, C_FOOD_GLOW, self.food_glow.get_rect(),
                         border_radius=6)

        # Like the Swing Timer in Java: pygame posts MOVE_EVENT every MOVE_DELAY ms
        pygame.time.set_timer(MOVE_EVENT, MOVE_DELAY)

    def run(self):
        """Runs the game loop."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == MOVE_EVENT:
                    self.board.step()
                    if self.board.game_over:
                        # Interval 0 turns the timer off
                        pygame.time.set_timer(MOVE_EVENT, 0)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False
                    elif event.key in DIRECTION_KEYS:
                        self.board.steer(*DIRECTION_KEYS[event.key])

            self.screen.fill(C_BG)
            self.draw_grid()
            self.draw_food()
            self.draw_snake()
            pygame.display.flip()
            # Wait so the loop runs at most FPS times per second
            self.clock.tick(FPS)
        pygame.quit()

    def draw_grid(self):
        """Draws the grid."""
        # Vertical lines, one per column edge
        for c in range(self.board.cols + 1):
            x = c * TILE
            pygame.draw.line(self.screen, C_GRID, (x, 0), (x, self.height))
        # Horizontal lines, one per row edge
        for r in range(self.board.rows + 1):
            y = r * TILE
            pygame.draw.line(self.screen, C_GRID, (0, y), (self.width, y))

    def draw_food(self):
        """Draws the food as a small apple with a glow, shine, and stem."""
        x = self.board.food.col * TILE
        y = self.board.food.row * TILE
        self.screen.blit(self.food_glow, (x - 3, y - 3))
        # Apple body, shine dot, and stem
        pygame.draw.rect(self.screen, C_FOOD, (x + 3, y + 3, TILE - 6, TILE - 6),
                         border_radius=4)
        pygame.draw.circle(self.screen, C_FOOD_SHINE, (x + 8, y + 8), 2)
        pygame.draw.line(self.screen, C_STEM, (x + TILE // 2, y + 3),
                         (x + TILE // 2 + 2, y), 2)

    def draw_snake(self):
        """Draws the snake as rounded squares that fade toward the tail."""
        body = self.board.snake.body
        # Draw tail first so the head ends up on top
        for i in range(len(body) - 1, -1, -1):
            row, col = body[i]
            x = col * TILE
            y = row * TILE
            if i == 0:
                pygame.draw.rect(self.screen, C_HEAD, (x + 1, y + 1, TILE - 2, TILE - 2),
                                 border_radius=4)
                self.draw_eyes(x, y)
            else:
                # t goes from near 0 (neck) to near 1 (tail); same fade as Java
                t = i / len(body)
                color = (0, max(int(200 * (1 - t * 0.65)), 50),
                         max(int(25 * (1 - t)), 10))
                rect = (x + 2, y + 2, TILE - 4, TILE - 4)
                pygame.draw.rect(self.screen, color, rect, border_radius=3)
                # width=1 draws only the outline
                pygame.draw.rect(self.screen, C_OUTLINE, rect, width=1, border_radius=3)

    def draw_eyes(self, x, y):
        """Draws two eyes on the head, facing the way the snake is moving."""
        d_row, d_col = self.board.snake.dir_row, self.board.snake.dir_col
        if d_col > 0:       # right
            eyes = [(x + TILE - 6, y + 7), (x + TILE - 6, y + 15)]
        elif d_col < 0:     # left
            eyes = [(x + 6, y + 7), (x + 6, y + 15)]
        elif d_row > 0:     # down
            eyes = [(x + 7, y + TILE - 6), (x + 15, y + TILE - 6)]
        else:               # up
            eyes = [(x + 7, y + 6), (x + 15, y + 6)]
        for center in eyes:
            pygame.draw.circle(self.screen, C_EYE, center, 2)
