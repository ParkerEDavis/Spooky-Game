import pygame
import lightswitch
import door


class Level:
    def __init__(self, directory):
        ## Level ##
        self.level = 0

        ## Directory Reference ##
        self.directory = directory

        ## Surface and related ##
        self.width = 0
        self.height = 0

        self.visual_surface = pygame.Surface((100, 100))
        self.object_surface = pygame.Surface((100, 100))

        # For fades to black
        self.extra_surface = pygame.Surface((640, 640)).convert_alpha()
        self.extra_surface.fill((0, 0, 0, 0))

        ## Level stuff
        # Left and right borders
        self.borders = [0, 0]

        # Stuff to draw
        self.visuals = []

        # Interactables
        self.interactables = []
    

    def loadLevel(self, zone):
        ## Fade to black
        self.extra_surface.fill((0, 0, 0, 85))
        self.directory.window.blit(self.extra_surface, (0, 0))
        pygame.display.flip()
        self.directory.clock.tick(self.directory.FPS)

        self.extra_surface.fill((0, 0, 0, 170))
        self.directory.window.blit(self.extra_surface, (0, 0))
        pygame.display.flip()
        self.directory.clock.tick(self.directory.FPS)

        self.extra_surface.fill((0, 0, 0, 255))
        self.directory.window.blit(self.extra_surface, (0, 0))
        pygame.display.flip()
        self.directory.clock.tick(self.directory.FPS)

        # zone is made of [Level ID, Direction]
        self.level = zone[0]

        # Read level data
        raw_data = open(f"data/level_data/{self.level}.txt", "r")

        # Split data into lines of text
        raw_data = raw_data.read().split('\n')

        # Split the lines of text into individual words.
        data = []
        for line in raw_data:
            data.append(line.split())
        
        # The first line is the player's potential positions
        for i in range(len(data[0])):
            # Search for a position that matches the loading zone's direction
            if data[0][i] == zone[1]:
                # Then, when found, move player to it
                self.directory.player.moveTo(int(data[0][i+1]), int(data[0][i+2]))
                break

        data.pop(0)

        # The second line is Size information
        self.width = int(data[0][0])
        self.height = int(data[0][1])

        data.pop(0)

        # Recreate the surface
        self.visual_surface = pygame.Surface((self.width, self.height))
        self.object_surface = pygame.Surface((self.width, self.height)).convert_alpha()
        self.player_surface = pygame.Surface((self.width, self.height)).convert_alpha()

        # Make sure the object surface is transparent
        self.object_surface.fill((0, 0, 0, 0))
        self.player_surface.fill((0, 0, 0, 0))

        # And link the new one
        self.directory.surfaces['visual'] = self.visual_surface
        self.directory.surfaces['object'] = self.object_surface
        self.directory.surfaces['player'] = self.player_surface

        # Clear old level data while we're at it
        self.directory.objects.clear()
        #self.directory.load_zones.clear()

        # The third line is border information
        self.borders[0] = int(data[0][0])
        self.borders[1] = int(data[0][1])

        data.pop(0)

        # Display these for now
        self.visual_surface.fill((200, 100, 100))
        pygame.draw.rect(self.visual_surface, (100, 200, 100), (self.borders[0], 0, self.borders[1] - self.borders[0], 640))
        
        # The rest are visuals and interactables
        # VISUAL:
        # "visual" [x] [y] "name (to be used to find image)"
        for line in data:
            if line[0] == 'visual':
                # Load visual image
                img = pygame.image.load(f"data/assets/{line[3]}.png")
                
                # Scale and flip to specified sizes
                # Takes image dimensions and multiplies by given scale factor
                img = pygame.transform.scale(img, (img.get_width() * float(line[5]), img.get_height() * float(line[5])))

                # Flips
                img = pygame.transform.flip(img, int(line[4]), 0)

                # Display the image
                self.visual_surface.blit(img, (int(line[1]), int(line[2])))
            
            elif line[0] == 'object':
                # Lights
                if line[3] == 'lightswitch':
                    active = False
                    # Check if lightswitch has an existing flag in directory
                    if f"light{str(self.level)}" in self.directory.flags:
                        # If it does, set the lightswitch's flag to be the existing flag
                        active = self.directory.flags[f"light{str(self.level)}"]
                
                    self.directory.link('object', lightswitch.Lightswitch(self.directory, int(line[1]), int(line[2]), active))
                
                # Door, this one isn't so complicated
                elif line[3] == 'door':
                    self.directory.link('object', door.Door(self.directory, int(line[1]), int(line[2]), int(line[4],), int(line[5]), line[6]))
            
        ## Fade to In
        self.extra_surface.fill((0, 0, 0, 170))
        self.directory.window.blit(self.extra_surface, (0, 0))
        pygame.display.flip()
        self.directory.clock.tick(self.directory.FPS)

        self.extra_surface.fill((0, 0, 0, 85))
        self.directory.window.blit(self.extra_surface, (0, 0))
        pygame.display.flip()
        self.directory.clock.tick(self.directory.FPS)

        self.extra_surface.fill((0, 0, 0, 0))
        self.directory.window.blit(self.extra_surface, (0, 0))
        pygame.display.flip()
        self.directory.clock.tick(self.directory.FPS)