import pygame
from pygame.locals import *
from Barre import *
from Brick import *
import time

pygame.init()

fenetre = pygame.display.set_mode((800, 650))

continuer = True

barre = Barre("Img/Barre.png")
ball = Ball("Img/Ball.png")
bricks = [Brick("Img/Barre.png")]

t=time.time()

while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                continuer = False
            elif event.key == K_SPACE:
                ball.go()

    if time.time() - t > 0.001:
        tkey = pygame.key.get_pressed()
        if tkey[K_LEFT] != 0:
            barre.movement("left")
        elif tkey[K_RIGHT] != 0:
            barre.movement("right")
        ball.movement(barre, bricks)
        t = time.time()
        if len(bricks) != 0 :
            if bricks[0].life == 0:
                del(bricks[0])
        if ball.game_over == True:
            continuer = False

    fenetre.fill(0)
    fenetre.blit(barre.image,(barre.x ,barre.y))
    fenetre.blit(ball.image,(ball.x,ball.y))
    if len(bricks) != 0 : fenetre.blit(bricks[0].image,(bricks[0].x, bricks[0].y))
    pygame.display.flip()

if ball.game_over == True:
    print('game over')
pygame.quit()