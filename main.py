import pygame
from pygame.locals import *
from Barre import *
from Brick import *
from File import *
import time

pygame.init()

fenetre = pygame.display.set_mode((800, 650))
font = pygame.font.SysFont('freesans', 36)
font_title = pygame.font.SysFont('freesans', 50)

def message(window, level, str_message, x=0):
    message_ok = False
    text = font.render(str_message,True, (255,0,0))
    window.blit(text, (300 + x, 300))
    pygame.display.flip()
    while not message_ok and not level.end_game:
        for event in pygame.event.get():
                if event.type == QUIT:
                    level.end_game = True
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        level.end_game = True
                    elif event.key == K_SPACE:
                        message_ok = True


def game(fenetre):
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
                    message(fenetre, level, "Game Over")
                    level.end = True
                if level.victory() == True:
                    message(fenetre, level, "Victory", 50)
                    level.end = True
                    level.next_level()


            fenetre.fill(0)
            fenetre.blit(barre.image,(barre.x ,barre.y))
            fenetre.blit(ball.image,(ball.x,ball.y))
            level.draw_bricks(fenetre)
            pygame.display.flip()


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
                        game(fenetre)
                    elif index_option == 1:
                        pass
                    elif index_option == 2:
                        pass
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

