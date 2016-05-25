import pygame
from pygame.locals import *
from Game import *
from Scores import *

pygame.init()

fenetre = pygame.display.set_mode((800, 650))
font = pygame.font.SysFont('freesans', 36)
font_title = pygame.font.SysFont('freesans', 50)

option = [["Play",(100,175)],["Play Endless Mode",(100,275)],["Score",(100,375)],["Quit",(100,475)]]
index_option = 0
stop = False

while not stop:
    for event in pygame.event.get():
            if event.type == QUIT:
                stop = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    stop = True
                elif event.key == K_DOWN :
                    index_option += 1
                    if index_option == 4: index_option = 0
                elif event.key == K_UP :
                    index_option -= 1
                    if index_option == -1 : index_option = 3
                elif event.key == K_RETURN:
                    if index_option == 0:
                        game_level(fenetre)
                    elif index_option == 1:
                        game_endless(fenetre)
                    elif index_option == 2:
                        display_scores(fenetre)
                    elif index_option == 3:
                        stop = True

    fenetre.fill(0)

    text = font_title.render("Break Out", True, (255,255,255))
    fenetre.blit(text, (300, 50))
    for i in range(len(option)):
        if i == index_option :
            text = font.render(option[i][0],True, (255,0,0))
        else :
            text = font.render(option[i][0],True, (255,255,255))
        fenetre.blit(text, option[i][1])
    pygame.display.flip()

pygame.quit()