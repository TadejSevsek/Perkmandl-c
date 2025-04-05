import pygame
import random
from constants import * 
from pygame.math import Vector2

class Coal:
    def __init__(self):
        self.randomize()
        try:
            self.apple = pygame.image.load('Graphics/coal.png').convert_alpha()
            self.apple = pygame.transform.scale(self.apple, (cell_size, cell_size // 2))
        except pygame.error as e:
            print(f"Unable to load image: {e}")
            sys.exit()

    def draw_coal(self, screen):  # Add 'screen' as a parameter
        visual_offset_y = screen_height - (cell_number * cell_size // 2)
        x_pos = int(self.pos.x * cell_size)
        y_pos = int(self.pos.y * cell_size // 2 + visual_offset_y)
        screen.blit(self.apple, (x_pos, y_pos))

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)