import sys
from pathlib import Path

import pygame as pg


class SpriteSheet:
    """Class for storing and managing sprite sheets."""
    def __init__(self, file_path):
        """Load the sprite sheet from the given path."""
        self.sheet = pg.image.load(file_path).convert_alpha()

    def get_image(self, x, y, width, height):
        """Cut and return a piece of sprite sheet."""
        return self.sheet.subsurface(x, y, width, height)


# Use this to not overcomplicate
# res = Path("res")

# Use this to be able to run the game by simply
# double-clicking the main file
res = Path(sys.argv[0]).parent/"res"