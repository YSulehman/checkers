import pygame
import math
import numpy as np

class Pieces:
    team_one_colour = (165,42,42)
    # team_two_colour = (255,255,255)
    team_two_colour = (34, 139, 34)
    black_colour = (0,0,0)
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

    def _remove_piece(self, display, colour, coordinate, block_width):
        # pygame.draw.Rect(coordinate[0], coordinate[1], block_width, block_width)
        pygame.draw.rect(
        display, 
        colour, 
        (
            int(coordinate[0] - block_width // 2), 
            int(coordinate[1] - block_width // 2), 
            int(block_width), 
            int(block_width)
        )
    )

    def _move_piece(self, display, colour, team_coordinates: list[tuple], current_point: tuple, new_point: tuple, block_width: int, team_one_turn: bool,
                    opposition_pieces_to_take: list[tuple]):
        """
        draws new piece (colour corresponding to correct team) based on new point. current_point e.g. : ('normal, x, y)
        """
       # Find the correct tuple and remove it
        team_coordinates[:] = [item for item in team_coordinates if not (item[1] == current_point[1] and item[2] == current_point[2])]
        # figure out how many multiples of block width we've shifted
        # print(abs(current_point[1] - new_point[0]))
        # print(block_width)
        num_blocks = round(abs(current_point[1] - new_point[0]) / block_width)
        # print(f'num_blocks: {num_blocks}')

        # Compute new coordinates
        if team_one_turn:
            new_y = current_point[2] + num_blocks * block_width
        else:
            new_y = current_point[2] - num_blocks * block_width
        if new_point[0] < current_point[1]:
            new_x = current_point[1] - num_blocks * block_width
        else:
            new_x = current_point[1] + num_blocks * block_width

        # Add the updated piece
        team_coordinates.append(('normal', new_x, new_y))
        # draw new circle last 
        self._remove_piece(display, self.black_colour, current_point[1:], block_width)
        self._draw_piece(display, colour, (new_x, new_y), self.piece_radius)

        # remove any opposition pieces  if applicable 
        if len(opposition_pieces_to_take) != 0:
            for piece in opposition_pieces_to_take:
                # removing pieces
                # print('heyyy')
                self._remove_piece(display, self.black_colour, piece[1:], block_width)
        
        

    def valid_move(self, new_position: tuple, current_position: tuple, team_one: bool, block_width: int, king: bool = False):
        # for debugging
        # x = math.acos(np.dot(current_position, new_position) / (np.linalg.norm(new_position) * np.linalg.norm(current_position)))
        # print(f'Team one move? {team_one}. Angle between old and new position is: {x}')
        # all pieces have to stay within the board
        if new_position[0] <= 0 or new_position[0] >= block_width * 8:
            return False 
        
        if new_position[1] <= 0 or new_position[1] >= block_width * 8:
            return False

        if king:
            pass
        elif team_one:
            # check y coordinate has increased
            # if new_position[1] <= current_position[1]:
            #     return False
            
            # should the above be
            if new_position[1] - current_position[1] <= block_width / 2:
                return False 

            # just testing something: basically we're moving along a diagonal, so can check if angle is close to zero.
            angles_radians = math.acos(np.dot(current_position, new_position) / (np.linalg.norm(new_position) * np.linalg.norm(current_position)))
            # print(angles_radians)
            if 0 <= angles_radians <= 0.65:
                return True
        else:
            # check y coordinate is decreasing
            # if new_position[1] >= current_position[1]:
            #     return False
            
            if current_position[1] - new_position[1] <= block_width / 2 :
                return False

            # just testing something
            angles_radians = math.acos(np.dot(current_position, new_position) / (np.linalg.norm(new_position) * np.linalg.norm(current_position)))
            # print(angles_radians)
            if 0 <= angles_radians <= 0.65:
                return True

        return False

    def valid_normal_move(self, new_position: tuple, current_position: tuple, team_one: bool, block_width: int, king: bool = False):
        """
        given current position, checks if new position is valid based on team and normal/king piece.
        """
        if king:
            pass
        else:
            # now break into team one and team two
            if team_one:
                # standard move (not taking)
                # first inequality checks valid y-coord within limits,
                # second inequality checks valid x-coord within limits.
                if block_width / 2 <= new_position[1] - current_position[1] <= 3 / 2 * block_width and block_width / 2 <= abs(new_position[0] - current_position[0]) <= 3 /2 * block_width:
                    # return True if the square is free and not occupied (by either same team piece of opposing team)
                    for point in self.team_one_initial_coordinates:
                        if point == current_position:
                            continue
                        if abs(new_position[0] - point[1]) <= block_width / 2 and abs(new_position[1] - point[2]) <= block_width / 2:
                            return False
                    for point in self.team_two_initial_coordinates:
                        # if point == current_position:
                        #     continue
                        if abs(new_position[0] - point[1]) <= block_width / 2 and abs(new_position[1] - point[2]) <= block_width / 2:
                            return False 
                    return True  
                
            if not team_one:
                # same logic as for team one, except new y-coord should be less than current
                if block_width / 2  <= current_position[1] - new_position[1] <= 3 / 2 * block_width and block_width / 2 <= abs(new_position[0] - current_position[0]) <= 3 /2 * block_width:
                    # return True if the square is free and not occupied (by either same team piece of opposing team)
                    for point in self.team_one_initial_coordinates:
                        if abs(new_position[0] - point[1]) <= block_width / 2 and abs(new_position[1] - point[2]) <= block_width / 2:
                            return False
                    for point in self.team_two_initial_coordinates:
                        if point == current_position:
                            continue
                        if abs(new_position[0] - point[1]) <= block_width / 2 and abs(new_position[1] - point[2]) <= block_width / 2:
                            return False 
                    return True 
        return False
            


    def make_king(self):
        pass