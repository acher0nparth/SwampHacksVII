import random
import pygame as pg
from pygame.locals import *
pg.init()

screen_width = 1920
screen_height = 1080

screen = pg.display.set_mode([screen_width, screen_height])

player_stand = pg.image.load('gator_sprite1.png').convert_alpha()
player_walk = pg.image.load('gator_sprite2.png').convert_alpha()
bulldog1 = pg.image.load('bulldog1.png').convert_alpha()

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

    def update(self, pressed_keys):
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


class enemy(pg.sprite.Sprite):

    def __init__(self):
        super(enemy, self).__init__()
        self.surf = bulldog1
        self.rect = self.surf.get_rect(
            center=(
                random.randint(screen_height + 20, screen_width + 100),
                random.randint(0, screen_height),
            )
         )