import pygame
from pygame.locals import *
from Barre import *

pygame.init()

fenetre = pygame.display.set_mode((800, 650))

continuer = True

barre = Barre("Img/Barre.png")

pygame.key.set_repeat(10,10)

while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                barre.movement("left")
            elif event.key == K_RIGHT:
                barre.movement("right")
            elif event.key == K_ESCAPE:
                continuer = False

    fenetre.fill(0)
    fenetre.blit(barre.image ,(barre.x ,barre.y))
    pygame.display.flip()

pygame.quit()