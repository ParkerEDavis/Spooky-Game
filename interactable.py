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
        self.highlight_rect = pygame.Rect(self.x - 5, self.y - 5, self.width + 10, self.height + 10)

        self.highlighted = False

    # Temporary
    def draw(self):
        pygame.draw.rect(self.directory.surfaces['object'], (150, 100, 100), self.rect)
        
        if self.highlighted:
            pygame.draw.rect(self.directory.surfaces['object'], (0, 0, 0), self.highlight_rect, 5)