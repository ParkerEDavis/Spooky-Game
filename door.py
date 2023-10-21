import pygame


class Door(pygame.sprite.Sprite):
    def __init__(self, directory, x, y, orientation, level_id, direction):
        # Directory
        self.directory = directory
        
        # Dimensions
        self.x = x
        self.y = y
        self.width = 140
        self.height = 225

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        # Decides displayed image
        self.orientation = orientation
        self.highlighted = False

        self.level_id = level_id
        self.direction = direction

        # Image
        self.image = pygame.image.load(f"data/assets/door{self.orientation}.png")
        self.image_highlighted = pygame.image.load(f"data/assets/door{self.orientation}_high.png")

        # Transform images
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.image_highlighted = pygame.transform.scale(self.image_highlighted, (self.width, self.height))
    

    def activate(self):
        self.directory.level.loadLevel([self.level_id, self.direction])


    def draw(self):
        # Display the image
        if self.highlighted:
            self.directory.surfaces['visual'].blit(self.image_highlighted, (self.x, self.y))
        else:
            self.directory.surfaces['visual'].blit(self.image, (self.x, self.y))