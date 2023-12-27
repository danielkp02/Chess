"""
This is our main driver file. It will be responsible for handling user input and displaying current gamestate.
"""

import pygame as p
from Chess import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8  # dimensions of board are 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15  # for animations later on
IMAGES = []

"""
Initialize a global dictionary of images. This will be called once in the main
"""


def load_images():
    pieces = ["wp", "wR", "wN", "wB", "wQ", "wK", "bp", "bR", "bN", "bB", "bQ", "bK"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"),
                                          (SQ_SIZE, SQ_SIZE))  # We can access an image by saying "IMAGES['wp'}


"""
The main driver, will handle user input and updating the graphics
"""


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
