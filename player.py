import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, directory):
        # Access to other objects
        self.directory = directory

        # Dimensions
        self.x = 0
        self.y = 0

        self.width = 64
        self.height = 64

        # Rect
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        # Movement
        self.speed = 3
        self.moving_left = False
        self.moving_right = False
    

    # Draw
    def draw(self):
        pygame.draw.rect(self.directory.window, (200, 200, 200), self.rect)
    

    def update(self):
        ## Player Movement ##
        dx = 0
        
        # Check movement flags
        if self.moving_left:
            dx -= 1
        
        if self.moving_right:
            dx += 1
        
        # Move the player
        # Player will not move vertically
        self.move(dx * self.speed, 0)
    

    # Moves the player a given number of pixels
    def move(self, dx, dy):
        ## Move player's position ##
        # Change coordinates
        self.x += dx
        self.y += dy

        # Move rect
        self.rect.move_ip(dx, dy)
    

    # Plops player down in a completely new location
    def moveTo(self, new_x, new_y):
        dx = new_x - self.x
        dy = new_y - self.y
        
        self.x += dx
        self.y += dy

        self.rect.move_ip(dx, dy)