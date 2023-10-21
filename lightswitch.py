import pygame

class Lightswitch:
    def __init__(self, directory, x, y, active):
        # Directory
        self.directory = directory
        
        # Dimensions
        self.x = x
        self.y = y
        self.width = 24
        self.height = 24

        # Rect
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.highlight_rect = pygame.Rect(self.x - 3, self.y - 3, self.width + 6, self.height + 6)

        # Flags
        self.highlighted = False
        self.activated = active

        # Color for testing
        if self.activated:
            self.color = (100, 150, 100)
        else:
            self.color = (150, 100, 100)


    def activate(self):
        # Calls when the player presses activate when object is in hitbox
        if not self.activated:
            # When activated, make green and active
            self.color = (100, 150, 100)
            self.activated = True

            # Set flag to true
            self.directory.flags[f"light{str(self.directory.level.level)}"] = True

        # If green, turn off (red)
        else:
            self.color = (150, 100, 100)
            self.activated = False

            self.directory.flags[f"light{str(self.directory.level.level)}"] = False


    def draw(self):
        pygame.draw.rect(self.directory.surfaces['object'], self.color, self.rect)
        
        if self.highlighted:
            pygame.draw.rect(self.directory.surfaces['object'], (0, 0, 0), self.highlight_rect, 5)