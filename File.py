import pygame
from pygame.locals import *
from Barre import *
from Brick import Brick
from random import randint

class Level:
    def __init__(self, nb, mode):
        self.nb = nb
        self.bricks = []
        self.color = [(232,232,0),(255,127,0),(255,0,0)]
        self.end = False
        self.end_game = False

        if mode == "level":
            list_levels = open('Level\listLevels.txt','r')
            self.list_levels = list_levels.read().split('\n')
            list_levels.close()
        if mode == "endless":
            list_rows = open('Endless\listRows.txt','r')
            self.list_rows = list_rows.read().split('\n')
            list_rows.close()

    def load(self):
        self.end = False
        self.bricks = []
        if len(self.list_levels) > self.nb:
            name_level = self.list_levels[self.nb]
            with open(str(name_level), 'r') as level:
                for line in level.read().split('\n'):
                    brick = line.split(';')
                    self.bricks.append(Brick(int(brick[0]),int(brick[1]),int(brick[2]),int(brick[3]),int(brick[4])))
        else :
            self.end_game = True

    def draw_bricks(self, window):
        for brick in self.bricks :
            pygame.draw.rect(window, self.color[brick.life-1],(brick.x, brick.y, brick.sizew, brick.sizeh))

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

    def brick_under_limit(self):
        for brick in self.bricks:
            if brick.y + brick.sizeh > 450:
                return True
        return False

    def add_row(self):
        for brick in self.bricks:
            brick.y += 50

        name_row = self.list_rows[randint(0, len(self.list_rows)-1)]
        with open(str(name_row), 'r') as row:
            for line in row.read().split('\n'):
                brick = line.split(';')
                self.bricks.append(Brick(int(brick[0]),int(brick[1]),int(brick[2]),int(brick[3]),int(brick[4])))






