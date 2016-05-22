import pygame
from pygame.locals import *
from Brick import *
from File import *
from math import sqrt

class Barre:
    def __init__(self, image):
        self.image = pygame.image.load(image).convert()
        self.x = 325
        self.y = 550
        self.vitesse = 2
        self.sizew = 150
        self.sizeh = 19

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


class Ball:
    def __init__(self, image):
        self.image = pygame.image.load(image).convert_alpha()
        self.rayon = 12.5
        self.x = 400-self.rayon
        self.y = 550-2*self.rayon
        self.norm_vitesse = 1
        self.vitessex = 0
        self.vitessey = -self.norm_vitesse
        self.start_position = True
        self.last_iteration = False
        self.game_over = False

    def movement(self, paddle, bricks):
        if self.start_position == True:
            self.x = paddle.x + 150/2 - self.rayon
            self.y = paddle.y- 2*self.rayon
        else :
            self.x += self.vitessex
            self.y += self.vitessey
            self.collision_paddle(paddle)
            bricks.manage_bricks(self)
            if self.x < 0 or self.x > 800-2*self.rayon:
                if self.x < 0 : self.x = 0
                elif self.x > 800-2*self.rayon : self.x = 800-2*self.rayon
                self.vitessex *=-1
            if self.y < 0 or self.y > 650:
                if self.y < 0 : self.y = 0
                elif self.y > 650: self.game_over = True
                self.vitessey *=-1

    def go(self):
        if self.start_position == True:
            self.start_position = False
        else :
            self.start_position = True

    def collision_paddle(self, paddle):
        if (self.y + 2*self.rayon > paddle.y and self.y < paddle.y + paddle.sizeh) and (self.x + 2*self.rayon > paddle.x and self.x < paddle.x + paddle.sizew):
            if (self.x + self.rayon > paddle.x and self.x + self.rayon < paddle.x + paddle.sizew) and (self.y + self.rayon < paddle.y or self.y + self.rayon > paddle.y+paddle.sizeh):
                if self.last_iteration == False:
                    self.vitessey *=-1
                    self.rebound_paddle(paddle)
                self.last_iteration = True
                if self.y + self.rayon < paddle.y :
                    self.y = paddle.y - 2*self.rayon
                else :
                    self.y = paddle.y + paddle.sizeh
            elif (self.y + self.rayon > paddle.y and self.y + self.rayon < paddle.y + paddle.sizeh) and (self.x + self.rayon < paddle.x or self.x + self.rayon > paddle.x+paddle.sizew):
                if self.last_iteration == False:
                    self.vitessex *=-1
                self.last_iteration = True
                if self.x + self.rayon < paddle.x :
                    self.x = paddle.x - 2*self.rayon
                else :
                    self.x = paddle.x + paddle.sizew
            else :
                if self.last_iteration == False:
                    self.rebound_paddle(paddle)
                    if (self.vitessey > 0 and self.y + self.rayon < paddle.y) or (self.vitessey < 0 and self.y + self.rayon > paddle.y+paddle.sizeh):
                        self.vitessey *=-1
                self.last_iteration = True

        else:
            self.last_iteration = False




    def rebound_paddle(self, paddle):
        self.vitessex = ((self.x + self.rayon - paddle.x-paddle.sizew/2)/(paddle.sizew/1.5))*self.norm_vitesse
        if self.vitessey < 0:
            self.vitessey = -sqrt(abs(self.norm_vitesse**2 - self.vitessex**2))
        else :
            self.vitessey = sqrt(abs(self.norm_vitesse**2 - self.vitessex**2))




