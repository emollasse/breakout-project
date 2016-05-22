﻿import pygame
from pygame.locals import *
from Barre import *

class Bricks:
    def __init__ (self, bricks):
        self.bricks = bricks

    def manage_bricks(self, ball):
        l = []
        for i in range(len(self.bricks)) :
            self.bricks[i].collision(ball)
            if self.bricks[i].life == 0:
                l += [i]
        for i in l : del(self.bricks[i])


    def victory(self):
        if self.bricks == []:
            return True
        return False

class Brick:
    def __init__(self, x, y):
        self.image = pygame.image.load("Img/Barre.png").convert()
        self.x = x
        self.y = y
        self.vitesse = 1
        self.sizew = 150
        self.sizeh = 19
        self.life = 1
        self.last_iteration = False

    def __del__(self):
        pass

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
                    if (ball.vitessex > 0 and ball.x + ball.rayon < self.x) or (ball.vitessex < 0 and ball.x + ball.rayon > self.x+self.sizeh):
                        ball.vitessex *=-1
                    if (ball.vitessey > 0 and ball.y + ball.rayon < self.y) or (ball.vitessey < 0 and ball.y + ball.rayon > self.y+self.sizeh):
                        ball.vitessey *=-1
                self.last_iteration = True
            self.life -=1
        else:
            self.last_iteration = False