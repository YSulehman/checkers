import pygame

class Pieces:
    team_one_colour = (165,42,42)
    team_two_colour = (255,255,255)
    def __init__(self):
        pass

    def set_initial_pieces(self, display: pygame.surface.Surface, dimension: int, block_width: int):
        # store coordinates of centres of initial pieces
        self.team_one_initial_coordinates = []
        self.team_two_initial_coordinates = []
        self.piece_radius = block_width // 4
        # y = (block_width + i) / 2
        # 12 pieces in total for both teams
        for row in range(3):
            y = block_width / 2 + block_width * row
            for col in range(4):
                if row == 0:
                    x = block_width / 2 + (2 * col + 1) * block_width
                    # print(x)
                    self.team_one_initial_coordinates.append(('normal', x, y))
                if row == 1:
                     x = - block_width / 2 + (2 * col + 1) * block_width
                     self.team_one_initial_coordinates.append(('normal', x, y))
                if row == 2: 
                     x = block_width / 2 + (2 * col + 1) * block_width 
                     self.team_one_initial_coordinates.append(('normal', x, y))

        # same process for team two initial coordinates
        for row in range(3):
            y = dimension - (block_width / 2 + block_width * row)
            for col in range(4):
                if row == 0:
                    x = - block_width / 2 + (2 * col + 1) * block_width
                    # print(x)
                    self.team_two_initial_coordinates.append(('normal', x, y))
                if row == 1:
                     x =  x = block_width / 2 + (2 * col + 1) * block_width
                     self.team_two_initial_coordinates.append(('normal', x, y))
                if row == 2: 
                     x = - block_width / 2 + (2 * col + 1) * block_width 
                     self.team_two_initial_coordinates.append(('normal', x, y))
        
        # loop through team one coordinates and draw circle
        for point in self.team_one_initial_coordinates:
            self._draw_piece(display, self.team_one_colour, point[1:], self.piece_radius)
        # similarly for team two
        for point in self.team_two_initial_coordinates:
            self._draw_piece(display, self.team_two_colour, point[1:], self.piece_radius)

        

    def _draw_piece(self, display, colour, coordinate, radius):
        pygame.draw.circle(display, colour, coordinate, radius)

    def remove_piece(self):
        pass

    def move_piece(self):
        pass

    def make_king(self):
        pass