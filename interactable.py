import pygame


class Interactable(pygame.sprite.Sprite):
    def __init__(self, directory, x, y, width, height):
        # Directory
        self.directory = directory
        
        # Dimensions
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # Rect
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.color = (200, 100, 100)

    # Temporary
    def draw(self):
        pygame.draw.rect(self.directory.surfaces['object'], self.color, self.rect)