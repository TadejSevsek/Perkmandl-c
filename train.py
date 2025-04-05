import pygame
from constants import *
from pygame.math import Vector2

class Train:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
        self.new_block = False

    def draw_train(self, screen):  
        visual_offset_y = screen_height - (cell_number * cell_size // 2)
        if self.direction == Vector2(0, 1):  # Moving downward
            body_blocks = reversed(self.body)  # Render tail first, then body, then head
        else:
            body_blocks = self.body  # Render head first, then body, then tail
        for index, block in enumerate(body_blocks):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size // 2 + visual_offset_y)
            # Define the four corners of the diamond-shaped tile
            top_left = (x_pos, y_pos - cell_size // 2)
            top_right = (x_pos + cell_size, y_pos - cell_size // 2)
            bottom_left = (x_pos, y_pos + cell_size // 2)
            bottom_right = (x_pos + cell_size, y_pos + cell_size // 2)
            # Draw the train parts
            if index == 0 and self.direction != Vector2(0, 1):  # Head (normal order)
                pygame.draw.polygon(screen, train_head_color, [top_left, top_right, bottom_right, bottom_left])
            elif index == len(self.body) - 1 and self.direction == Vector2(0, 1):  # Head (reversed order)
                pygame.draw.polygon(screen, train_head_color, [top_left, top_right, bottom_right, bottom_left])
            elif index == 0 and self.direction == Vector2(0, 1):  # Tail (reversed order)
                pygame.draw.polygon(screen, train_tail_color, [top_left, top_right, bottom_right, bottom_left])
            elif index == len(self.body) - 1 and self.direction != Vector2(0, 1):  # Tail (normal order)
                pygame.draw.polygon(screen, train_tail_color, [top_left, top_right, bottom_right, bottom_left])
            else:  # Body
                pygame.draw.polygon(screen, train_body_color, [top_left, top_right, bottom_right, bottom_left])

    def move_train(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        elif self.direction != Vector2(0, 0):
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)