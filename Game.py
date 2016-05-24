import pygame
from pygame.locals import *
from Barre import *
from Brick import *
from File import *
import time

def message(window, level, str_message, x=0):
    font = pygame.font.SysFont('freesans', 36)
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


def game_level(fenetre):
    level = Level(0, "level")

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

def game_endless(fenetre):
    level = Level(0, "endless")

    while not level.end_game:
        barre = Barre("Img/Barre.png")
        ball = Ball("Img/Ball.png")

        level.bricks = []
        for i in range(3):
            level.add_row()

        t=time.time()
        level.end = False

        while not level.end and not level.end_game:
            for event in pygame.event.get():
                if event.type == QUIT:
                    level.end_game = True
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        level.end_game = True
                    elif event.key == K_SPACE:
                        ball.go()
                    elif event.key == K_RETURN:
                        level.add_row()

            if time.time() - t > 0.001:
                tkey = pygame.key.get_pressed()
                if tkey[K_LEFT] != 0:
                    barre.movement("left")
                elif tkey[K_RIGHT] != 0:
                    barre.movement("right")
                ball.movement(barre, level)
                t = time.time()
                fenetre.fill(0)
                if ball.game_over == True or level.brick_under_limit():
                    pygame.draw.rect(fenetre, (0,255,0),(0, 450, 800, 2))
                    fenetre.blit(barre.image,(barre.x ,barre.y))
                    fenetre.blit(ball.image,(ball.x,ball.y))
                    level.draw_bricks(fenetre)
                    message(fenetre, level, "Game Over")
                    level.end = True
                if ball.rebound_number[0] == ball.max_rebound():
                    ball.rebound_number = [0, ball.rebound_number[1]+1]
                    level.add_row()
                if level.victory():
                    level.add_row()

            fenetre.fill(0)
            pygame.draw.rect(fenetre, (0,255,0),(0, 450, 800, 2))
            fenetre.blit(barre.image,(barre.x ,barre.y))
            fenetre.blit(ball.image,(ball.x,ball.y))
            level.draw_bricks(fenetre)
            pygame.display.flip()
