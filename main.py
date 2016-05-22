import pygame
from pygame.locals import *
from Barre import *
from Brick import *
from File import *
import time

pygame.init()

fenetre = pygame.display.set_mode((800, 650))

level = Level(0)

while not level.end_game:
    barre = Barre("Img/Barre.png")
    ball = Ball("Img/Ball.png")

    level.load()

    t=time.time()

    while not level.end and not level.end_game:
        for event in pygame.event.get():
            if event.type == QUIT:
                level.end_game = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    level.end_game = True
                elif event.key == K_SPACE:
                    ball.go()

        if time.time() - t > 0.001:
            tkey = pygame.key.get_pressed()
            if tkey[K_LEFT] != 0:
                barre.movement("left")
            elif tkey[K_RIGHT] != 0:
                barre.movement("right")
            ball.movement(barre, level)
            t = time.time()
            if ball.game_over == True:
                print('game over')
                level.end = True
            if level.victory() == True:
                print('victory')
                level.end = True
                level.next_level()


        fenetre.fill(0)
        fenetre.blit(barre.image,(barre.x ,barre.y))
        fenetre.blit(ball.image,(ball.x,ball.y))
        level.draw_bricks(fenetre)
        pygame.display.flip()

pygame.quit()