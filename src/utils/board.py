import pygame

class Board:
    black = (0,0,0)
    white = (255, 255, 255)
    brown = (139,69,19)
    def __init__(self):
        pass

    def make_board(self, display, dimension: int, block_width: int):
        """
        makes the board on display, dimension is window size (width = height),
        block_width (=block_height). number_rows (& number_cols) = dimension // block_width
        """
        # rows = dimension // block_width
        for i in range(0, dimension, block_width):
            for j in range(0, dimension, block_width):
                # draw block using pygame 
                block = pygame.Rect(i, j, block_width, block_width)
                # need to alternate between white and black coloured squares
                if (i // block_width + j // block_width) % 2 == 0:
                    pygame.draw.rect(display, self.brown, block)
                else:
                    pygame.draw.rect(display, self.black, block)
    
    
