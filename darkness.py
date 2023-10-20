import pygame
import player
import directory

class DarknessGame:
    def __init__(self):
        ### Engine Variables ###
        # Will not be able to change window size.
        # Don't really have time to mess around with that atm.
        WINDOW_WIDTH = 640
        WINDOW_HEIGHT = 640

        # The Window itself
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        # Objects
        # Directory is rather experimental, hope this works.
        self.directory = directory.Directory(self.window)
        self.player = player.Player(self.directory)

        # Link objects to the directory
        self.directory.link('player', self.player)

        # Maybe to high, dunno
        self.FPS = 60
        self.clock = pygame.time.Clock()

        # Running flag
        self.running = True


    def eventHandler(self):
        ### Event Handler ###
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    

    def draw(self):
        ### Basically, draw everything ###
        self.window.fill((100, 100, 200))


    def run(self):
        ### Main Game Loop ###
        while self.running:
            # Check for Player input
            self.eventHandler()
            # Update needed objects

            # Draw
            self.draw()

            # Update display
            pygame.display.flip()
            
            # FPS Limiter
            self.clock.tick(self.FPS)