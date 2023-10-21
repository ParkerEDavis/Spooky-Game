import pygame
import lightswitch


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

        ## Level stuff
        # Left and right borders
        self.borders = [0, 0]

        # Stuff to draw
        self.visuals = []

        # Interactables
        self.interactables = []
    

    def loadLevel(self):
        # Read level data
        raw_data = open(f"data/level_data/{self.level}.txt", "r")

        # Split data into lines of text
        raw_data = raw_data.read().split('\n')

        # Split the lines of text into individual words.
        data = []
        for line in raw_data:
            data.append(line.split())
        
        
        # The first line is the player's position
        self.directory.player.moveTo(int(data[0][0]), int(data[0][1]))

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
        self.directory.load_zones.clear()

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
                self.directory.link('object', lightswitch.Lightswitch(self.directory, int(line[1]), int(line[2])))
            
            elif line[0] == 'load_zone':
                # "load_zone" [x] [y] [level ID], data sent to directory as list of [Rect, ID]
                self.directory.link('load zone', [pygame.Rect(int(line[1]), int(line[2]), 5, 5), int(line[3])])