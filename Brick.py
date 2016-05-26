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
    #Check the collisions between the ball and bricks.
        if (ball.y + 2*ball.radius > self.y and ball.y < self.y + self.sizeh) and (ball.x + 2*ball.radius > self.x and ball.x < self.x + self.sizew):
            #check if the ball is in the brick.
            if (ball.x + ball.radius > self.x and ball.x + ball.radius < self.x + self.sizew) and (ball.y + ball.radius < self.y or ball.y + ball.radius > self.y+self.sizeh):
                #check if the ball is under or on the brick.
                if ball.last_iteration == False:
                    #check if the ball was already in the brick at the last iteration.
                    ball.speedy *=-1
                    level.change_score(self.life, ball)
                    self.life -=1
                ball.last_iteration = True
                #replace the ball outside of the brick.
                if ball.y + ball.radius < self.y :
                    ball.y = self.y - 2*ball.radius
                else :
                    ball.y = self.y + self.sizeh
            elif (ball.y + ball.radius > self.y and ball.y + ball.radius < self.y + self.sizeh) and (ball.x + ball.radius < self.x or ball.x + ball.radius > self.x+self.sizew):
                #check if the ball is at the left or at the right of the brick.
                if ball.last_iteration == False:
                    #check if the ball was already in the brick at the last iteration.
                    ball.speedx *=-1
                    level.change_score(self.life, ball)
                    self.life -=1
                ball.last_iteration = True
                #replace the ball outside of the brick.
                if ball.x + ball.radius < self.x :
                    ball.x = self.x - 2*ball.radius
                else :
                    ball.x = self.x + self.sizew
            else :
                #check if the brick is in a corner.
                if ball.last_iteration == False:
                    #check if the ball was already in the brick at the last iteration.
                    level.change_score(self.life, ball)
                    self.life -=1
                    if (ball.speedx > 0 and ball.x + ball.radius < self.x) or (ball.speedx < 0 and ball.x + ball.radius > self.x+self.sizeh):
                        ball.speedx *=-1
                    if (ball.speedy > 0 and ball.y + ball.radius < self.y) or (ball.speedy < 0 and ball.y + ball.radius > self.y+self.sizeh):
                        ball.speedy *=-1
                ball.last_iteration = True
                #replace the ball outside of the brick.
        else:
            self.last_iteration = False