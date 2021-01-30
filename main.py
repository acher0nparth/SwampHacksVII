import characters
import random
import pygame as pg
from pygame.locals import *

pg.init()

screen_width = 1280
screen_height = 720
screen = pg.display.set_mode([screen_width, screen_height])

walkLeft = [pg.image.load('gator_sprite1.png').convert_alpha(), pg.image.load('gator_sprite2.png').convert_alpha(), pg.image.load('gator_sprite1.png').convert_alpha(), pg.image.load('gator_sprite2.png').convert_alpha(), pg.image.load('gator_sprite1.png').convert_alpha(), pg.image.load('gator_sprite2.png').convert_alpha()]
walkRight = [pg.image.load('gator_sprite1.png').convert_alpha(), pg.image.load('gator_sprite2.png').convert_alpha(), pg.image.load('gator_sprite1.png').convert_alpha(), pg.image.load('gator_sprite2.png').convert_alpha(), pg.image.load('gator_sprite1.png').convert_alpha(), pg.image.load('gator_sprite2.png').convert_alpha()]

background = pg.image.load('background.png')

clock = pg.time.Clock()
player = characters.Gator()
bulldog = characters.enemy()

def redrawGameWindow() :
    screen.blit(background, (0,0))
    if player.walkCount + 1 >= 59 :
        player.walkCount = 0
    if player.left :
        screen.blit(walkLeft[player.walkCount//6], (player.x,player.y))
        player.walkCount += 1
    
    screen.blit(player.surf, player.rect)
    screen.blit(bulldog.surf, bulldog.rect)
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
    screen.fill((255, 255, 255))
    pg.draw.rect(screen, (255, 0, 0), (player.x, player.y, player.width, player.height))
    pg.display.flip()
    # redrawGameWindow()
    clock.tick(60)

# Done! Time to quit.
pg.quit()