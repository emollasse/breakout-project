import pygame
from pygame.locals import *

class Barre:
    def __init__(self, image):
        self.image = pygame.image.load(image).convert()
        self.x = 325
        self.y = 550
        self.vitesse = 1
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
        self.vitessex = 1
        self.vitessey = -1
        self.start_position = True
        self.last_iteration = False

    def movement(self, paddle):
        if self.start_position == True:
            self.x = paddle.x + 150/2 - self.rayon
            self.y = paddle.y- 2*self.rayon
        else :
            self.x += self.vitessex
            self.y += self.vitessey
            self.collision(paddle)
            if self.x < 0 or self.x > 800-2*self.rayon:
                if self.x < 0 : self.x = 0
                elif self.x > 800-2*self.rayon : self.x = 800-2*self.rayon
                self.vitessex *=-1
            if self.y < 0 or self.y > 650-2*self.rayon:
                if self.y < 0 : self.y = 0
                elif self.y > 650-2*self.rayon: self.y = 650-2*self.rayon
                self.vitessey *=-1

    def go(self):
        if self.start_position == True:
            self.start_position = False
        else :
            self.start_position = True

    def collision(self, paddle):
        if (self.y + 2*self.rayon > paddle.y and self.y < paddle.y + paddle.sizeh) and (self.x + 2*self.rayon > paddle.x and self.x < paddle.x + paddle.sizew):
            if (self.x + self.rayon > paddle.x and self.x + self.rayon < paddle.x + paddle.sizew) and (self.y + self.rayon < paddle.y or self.y + self.rayon > paddle.y+paddle.sizeh):
                if self.last_iteration == False:
                    self.vitessey *=-1
                self.last_iteration = True
                if self.y + self.rayon < paddle.y :
                    self.y = paddle.y - 2*self.rayon
                else :
                    self.y = paddle.y + paddle.sizeh
                print('change y')
            elif (self.y + self.rayon > paddle.y and self.y + self.rayon < paddle.y + paddle.sizeh) and (self.x + self.rayon < paddle.x or self.x + self.rayon > paddle.x+paddle.sizew):
                if self.last_iteration == False:
                    self.vitessex *=-1
                self.last_iteration = True
                print('change x')
                if self.x + self.rayon < paddle.x :
                    self.x = paddle.x - 2*self.rayon
                else :
                    self.x = paddle.x + paddle.sizew
            else :
                print('change x and y')
                if self.last_iteration == False:
                    if (self.vitessex > 0 and self.x + self.rayon < paddle.x) or (self.vitessex < 0 and self.x + self.rayon > paddle.x+paddle.sizew):
                        self.vitessex *=-1
                    if (self.vitessey > 0 and self.y + self.rayon < paddle.y) or (self.vitessey < 0 and self.y + self.rayon > paddle.y+paddle.sizeh):
                        self.vitessey *=-1
                self.last_iteration = True

        else:
            self.last_iteration = False


