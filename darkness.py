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
        self.level = level.Level(self.directory)

        # Maybe too high, dunno
        self.FPS = 60
        self.clock = pygame.time.Clock()

        # Gotta link these too, for cutscenes
        self.directory.link('clock', self.clock, self.FPS)

        # Link objects to the directory
        self.directory.link('player', self.player)
        self.directory.link('level', self.level)

        # Load the first level
        self.level.loadLevel([0, 'none'])
        self.directory.link('surface', self.level.extra_surface, "extra")

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
                
                # Player Interact
                elif event.key == pygame.K_SPACE:
                    self.player.interact()
            
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


        # Objects
        # Clear object surface
        self.directory.surfaces['object'].fill((0, 0, 0, 0))
        self.directory.surfaces['highlight'].fill((0, 0, 0, 0))
        
        # Then draw objects onto it
        for obj in self.directory.objects:
            obj.draw()

        # Player
        self.player.draw()
        
        # Drawing the layers
        # This is how much the the layers will be shifted to the left
        # If the player is not too close to the edge
        x_offset = 288 - self.player.x
        
        # If player x is too small, then the player is by the left border, and hence the screen stops scrolling
        if x_offset > 0:
            x_offset = 0
        
        # I knew how this worked when I coded it :p
        elif self.level.width - 640 + x_offset < 0:
            x_offset = -self.level.width + 640
        
        # Display the layers
        self.window.blit(self.directory.surfaces['visual'], (x_offset, 0))
        self.window.blit(self.directory.surfaces['object'], (x_offset, 0))

        # Make sure the proper layers are drawn when lights are on vs. off
        # I KNOW this can be prettier.
        # Probably
        if f"light{self.level.level}" in self.directory.flags:
            if self.directory.flags[f"light{self.level.level}"] == True:
                #self.window.blit(self.directory.surfaces['player'], (x_offset, 0))
                self.window.blit(self.directory.surfaces['darkness'], (x_offset, 0))
                self.window.blit(self.directory.surfaces['highlight'], (x_offset, 0))
                self.window.blit(self.directory.surfaces['eyes'], (x_offset, 0))
            else:
                self.window.blit(self.directory.surfaces['highlight'], (x_offset, 0))
                self.window.blit(self.directory.surfaces['player'], (x_offset, 0))
        
        else:
            self.window.blit(self.directory.surfaces['highlight'], (x_offset, 0))
            self.window.blit(self.directory.surfaces['player'], (x_offset, 0))

        self.window.blit(self.directory.surfaces['extra'], (0, 0))
    

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