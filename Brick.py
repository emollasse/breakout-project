import pygame
from pygame.locals import *
from Barre import *

class Brick:
    def __init__(self, x, y, life, sizew, sizeh):
        self.image = pygame.image.load("Img/Barre.png").convert()
        self.x = x
        self.y = y
        self.sizew = sizew
        self.sizeh = sizeh
        self.life = life

    def __del__(self):
        pass

    def collision(self, ball):
        if (ball.y + 2*ball.rayon > self.y and ball.y < self.y + self.sizeh) and (ball.x + 2*ball.rayon > self.x and ball.x < self.x + self.sizew):
            if (ball.x + ball.rayon > self.x and ball.x + ball.rayon < self.x + self.sizew) and (ball.y + ball.rayon < self.y or ball.y + ball.rayon > self.y+self.sizeh):
                if ball.last_iteration == False:
                    ball.vitessey *=-1
                    self.life -=1
                ball.last_iteration = True
                if ball.y + ball.rayon < self.y :
                    ball.y = self.y - 2*ball.rayon
                else :
                    ball.y = self.y + self.sizeh
            elif (ball.y + ball.rayon > self.y and ball.y + ball.rayon < self.y + self.sizeh) and (ball.x + ball.rayon < self.x or ball.x + ball.rayon > self.x+self.sizew):
                if ball.last_iteration == False:
                    ball.vitessex *=-1
                    self.life -=1
                ball.last_iteration = True
                if ball.x + ball.rayon < self.x :
                    ball.x = self.x - 2*ball.rayon
                else :
                    ball.x = self.x + self.sizew
            else :
                if ball.last_iteration == False:
                    self.life -=1
                    if (ball.vitessex > 0 and ball.x + ball.rayon < self.x) or (ball.vitessex < 0 and ball.x + ball.rayon > self.x+self.sizeh):
                        ball.vitessex *=-1
                    if (ball.vitessey > 0 and ball.y + ball.rayon < self.y) or (ball.vitessey < 0 and ball.y + ball.rayon > self.y+self.sizeh):
                        ball.vitessey *=-1
                ball.last_iteration = True
        else:
            self.last_iteration = False