import pygame
import player
import level
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
        self.level = level.Level()

        # Link objects to the directory
        self.directory.link('player', self.player)
        self.directory.link('level', self.level)

        self.directory.link('surface', self.level.surface, "level")

        # Maybe to high, dunno
        self.FPS = 60
        self.clock = pygame.time.Clock()

        # Running flag
        self.running = True


    def eventHandler(self):
        ### Event Handler ###
        for event in pygame.event.get():
            # Clicking the 'X' Button
            if event.type == pygame.QUIT:
                self.running = False
            
            # Keypresses
            elif event.type == pygame.KEYDOWN:
                # Try to remember to remove this.
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                
                # Moving Left
                elif (event.key == pygame.K_a) or (event.key == pygame.K_LEFT):
                    self.player.moving_left = True

                # Moving Right
                elif (event.key == pygame.K_d) or (event.key == pygame.K_RIGHT):
                    self.player.moving_right = True
            
            # Key Releases
            elif event.type == pygame.KEYUP:
                # Stopping Left
                if (event.key == pygame.K_a) or (event.key == pygame.K_LEFT):
                    self.player.moving_left = False

                # Stopping Right
                elif (event.key == pygame.K_d) or (event.key == pygame.K_RIGHT):
                    self.player.moving_right = False
    

    def update(self):
        # First, check player movement
        self.player.update()


    def draw(self):
        ### Basically, draw everything ###
        # Background
        self.window.fill((100, 100, 200))
        
        # Level
        self.level.draw()
        self.window.blit(self.directory.layers['level'], (0, 0))

        # Objects

        # Player
        self.player.draw()
    

    def run(self):
        ### Main Game Loop ###
        while self.running:
            # Check for Player input
            self.eventHandler()

            # Update needed objects
            self.update()

            # Draw
            self.draw()

            # Update display
            pygame.display.flip()
            
            # FPS Limiter
            self.clock.tick(self.FPS)