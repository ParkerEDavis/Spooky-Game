import pygame
import interactable


class Lightswitch(interactable.Interactable):
    def __init__(self, directory, x, y):
        # Initialize Interactable
        interactable.Interactable.__init__(self, directory, x, y, 64, 64)

        #
        self.directory = directory