import pygame


class Door(pygame.sprite.Sprite):
    def __init__(self, directory, x, y, orientation):
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

        # Image
        self.image = pygame.image.load(f"data/assets/door{self.orientation}.png")
        self.highlighted = pygame.image.load(f"data/assets/door{self.orientation}_high.png")

        # Transform images
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * .25, self.image.get_height() * .25))
    

    def draw(self):
        # Display the image
        self.directory.surfaces['visual'].blit(self.image, (self.x, self.y))