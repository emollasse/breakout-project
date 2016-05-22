import pygame
from pygame.locals import *

class Brick:
    def __init__(self, image):
        self.image = pygame.image.load(image).convert()
        self.x = 325
        self.y = 100
        self.vitesse = 1
        self.sizew = 150
        self.sizeh = 19
        self.life = 1
        self.last_iteration = False

    def collision(self, ball):
        if (ball.y + 2*ball.rayon > self.y and ball.y < self.y + self.sizeh) and (ball.x + 2*ball.rayon > self.x and ball.x < self.x + self.sizew):
            if (ball.x + ball.rayon > self.x and ball.x + ball.rayon < self.x + self.sizew) and (ball.y + ball.rayon < self.y or ball.y + ball.rayon > self.y+self.sizeh):
                if self.last_iteration == False:
                    ball.vitessey *=-1
                self.last_iteration = True
                if ball.y + ball.rayon < self.y :
                    ball.y = self.y - 2*ball.rayon
                else :
                    ball.y = self.y + self.sizeh
            elif (ball.y + ball.rayon > self.y and ball.y + ball.rayon < self.y + self.sizeh) and (ball.x + ball.rayon < self.x or ball.x + ball.rayon > self.x+self.sizew):
                if self.last_iteration == False:
                    ball.vitessex *=-1
                self.last_iteration = True
                if ball.x + ball.rayon < self.x :
                    ball.x = self.x - 2*ball.rayon
                else :
                    ball.x = self.x + self.sizew
            else :
                if self.last_iteration == False:
                    if (self.vitessex > 0 and ball.x + ball.rayon < self.x) or (ball.vitessex < 0 and ball.x + ball.rayon > self.x+self.sizeh):
                        self.vitessex *=-1
                    if (self.vitessey > 0 and ball.y + ball.rayon < self.y) or (ball.vitessey < 0 and ball.y + ball.rayon > self.y+self.sizeh):
                        self.vitessey *=-1
                self.last_iteration = True
            self.life -=1
        else:
            self.last_iteration = False