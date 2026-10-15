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


