
### Holds references to all other game objects, for easy checking.
# Mainly for collisions and picking up items and stuff.
class Directory:
    def __init__(self, window):
        self.window = window
        self.player = False
        self.level = False
        self.objects = []
        self.surfaces = {}

    def link(self, type, thing, extra = False):
        if type == 'object':
            self.objects.append(thing)
        
        elif type == 'surface':
            # A layer is passed as the object, and the name of the layer is passed as a key
            self.surfaces[extra] = thing
        
        elif type == 'level':
            self.level = thing
        
        elif type == 'player':
            self.player = thing

        