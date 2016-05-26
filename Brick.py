import pygame
from pygame.locals import *
from Paddle import *

class Brick:
    def __init__(self, x, y, life, sizew, sizeh):
        self.x = x
        self.y = y
        self.sizew = sizew
        self.sizeh = sizeh
        self.life = life

    def __del__(self):
        pass

    def collision(self, ball, level):
        if (ball.y + 2*ball.radius > self.y and ball.y < self.y + self.sizeh) and (ball.x + 2*ball.radius > self.x and ball.x < self.x + self.sizew):
            if (ball.x + ball.radius > self.x and ball.x + ball.radius < self.x + self.sizew) and (ball.y + ball.radius < self.y or ball.y + ball.radius > self.y+self.sizeh):
                if ball.last_iteration == False:
                    ball.speedy *=-1
                    level.change_score(self.life, ball)
                    self.life -=1
                ball.last_iteration = True
                if ball.y + ball.radius < self.y :
                    ball.y = self.y - 2*ball.radius
                else :
                    ball.y = self.y + self.sizeh
            elif (ball.y + ball.radius > self.y and ball.y + ball.radius < self.y + self.sizeh) and (ball.x + ball.radius < self.x or ball.x + ball.radius > self.x+self.sizew):
                if ball.last_iteration == False:
                    ball.speedx *=-1
                    level.change_score(self.life, ball)
                    self.life -=1
                ball.last_iteration = True
                if ball.x + ball.radius < self.x :
                    ball.x = self.x - 2*ball.radius
                else :
                    ball.x = self.x + self.sizew
            else :
                if ball.last_iteration == False:
                    level.change_score(self.life, ball)
                    self.life -=1
                    if (ball.speedx > 0 and ball.x + ball.radius < self.x) or (ball.speedx < 0 and ball.x + ball.radius > self.x+self.sizeh):
                        ball.speedx *=-1
                    if (ball.speedy > 0 and ball.y + ball.radius < self.y) or (ball.speedy < 0 and ball.y + ball.radius > self.y+self.sizeh):
                        ball.speedy *=-1
                ball.last_iteration = True
        else:
            self.last_iteration = False