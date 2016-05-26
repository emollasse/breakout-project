﻿import pygame
from pygame.locals import *
from Brick import *
from Level import *
from math import sqrt

class Paddle:
    def __init__(self, image):
        self.image = pygame.image.load(image).convert()
        self.x = 325
        self.y = 550
        self.speed = 2
        self.sizew = 150
        self.sizeh = 19

    def movement(self, direction):
        #manage the movement of the paddle.
        if direction == "left":
            self.x -= self.speed
            if self.x < 0:
                self.x = 0
        elif direction == "right":
            self.x += self.speed
            if self.x > 650:
                self.x = 650


class Ball:
    def __init__(self, image):
        self.image = pygame.image.load(image).convert_alpha()
        self.radius = 12.5
        self.x = 400-self.radius
        self.y = 550-2*self.radius
        self.norm_speed = 1.5
        self.speedx = 0
        self.speedy = -self.norm_speed
        self.start_position = True
        self.last_iteration = False
        self.collision = False
        self.game_over = False
        self.rebound_number = 0
        self.level_number = 0

    def movement(self, paddle, bricks):
        #move the ball and check the collision between the ball and the paddle and call the function to manage the bricks.
        if self.start_position == True:
            self.x = paddle.x + 150/2 - self.radius
            self.y = paddle.y- 2*self.radius
        else :
            self.x += self.speedx
            self.y += self.speedy
            self.collision_paddle(paddle)
            bricks.manage_bricks(self)
            if self.x < 0 or self.x > 800-2*self.radius:
                if self.x < 0 : self.x = 0
                elif self.x > 800-2*self.radius : self.x = 800-2*self.radius
                self.speedx *=-1
            if self.y < 0 or self.y > 650:
                if self.y < 0 : self.y = 0
                elif self.y > 650: self.game_over = True
                self.speedy *=-1


    def go(self):
        #Start the game.
        self.start_position = False

    def collision_paddle(self, paddle):
        #Check the collisions between the ball and the paddle.
        if (self.y + 2*self.radius > paddle.y and self.y < paddle.y + paddle.sizeh) and (self.x + 2*self.radius > paddle.x and self.x < paddle.x + paddle.sizew):
            #check if the ball is in the paddle.
            if (self.x + self.radius > paddle.x and self.x + self.radius < paddle.x + paddle.sizew) and (self.y + self.radius < paddle.y or self.y + self.radius > paddle.y+paddle.sizeh):
                #check if the ball is under or on the paddle.
                if self.last_iteration == False:
                    #check if the ball was already in the paddle at the last iteration.
                    self.speedy *=-1
                    #call the function to compute the rebound of the ball.
                    self.rebound_paddle(paddle)
                    self.rebound_number +=1
                self.last_iteration = True
                #replace the ball outside of the paddle.
                if self.y + self.radius < paddle.y :
                    self.y = paddle.y - 2*self.radius
                else :
                    self.y = paddle.y + paddle.sizeh
            elif (self.y + self.radius > paddle.y and self.y + self.radius < paddle.y + paddle.sizeh) and (self.x + self.radius < paddle.x or self.x + self.radius > paddle.x+paddle.sizew):
                #check if the ball is at the left or at the right of the paddle.
                if self.last_iteration == False:
                    #check if the ball was already in the paddle at the last iteration.
                    self.speedx *=-1
                    self.rebound_number +=1
                self.last_iteration = True
                #replace the ball outside of the paddle.
                if self.x + self.radius < paddle.x :
                    self.x = paddle.x - 2*self.radius
                else :
                    self.x = paddle.x + paddle.sizew
            else :
                #check if the paddle is in a corner.
                if self.last_iteration == False:
                    #check if the ball was already in the paddle at the last iteration.
                    self.rebound_paddle(paddle)
                    if (self.speedy > 0 and self.y + self.radius < paddle.y) or (self.speedy < 0 and self.y + self.radius > paddle.y+paddle.sizeh):
                        self.speedy *=-1
                    self.rebound_number +=1
                self.last_iteration = True
                #replace the ball outside of the paddle.

        else:
            self.last_iteration = False

    def rebound_paddle(self, paddle):
        #compute the speed x and speed y thanks the position of the ball on the paddle at the time of rebound.
        self.speedx = ((self.x + self.radius - paddle.x-paddle.sizew/2)/(paddle.sizew/1.5))*self.norm_speed
        if self.speedy < 0:
            self.speedy = -sqrt(abs(self.norm_speed**2 - self.speedx**2))
        else :
            self.speedy = sqrt(abs(self.norm_speed**2 - self.speedx**2))


    def max_rebound(self):
    #return the required number of rebounds in order to add a row.
        if self.level_number//2 > 7:
            return 3
        else :
            return 10-self.level_number//2

    def under_limit(self):
    #check when the ball is under the line limit.
        if self.y + self.radius*2 > 450:
            return True
        return False




