import pygame
from src.utils.board import Board
from src.utils.pieces import Pieces

class Checkers(Board, Pieces):
    def __init__(self, window_width: int, window_height: int):
        self.run_game = True
        self.window_width = window_width
        self.window_height = window_height
        self.block_width = self.window_width // 8
        # initialise team one to move first
        self.team_ones_move = True
        self.last_moved = 'one'

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
                # close the game terminal if close button clicked
                if event.type == pygame.QUIT:
                    self.run_game = False
                
                # let's print a message if mouse is clicked
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # let's check if mouse position is on a piece
                    for point in self.team_one_initial_coordinates:
                        if abs(event.pos[0] - point[1]) <= self.piece_radius and abs(event.pos[1] - point[2]) <= self.piece_radius:
                            self.selected_piece = point
                            self.team_one_turn = True
                            # print(f'the selected piece is {self.selected_piece}')
                            break
                    for point in self.team_two_initial_coordinates:
                        if abs(event.pos[0] - point[1]) <= self.piece_radius and abs(event.pos[1] - point[2]) <= self.piece_radius:
                            self.selected_piece = point
                            self.team_one_turn = False
                            # print('here we are')
                            # print(self.team_one_turn)
                            break

                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.selected_piece:
                        # Check if the move is valid
                        if self.selected_piece[0] == 'normal':
                            valid_move = self.valid_normal_move(event.pos, self.selected_piece[1:], self.team_one_turn, self.block_width)
                            # print(f'valid move for block width {self.block_width}? : {valid_move}')
                            # print(event.pos)
                        else:
                            valid_move = self.valid_normal_move(event.pos, self.selected_piece[1:], self.team_one_turn, self.block_width, king=True)

                        # Update the position if the move is valid
                        if valid_move:
                            if self.team_one_turn:
                                self._move_piece(self.display, self.team_one_colour, self.team_one_initial_coordinates, self.selected_piece, event.pos, self.block_width, self.team_one_turn)
                                # update self.team_one_turn
                                self.team_one_turn = False
                                # self.last_moved = None
                                # print('yo')
                            else:
                                self._move_piece(self.display, self.team_two_colour, self.team_two_initial_coordinates, self.selected_piece, event.pos, self.block_width, self.team_one_turn)
                                # update self.team_one_turn
                                self.team_one_turn = True
                                # self.last_moved = 'one'

                        # Reset selection after move
                        self.selected_piece = None
                        pygame.display.update()

                    # basically check if point is in team 1 or 2, check who's move it is,
                    # track mouse move movement, mousebuttonup and if move is valid
                elif event.type == pygame.MOUSEMOTION:
                    pass
                    # ADD IN PIECE MOVEMENT WITH MOUSE? 
                    # below code was right idea but incorrect handling of events
                    # if event.type == pygame.MOUSEBUTTONUP:
                    #     # check if the attempted move is valid and update accordingly.
                    #     if point[0] == 'normal':
                    #         valid_move = self.valid_normal_move(event.pos, point[1:], team_one, self.block_width)
                    #     else:
                    #         valid_move = self.valid_normal_move(event.pos, point[1:], team_one, self.block_width, king=True)
                    #     # need to update position, draw and update display. 
                    #     if valid_move and team_one:
                    #         # update piece location
                    #         self._move_piece(self.display, self.team_one_colour, self.team_one_initial_coordinates, point, event.pos, 
                    #                             self.block_width)
                    #     elif valid_move and not team_one:
                    #         self._move_piece(self.display, self.team_two_colour, self.team_two_initial_coordinates, point, event.pos, 
                    #                             self.block_width)

                    #     # update display last
                    #     pygame.display.update()
