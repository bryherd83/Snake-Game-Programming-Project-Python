## v0.1 beta - September 8 - 23, 2026

- Started porting `Snake` class from Java to Python
- Started porting `SnakeFood` class

## v0.2 beta - October 8 - 14, 2026

- Finished `Snake` and `SnakeFood` (see QA fixes)
- Added `requirements.txt` (pygame-ce)
- Added `display.py` and `main.py`: first running version showing the snake and food
- Added missing docstrings
- Added `README.md`

### Fixed 
- Fixed the food spawning on snake bug as well
- Bug fixes for `Snake`, `SnakeFood`, and `Display` as well
- pygame would not install on python 3.14, so the project uses `pygame.ce`
- `respawn()` could loop forever because the `break` was outside the `while` loop

## v0.3 beta - November 12, 2026

- Snake moves on its own every 160 ms using a pygame timer event (same speed as the Java `Timer`)
- Added WASD and arrow key controls, and Q to quit
- Snake eats the food and grows; the food moves to a new empty cell
- Snake stops when it hits the edge of the board or its own body (game-over screen comes in Sprint 4)
- New look: snake is drawn as rounded squares that fade toward the tail, with eyes facing the direction of travel; food is drawn as an apple (both from the Java version)
- Game loop now runs at 60 FPS
- New `GameBoard` class holds the board size, the snake, the food, and the game rules; `Display` now only draws and handles input (single responsibility)
- Snake body is now a `deque` plus a `set`, so it stays fast as it grows; `grow()` keeps the tail in place on the next move
- Added `test_game.py` with 10 unit tests (`python -m unittest`)

### Fixed
- `display.py` line 83: the game loop ran with no frame limit and used 100% of a CPU core. Added `clock.tick(FPS)`.
- `snake_food.py` line 32: `respawn()` kept trying random cells, which got slow as the snake grew and never ended on a full board. It now picks from a list of empty cells and returns False when none are left.
- `snake.py` line 75: the `body` property returned the real list, so other code could change the snake. It now returns a tuple copy.
- `display.py`: the food glow image was rebuilt every frame; it is now built once in `__init__`.
- `snake.py` line 57: pressing two keys quickly (up then left while moving right) could reverse the snake into itself. The reverse check now uses the last step taken.
