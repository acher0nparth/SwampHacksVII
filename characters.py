import random
import pygame as pg
from pygame.locals import *
pg.init()

screen_width = 1280
screen_height = 720

screen = pg.display.set_mode([screen_width, screen_height])


class Gator(pg.sprite.Sprite):
    left = False
    right = False
    isJump = False
    jumpCount = 10
    player_stand = pg.image.load('gator_sprite1.png').convert_alpha()
    player_walk = pg.image.load('gator_sprite2.png').convert_alpha()
    player_attack = pg.image.load('gator_attack.png').convert_alpha()

    x = screen_width / 2
    y = screen_height / 2
    walkCount = 0
    width = 64 #CHANGE BASED ON SIZE OF SPRITE
    height = 64 #CHANGE BASED ON SIZE OF SPRITE
    vel = 5
    
    def __init__(self):
        super(Gator, self).__init__()
        self.surf = Gator.player_stand
        self.rect = self.surf.get_rect(
            center=(
                Gator.x, Gator.y
            )
         )

    def update(self, pressed_keys):
        if (pressed_keys[K_LEFT] or pressed_keys[K_a]) and Gator.x > Gator.vel :
            Gator.x -= Gator.vel
        if (pressed_keys[K_RIGHT] or pressed_keys[K_d]) and Gator.x < screen_width - Gator.width - Gator.vel :
            Gator.x += Gator.vel

        if not (Gator.isJump) :
            if pressed_keys[K_w] or pressed_keys[K_UP] :
                Gator.isJump = True
        else :
            if Gator.jumpCount >= -10 :
                neg = 1
                if Gator.jumpCount < 0 :
                    neg = -1
                Gator.y -= (Gator.jumpCount ** 2) * 0.5 * neg
                Gator.jumpCount -= 1
            else :
                Gator.isJump = False
                Gator.jumpCount = 10

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