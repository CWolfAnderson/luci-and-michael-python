"""wall module

"""

import pygame

class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, color):

        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y