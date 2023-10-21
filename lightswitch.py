import pygame

class Lightswitch:
    def __init__(self, directory, x, y):
        # Directory
        self.directory = directory
        
        # Dimensions
        self.x = x
        self.y = y
        self.width = 64
        self.height = 64

        # Rect
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.highlight_rect = pygame.Rect(self.x - 5, self.y - 5, self.width + 10, self.height + 10)

        # Flags
        self.highlighted = False
        self.activated = False

        # Color for testing
        self.color = (150, 100, 100)


    def activate(self):
        # Calls when the player presses activate when object is in hitbox
        if not self.activated:
            self.color = (100, 150, 100)
            self.activated = True

        # If green, turn off (red)
        else:
            self.color = (150, 100, 100)
            self.activated = False


    def draw(self):
        pygame.draw.rect(self.directory.surfaces['object'], self.color, self.rect)
        
        if self.highlighted:
            pygame.draw.rect(self.directory.surfaces['object'], (0, 0, 0), self.highlight_rect, 5)