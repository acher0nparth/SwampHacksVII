# Simple pygame program
import random
# Import and initialize the pygame library
import pygame as pg
from pygame.locals import *

pg.init()

screen_width = 800
screen_height = 600

screen = pg.display.set_mode([screen_width, screen_height])

player_stand = pg.image.load('gator_sprite1.png').convert_alpha()
player_walk = pg.image.load('gator_sprite2.png').convert_alpha()

clock = pg.time.Clock()

# class Enemy(pg.sprite.Sprite)

class Gator(pg.sprite.Sprite):
    def __init__(self):
        super(Gator, self).__init__()
        self.surf = player_stand
        self.rect = self.surf.get_rect(
            center=(
                random.randint(screen_height + 20, screen_width + 100),
                random.randint(0, screen_height),
            )
        )

    def update(self):
        if pressed_keys[K_w] or pressed_keys[K_UP]:
            self.surf = player_walk
            self.rect.move_ip(0, -5)
            self.surf = player_stand
        if pressed_keys[K_DOWN] or pressed_keys[K_s]:
            self.surf = player_walk
            self.rect.move_ip(0, 5)
            self.surf = player_stand
        if pressed_keys[K_LEFT] or pressed_keys[K_a]:
            self.surf = player_walk
            self.rect.move_ip(-5, 0)
            self.surf = player_stand
        if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            self.surf = player_walk
            self.rect.move_ip(5, 0)
            self.surf = player_stand

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top <= 0 :
            self.rect.top = 0
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height

player = Gator()
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
    player.update()
    
    # Fill the background with white
    screen.fill((255, 255, 255))

    screen.blit(player.surf, player.rect)

    # Flip the display
    pg.display.flip()

    clock.tick(60)

# Done! Time to quit.
pg.quit()