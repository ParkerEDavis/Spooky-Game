import pygame


class Level:
    def __init__(self,):
        ## Level ##
        self.level = 0

        ## Surface and related ##
        self.width = 0
        self.height = 0

        self.surface = pygame.Surface((100, 100))
    

    def loadLevel(self):
        raw_data = open(f"data/level_data/{self.level}.txt", "r")
    

    def draw(self):
        self.surface.fill((100, 240, 100))