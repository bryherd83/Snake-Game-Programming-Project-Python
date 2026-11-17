# Snake Game (Python)

A Python remake of my Snake game, originally built in Java with Swing. This version uses **pygame-ce** for graphics and keeps the same object-oriented class design as the Java original, so the structure stays the same and only the language changes.

The game is being built in increments, so features are added a few at a time.

## Project Status

| Sprint | Goal | Status |
|---|---|---|
| 1 | Port `Snake` and `SnakeFood`, open a window showing the snake and food | ✅ Done |
| 2 | Movement, keyboard controls, eating food, and growing | ✅ Done |
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
6. Optional: run the tests with `python -m unittest`.

> **Why pygame-ce?** Regular `pygame` has no prebuilt version for Python 3.14, so this project uses `pygame-ce`, a community-maintained version that works the same way. Your code still uses `import pygame`.

## How to Play

*Working now: movement keys and Q. The snake stops when it hits the edge or itself. Pause, ENTER, score, levels, and high scores come in later sprints.*

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
| `display.py` | Game window, drawing, move timer, and keyboard input (no game rules) | ✅ (partial) |
| `snake.py` | Snake body, movement, growth, and direction logic | ✅ |
| `snake_food.py` | Food position tracking and random respawning | ✅ |
| `game_board.py` | Board size, the snake and food, and the game rules (walls and settings file planned) | ✅ (partial) |
| `file_handler.py` | Saves and loads high scores | Planned |
| `test_game.py` | Unit tests for the game classes (`python -m unittest`) | New |
| `requirements.txt` | Lists the libraries needed to run the game | ✅ |

## Changes from the Java Version

- Snake body segments are `(row, col)` tuples instead of `int[]` arrays.
- Getters are read-only `@property` methods, Python's version of encapsulation.
- Food is now given the snake's body when created, fixing a bug where food could spawn on top of the snake at the start.
- pygame replaces Swing. The game loop is written directly, and `pygame.time.set_timer` sends a move event every 160 ms in place of the Swing `Timer`.
- A turn is checked against the last step the snake took, not the last key pressed, so two fast key presses can no longer turn the snake back into itself.
- Food picks from a list of empty cells, so it never loops forever looking for a free spot.
- Game rules (move, crash, eat) live in `GameBoard` instead of `Display`, so each class has one job. In Java they were inside `Display.actionPerformed`.
- The snake body is a `deque` with a matching `set`, so moving and crash checks stay fast however long the snake gets.

## Authors

**Python version:** Blayne Ryherd

**Original Java version** ([SmallGamesProject](https://github.com/jsgreenwell/SmallGamesProject)):
- Blayne Ryherd: GUI, Display, colors, FileHandler, and debugging
- Rain Brown: Snake movement and food
- Aiden Simmons: Game board and logic

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
