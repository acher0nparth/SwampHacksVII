import characters
import random
import pygame as pg
from pygame.locals import *

pg.init()

screen_width = 1920
screen_height = 1080

screen = pg.display.set_mode([screen_width, screen_height])


clock = pg.time.Clock()

# class Enemy(pg.sprite.Sprite)

player = characters.Gator()
knight = characters.Knight()
# Run until the user asks to quit
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
    
    # Fill the background with white
    screen.fill((2, 255, 25))

    screen.blit(player.surf, player.rect)
    screen.blit(knight.surf, knight.rect)
    # Flip the display
    pg.display.flip()

    clock.tick(60)

# Done! Time to quit.
pg.quit()