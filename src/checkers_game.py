import pygame
from src.utils.board import Board
from src.utils.pieces import Pieces

class Checkers(Board, Pieces):
    def __init__(self, window_width: int, window_height: int):
        self.run_game = True
        self.window_width = window_width
        self.window_height = window_height
        self.block_width = self.window_width // 8

    def play_game(self):
        # initialise a game 
        pygame.init()

        # make a pygame display
        self.display = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Checkers")

        # make checkboard display
        self.make_board(self.display, self.window_width, self.block_width)
        # add pieces to board
        self.set_initial_pieces(self.display, self.window_width, self.block_width)

        # update display
        pygame.display.update()

        # run game 
        while self.run_game:
             for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run_game = False