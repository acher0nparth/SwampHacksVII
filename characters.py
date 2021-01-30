import random
import pygame as pg
from pygame.locals import *
pg.init()

screen_width = 1920
screen_height = 1080
x = screen_width / 2
y = screen_height / 2

screen = pg.display.set_mode([screen_width, screen_height])


class Gator(pg.sprite.Sprite):
    player_stand = pg.image.load('gator_sprite1.png').convert_alpha()
    player_walk = pg.image.load('gator_sprite2.png').convert_alpha()
    player_attack = pg.image.load('gator_attack.png').convert_alpha()

    def __init__(self):
        super(Gator, self).__init__()
        self.surf = Gator.player_stand
        self.rect = self.surf.get_rect(
            center=(
                random.randint(screen_height + 20, screen_width + 100),
                random.randint(0, screen_height),
            )
         )

    def update(self, pressed_keys):
        if pressed_keys[K_w] or pressed_keys[K_UP]:
            self.surf = Gator.player_walk
            self.rect.move_ip(0, -5)
            self.surf = Gator.player_stand
        if pressed_keys[K_DOWN] or pressed_keys[K_s]:
            self.surf = Gator.player_walk
            self.rect.move_ip(0, 5)
            self.surf = Gator.player_stand
        if pressed_keys[K_LEFT] or pressed_keys[K_a]:
            self.surf = Gator.player_walk
            self.rect.move_ip(-5, 0)
            self.surf = Gator.player_stand
        if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            self.surf = Gator.player_walk
            self.rect.move_ip(5, 0)
            self.surf = Gator.player_stand

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top <= 0 :
            self.rect.top = 0
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height


class Bulldog(pg.sprite.Sprite):

    bulldog1 = pg.image.load('bulldog1.png').convert_alpha()
    bulldog2 = pg.image.load('bulldog2.png').convert_alpha()
    bulldog_attack = pg.image.load('bulldog_attack.png').convert_alpha()
    def __init__(self):
        super(Bulldog, self).__init__()
        self.surf = Bulldog.bulldog1
        self.rect = self.surf.get_rect(
            center=(x,y)
        )

    #def update(self):


class Knight(pg.sprite.Sprite):

    knight1 = pg.image.load('knight1.png').convert_alpha()
    knight2 = pg.image.load('knight2.png').convert_alpha()
    knight_attack = pg.image.load('knight_attack.png').convert_alpha()
    def __init__(self):
        super(Knight, self).__init__()
        self.surf = Knight.knight1
        self.rect = self.surf.get_rect(
            center=(x,y)
        )

    #def update(self):



class Items(pg.sprite.Sprite):

    orange = pg.image.load('orange.png').convert_alpha()
    flex_bucks = pg.image.load('flex_bucks.jpg').convert_alpha()
    def __init__(self):
        super(Items, self).__init__()
        self.surf = Knight.knight1
        self.rect = self.surf.get_rect(
            center=(x,y)
        )

    #def update(self):