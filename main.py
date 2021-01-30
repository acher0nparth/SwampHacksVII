import characters
import random
import pygame as pg
from pygame.locals import *
import tkinter as tk

pg.init()

screen_width = 1280
screen_height = 720
screen = pg.display.set_mode([screen_width, screen_height])



background = pg.image.load('background.png')

clock = pg.time.Clock()
player = characters.Gator()
bulldog = characters.Bulldog()
knight = characters.Knight()

def redrawGameWindow() :
    screen.blit(background, (0,0))
    screen.blit(bulldog.surf, bulldog.rect)
    screen.blit(knight.surf, knight.rect)

    if player.walkCount + 1 >= 59 :
        player.walkCount = 0
    if player.left :
        screen.blit(player.walkLeft[player.walkCount//10], (player.x, player.y))
        player.walkCount += 1
    elif player.right :
        screen.blit(player.walkRight[player.walkCount//10], (player.x, player.y))
        player.walkCount += 1
    else :
        if player.wasLeft :
            screen.blit(player.player_standL, (player.x, player.y))
        else :
            screen.blit(player.player_standR, (player.x, player.y))

    pg.display.update()



#main
running = True
while running:
    #get every event in the queue
    for event in pg.event.get():
        if event.type == KEYDOWN :
            if event.key == K_ESCAPE :
                running = False

        # Did the user click the window close button? If so, stop the loop.
        if event.type == QUIT:
            running = False

    pressed_keys = pg.key.get_pressed()
    player.update(pressed_keys)
    # screen.fill((255, 255, 255))
    # pg.draw.rect(screen, (255, 0, 0), (player.x, player.y, player.width, player.height))
    # pg.display.flip()
    redrawGameWindow()
    clock.tick(60)

pg.quit()
