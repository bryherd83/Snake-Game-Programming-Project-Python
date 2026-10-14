# Snake Game (Python)

A Python remake of my class Snake game, originally built in Java with Swing. This version uses **pygame-ce** for graphics and keeps the same object-oriented class design as the Java original, so the structure stays the same and only the language changes.

The game is being built in increments, so features are added a few at a time.

## Project Status

| Sprint | Goal | Status |
|---|---|---|
| 1 | Port `Snake` and `SnakeFood`, open a window showing the snake and food | ✅ Done |
| 2 | Movement, keyboard controls, eating food, and growing | Planned |
| 3 | Port `GameBoard` (walls and collision detection) | Planned |
| 4 | Port `FileHandler` (high scores), menu, pause, and game-over screens | Planned |

## How to Run

1. Install **Python 3.10 or newer** from [python.org](https://www.python.org/downloads/).
2. Clone the repository:
```
   git clone https://github.com/bryherd83/Snake-Game-Programming-Project-Python.git
```
3. Open the project folder in PyCharm (or any Python editor).
4. Install the required library:
```
   pip install -r requirements.txt
```
5. Run `main.py`.

> **Why pygame-ce?** Regular `pygame` has no prebuilt version for Python 3.14, so this project uses `pygame-ce`, a community-maintained version that works the same way. Your code still uses `import pygame`.

## How to Play

*Controls are planned for Sprint 2. In the current version, the window shows the snake and food but nothing moves yet.*

| Key | Action |
|---|---|
| W or ↑ | Move up |
| S or ↓ | Move down |
| A or ← | Move left |
| D or → | Move right |
| P | Pause / resume |
| Q | Quit |
| ENTER | Start / restart |

- Eat the red food to grow and earn points
- Every 5 foods eaten = level up and speed increase
- Avoid hitting the walls or your own body
- High scores will be saved automatically to `highscores.txt`

## Project Structure

| File | Description | Ported? |
|---|---|---|
| `main.py` | Entry point; starts the game | ✅ (menu planned) |
| `display.py` | Game window, drawing, and (later) keyboard input | ✅ (partial) |
| `snake.py` | Snake body, movement, growth, and direction logic | ✅ |
| `snake_food.py` | Food position tracking and random respawning | ✅ |
| `game_board.py` | Game grid, walls, and collision detection | Planned |
| `file_handler.py` | Saves and loads high scores | Planned |
| `requirements.txt` | Lists the libraries needed to run the game | ✅ |

## Changes from the Java Version

- Snake body segments are `(row, col)` tuples instead of `int[]` arrays.
- Getters are read-only `@property` methods, Python's version of encapsulation.
- Food is now given the snake's body when created, fixing a bug where food could spawn on top of the snake at the start.
- pygame replaces Swing, so the game loop is written directly instead of using a `Timer` and `repaint()`.

## Authors

**Python version:** Blayne Ryherd

**Original Java version** ([SmallGamesProject](https://github.com/jsgreenwell/SmallGamesProject)):
- Blayne Ryherd: GUI, Display, colors, FileHandler, and debugging
- Rain Brown: Snake movement and food
- Aiden Simmons: Game board and logic

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
