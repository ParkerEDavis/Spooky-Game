import pygame
import player


class DarknessGame:
    def __init__(self):
        WINDOW_WIDTH = 640
        WINDOW_HEIGHT = 640

        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        self.FPS = 60

        self.running = True


    def eventManager(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    

    def draw(self):
        self.window.fill((100, 100, 200))


    def run(self):
        while self.running:
            self.eventManager()
            self.draw()

            pygame.display.flip()
            