import pygame
from pygame.locals import *

class Barre:
    def __init__(self, image):
        self.image = pygame.image.load(image).convert()
        self.x = 325
        self.y = 550
        self.vitesse = 5

    def get_image(self):
        return self.image

    def movement(self, direction):
        if direction == "left":
            self.x -= self.vitesse
            if self.x < 0:
                self.x = 0
        elif direction == "right":
            self.x += self.vitesse
            if self.x > 650:
                self.x = 650
