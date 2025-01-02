"""
This is our main driver file. It will be responsible for handling user input and displaying current GameState object.
"""

import pygame as p
from Chess import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8  # dimensions of board are 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15  # for animations later on
IMAGES = {}


def load_images():
    """
    Initialize global dictionary of images. This will be called once in the main
    Can access an image by saing IMAGES['wp']
    :return:
    """
    pieces = ["wp", "wR", "wN", "wB", "wQ", "wK", "bp", "bR", "bN", "bB", "bQ", "bK"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


def main():
    """
    Main driver, will handle user input and updating the graphics
    :return:
    """
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    load_images()  # Do this once, before the game loop
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        draw_game_state(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


def draw_game_state(screen, gs):
    """
    Responsible for all the graphics within a current gamestate
    :param screen:
    :param gs:
    :return:
    """
    draw_board(screen)  # Draw squares on the board
    draw_pieces(screen, gs.board)  # draw pieces on top of these squares


def draw_board(screen):
    """
    Draw the squares on the board
    :param screen:
    :return:
    """
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


def draw_pieces(screen, board):
    """
    Draw the pieces on the board using the current GameState.board
    :param screen:
    :param board:
    :return:
    """
    pass


if __name__ == "__main__":
    main()

