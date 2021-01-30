# Simple pygame program
import random
# Import and initialize the pygame library
import pygame as pg
from pygame.locals import *


pg.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

IMAGE = pg.image.load('gator_sprite1.png').convert_alpha()

class Gator(pg.sprite.Sprite):
    def __init__(self):
        #print("YES")
        super(Gator, self).__init__()
        self.surf = IMAGE
        #self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(250, 250),
                random.randint(0, SCREEN_HEIGHT),
            )
         )
        self.speed = random.randint(5, 20)

    def update(self, pressed_keys):
        if pressed_keys[K_UP] or pressed_keys[K_w]:
            self.rect.move_ip(0, -1)
        if pressed_keys[K_DOWN] or pressed_keys[K_s]:
            self.rect.move_ip(0, 1)
        if pressed_keys[K_LEFT] or pressed_keys[K_a]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            self.rect.move_ip(1, 0)
            # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

gator = Gator()
# Run until the user asks to quit
running = True
while running:

    for event in pg.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False
    
    pressed_keys = pg.key.get_pressed()
    gator.update(pressed_keys)
    #  print(pressed_keys)

    screen.fill((0, 0, 0))

    screen.blit(gator.surf, gator.rect)
    # Flip the display
    pg.display.flip()

# Done! Time to quit.
pg.quit()