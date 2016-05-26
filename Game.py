import pygame
from pygame.locals import *
from Paddle import *
from Brick import *
from Level import *
import time

def message(window, level, str_message, x=0, y=0):
#write a message which contains str_message and the message is closed when the user takes the decision.
    font = pygame.font.SysFont('freesans', 36)
    message_ok = False
    text = font.render(str_message,True, (255,0,0))
    window.blit(text, (300 + x, 300 + y))
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


def game_level(window):
#Main loop to manage the game in Level mode.
    level = Level(0, "level")

    while not level.end_game:
        barre = Paddle("Img/Paddle.png")
        ball = Ball("Img/Ball.png")

        level.reset()

        level.load()

        t=time.time()
        #loop to check event about the closure of the game
        while not level.end and not level.end_game:
            for event in pygame.event.get():
                if event.type == QUIT:
                    level.end_game = True
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        level.end_game = True
                    elif event.key == K_SPACE:
                        ball.go()
            #check the event every milli second
            if time.time() - t > 0.001:
                #event to check the movement of the paddle
                tkey = pygame.key.get_pressed()
                if tkey[K_LEFT] != 0:
                    barre.movement("left")
                elif tkey[K_RIGHT] != 0:
                    barre.movement("right")
                ball.movement(barre, level)
                t = time.time()
                #Game over condition
                if ball.game_over == True:
                    message(window, level, "Game Over")
                    level.end = True
                #Victory condition
                if level.victory() == True:
                    message(window, level, "Victory", 50)
                    level.end = True
                    level.next_level()

            #Draw the game
            window.fill(0)
            window.blit(barre.image,(barre.x ,barre.y))
            window.blit(ball.image,(ball.x,ball.y))
            level.draw_bricks(window)
            pygame.display.flip()

def game_endless(window):
#Main loop to manage the game in Endless mode.
    level = Level(0, "endless")
    font = pygame.font.SysFont('freesans', 30)

    while not level.end_game:
        barre = Paddle("Img/Paddle.png")
        ball = Ball("Img/Ball.png")

        level.reset()

        for i in range(3):
            level.add_row()

        t=time.time()
        level.end = False
        #loop to check event about the closure of the game
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
            #check the event every milli second
            if time.time() - t > 0.001:
                 #event to check the movement of the paddle
                tkey = pygame.key.get_pressed()
                if tkey[K_LEFT] != 0:
                    barre.movement("left")
                elif tkey[K_RIGHT] != 0:
                    barre.movement("right")
                ball.movement(barre, level)
                t = time.time()
                window.fill(0)
                if ball.game_over == True or level.brick_under_limit():
                    #Game over condition
                    pygame.draw.rect(window, (0,255,0),(0, 450, 800, 2))
                    window.blit(font.render("Scores : "+str(level.score),True, (255,0,0)), (325, 600))
                    window.blit(barre.image,(barre.x ,barre.y))
                    window.blit(ball.image,(ball.x,ball.y))
                    level.draw_bricks(window)
                    level.add_score()
                    message(window, level, "Game Over", y=170)
                    level.end = True
                #add a row when the rebound number reach a certain value.
                if ball.rebound_number == ball.max_rebound():
                    ball.rebound_number = 0
                    ball.level_number += 1
                    level.add_row()
                #check if the ball is under the limit and if the level is empty and add a row when it's True.
                if ball.under_limit():
                    if level.victory():
                        level.change_score(6, ball)
                        ball.rebound_number = 0
                        level.add_row()
            #Draw game
            window.fill(0)
            window.blit(font.render("Scores : "+str(level.score),True, (255,0,0)), (325, 600))
            pygame.draw.rect(window, (0,255,0),(0, 450, 800, 2))
            window.blit(barre.image,(barre.x ,barre.y))
            window.blit(ball.image,(ball.x,ball.y))
            level.draw_bricks(window)
            pygame.display.flip()
