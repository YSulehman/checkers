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

    def play_game(self):
        # initialise a game 
        pygame.init()

        # initialise font style and font
        self.font = pygame.font.Font('freesansbold.ttf', 30)

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
            # track game_time 
            # game_time = pygame.time.get_ticks()

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
                        
                            break
                    for point in self.team_two_initial_coordinates:
                        if abs(event.pos[0] - point[1]) <= self.piece_radius and abs(event.pos[1] - point[2]) <= self.piece_radius:
                            self.selected_piece = point
                           
                            break

                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.selected_piece:
                        # Check if the move is valid and if it's a normal or king piece moving
                        if self.selected_piece[0] == 'normal':
                            valid_move = self.valid_normal_move(event.pos, self.selected_piece[1:], self.team_ones_move, self.block_width)
                        else:
                            valid_move = self.valid_normal_move(event.pos, self.selected_piece[1:], self.team_ones_move, self.block_width, king=True)

                        # Update the position if the move is valid
                        if valid_move:
                            if self.team_ones_move:
                                self._move_piece(self.display, self.team_one_colour, self.team_one_initial_coordinates, self.selected_piece, event.pos, self.block_width, self.team_ones_move)
                                # update self.team_one_turn
                                self.team_ones_move = False
                                
                            else:

                                self._move_piece(self.display, self.team_two_colour, self.team_two_initial_coordinates, self.selected_piece, event.pos, self.block_width, self.team_ones_move)
                                # update self.team_one_turn
                                self.team_ones_move = True
                                
                        else:
                            pass
                           
                    
                        # Reset selection after move
                        self.selected_piece = None
                        pygame.display.update()

                    # basically check if point is in team 1 or 2, check who's move it is,
                    # track mouse move movement, mousebuttonup and if move is valid
                elif event.type == pygame.MOUSEMOTION:
                    pass

                  
    def _display_message(self, text: str):
        # render text and box containing text
        text_obj = self.font.render(text, True, self.black, self.white)
        textRect = text_obj.get_rect()
        textRect.center = (self.window_width // 2, self.window_height // 2)

        self.display.blit(text_obj, textRect)
