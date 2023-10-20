import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, directory):
        # Access to other objects
        self.directory = directory

        # Dimensions
        self.x = 0
        self.y = 0

        self.width = 0
        self.height = 0

        # Rect
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    

    # Draw
    def draw(self):
        ...
    

    # Moves the player a given number of pixels
    def move(self, dx, dy):
        ...
    

    # Plops player down in a completely new location
    def moveTo(self, new_x, new_y):
        ...