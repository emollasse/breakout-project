import pygame
from pygame.locals import *
from Barre import *
import time

pygame.init()

fenetre = pygame.display.set_mode((800, 650))

continuer = True

barre = Barre("Img/Barre.png")
ball = Ball("Img/Ball.png")

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
        ball.movement(barre)
        t = time.time()

    fenetre.fill(0)
    fenetre.blit(barre.image,(barre.x ,barre.y))
    fenetre.blit(ball.image,(ball.x,ball.y))
    pygame.display.flip()

pygame.quit()