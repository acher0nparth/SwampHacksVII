# Simple pygame program
import random
# Import and initialize the pygame library
import pygame as pg
from pygame.locals import *
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pg.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

IMAGE = pg.image.load('gator_sprite1.png').convert_alpha()

class Gator(pg.sprite.Sprite):
    def __init__(self):
        print("YES")
        super(Gator, self).__init__()
        # self.image = IMAGE
        self.surf = IMAGE
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    def update(self):
        #print("accessed")
        #self.rect.move_ip(-5, 0)
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

gator = Gator()
# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    pressed_keys = pg.key.get_pressed()
    gator.update()
    #  print(pressed_keys)
    # Fill the background with white
    screen.fill((0, 0, 0))

    screen.blit(gator.surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    # Flip the display
    pg.display.flip()

# Done! Time to quit.
pg.quit()