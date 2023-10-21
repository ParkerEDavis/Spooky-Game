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
        self.hitbox = pygame.Rect(self.x - 16, self.y - 16, self.width + 32, self.height + 32)

        # Movement
        self.speed = 3
        self.moving_left = False
        self.moving_right = False
    

    def interact(self):
        # If the interact button is pressed, check for interactables and activate them
        # If one is activated, stop searching, only one should activate at a time.
        # This may cause problems eventually, but multiple objects shouldn't be that close to each other.
        for obj in self.directory.objects:
            if obj.rect.colliderect(self.hitbox):
                obj.activate()
                return


    def update(self):
        ## Player Movement ##
        dx = 0
        
        # Check movement flags
        if self.moving_left:
            dx -= 1
        
        if self.moving_right:
            dx += 1
        
        # Player go zoom (at speed of self.speed)
        dx = dx * self.speed

        # Check to see if player tries to go out of bounds
        if self.rect.right + dx > self.directory.level.borders[1]:
            dx = self.directory.level.borders[1] - self.rect.right
        elif self.x + dx < self.directory.level.borders[0]:
            dx = self.directory.level.borders[0] - self.x
        
        # Then, if player moved, check for objects in hitbox, if so, highlight
        if dx != 0:
            for obj in self.directory.objects:
                if obj.rect.colliderect(self.hitbox):
                    obj.highlighted = True
                else:
                    obj.highlighted = False
        
        # Move the player
        # Player will not move vertically
        self.move(dx, 0)
    

    # Moves the player a given number of pixels
    def move(self, dx, dy):
        ## Move player's position ##
        # Change coordinates
        self.x += dx
        self.y += dy

        # Move rect
        self.rect.move_ip(dx, dy)
        self.hitbox.move_ip(dx, dy)

        # If players moves into a loading zone, they transfer between levels
        for zone in self.directory.load_zones:
            # If player collides with load zone
            if zone[0].colliderect(self.rect):
                # Change level id to level if of loading zone
                self.directory.level.level = zone[1]
                
                # Reload the level
                self.directory.level.loadLevel()
    

    # Plops player down in a completely new location
    def moveTo(self, new_x, new_y):
        # Calculate dx
        dx = new_x - self.x
        dy = new_y - self.y
        
        # Update Position
        self.x += dx
        self.y += dy

        # Update rects
        self.rect.move_ip(dx, dy)
        self.hitbox.move_ip(dx, dy)
    

    # Draw
    def draw(self):
        # Fill surface with transparent pixels
        self.directory.surfaces['player'].fill((0, 0, 0, 0))

        # Draw rects
        pygame.draw.rect(self.directory.surfaces['player'], (100, 200, 200, 125), self.hitbox)
        pygame.draw.rect(self.directory.surfaces['player'], (200, 200, 200), self.rect)