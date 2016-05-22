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
bricks = Bricks([Brick(50, 50), Brick(250, 50), Brick(450, 50), Brick(650, 50),
                Brick(50, 150), Brick(250, 150), Brick(450, 150), Brick(650, 150)])

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
        if ball.game_over == True:
            print('game over')
            continuer = False
        if bricks.victory() == True:
            print('victory')
            continuer = False

    fenetre.fill(0)
    fenetre.blit(barre.image,(barre.x ,barre.y))
    fenetre.blit(ball.image,(ball.x,ball.y))
    for brick in bricks.bricks :
        fenetre.blit(brick.image,(brick.x, brick.y))
    pygame.display.flip()

pygame.quit()