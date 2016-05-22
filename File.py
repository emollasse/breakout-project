import pygame
from pygame.locals import *
from Barre import *
from Brick import Brick

class Level:
    def __init__(self, nb):
        self.nb = nb
        self.bricks = []
        self.end = False
        self.end_game = False

        list_levels = open('Level\listLevels.txt','r')
        self.list_levels = list_levels.read().split('\n')
        list_levels.close()

    def load(self):
        self.end = False
        if len(self.list_levels) > self.nb:
            name_level = self.list_levels[self.nb]
            with open(str(name_level), 'r') as level:
                for line in level.read().split('\n'):
                    brick = line.split(';')
                    self.bricks.append(Brick(int(brick[0]),int(brick[1])))
        else :
            self.end_game = True

    def manage_bricks(self, ball):
        l = []
        for i in range(len(self.bricks)) :
            self.bricks[i].collision(ball)
            if self.bricks[i].life == 0:
                l += [i]
        for i in l : del(self.bricks[i])

    def next_level(self):
        self.nb += 1

    def victory(self):
        if self.bricks == []:
            return True
        return False


