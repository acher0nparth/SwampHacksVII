import random
import pygame as pg
from pygame.locals import *
pg.init()

screen_width = 1280
screen_height = 720
x = screen_width / 2
y = screen_height / 2

screen = pg.display.set_mode([screen_width, screen_height])


class Gator(pg.sprite.Sprite):
    left = False
    right = False
    isJump = False
    jumpCount = 10
    x = screen_width / 2
    y = screen_height / 2
    walkCount = 0
    width = 64 #CHANGE BASED ON SIZE OF SPRITE
    height = 64 #CHANGE BASED ON SIZE OF SPRITE
    vel = 5
    wasLeft = False #used to assign the correct standing position 

    #can change name, just set to this for now
    player_standR = pg.image.load('gator_sprite1.png').convert_alpha()
    player_walkR = pg.image.load('gator_sprite2.png').convert_alpha()
    player_standL = pg.image.load('gator_LS1.png').convert_alpha()
    player_walkL = pg.image.load('gator_LS2.png').convert_alpha()
    player_attack = pg.image.load('gator_attack.png').convert_alpha()

    #used for assigning the walking animation when moving
    walkLeft = [pg.image.load('gator_LS1.png').convert_alpha(), pg.image.load('gator_LS2.png').convert_alpha(), pg.image.load('gator_LS1.png').convert_alpha(), pg.image.load('gator_LS2.png').convert_alpha(), pg.image.load('gator_LS1.png').convert_alpha(), pg.image.load('gator_LS2.png').convert_alpha()]
    walkRight = [pg.image.load('gator_sprite1.png').convert_alpha(), pg.image.load('gator_sprite2.png').convert_alpha(), pg.image.load('gator_sprite1.png').convert_alpha(), pg.image.load('gator_sprite2.png').convert_alpha(), pg.image.load('gator_sprite1.png').convert_alpha(), pg.image.load('gator_sprite2.png').convert_alpha()]


    def __init__(self):
        super(Gator, self).__init__()
        self.surf = self.player_standL
        self.rect = self.surf.get_rect(
            center=(
                self.x, self.y
            )
         )

    def update(self, pressed_keys):
        if (pressed_keys[K_LEFT] or pressed_keys[K_a]) and self.x > self.vel :
            self.x -= self.vel
            self.left = True
            self.right = False
        elif (pressed_keys[K_RIGHT] or pressed_keys[K_d]) and self.x < screen_width - self.width - self.vel :
            self.x += self.vel
            self.left = False
            self.right = True
        else :
            if self.right:
                self.wasLeft = False
            elif self.left :
                self.wasLeft = True
            self.right = False
            self.left = False
            self.walkCount = 0

        if not (self.isJump) :
            if pressed_keys[K_w] or pressed_keys[K_UP] :
                self.isJump = True
                self.right = False
                self.left = False
                self.walkCount = 0
        else :
            if self.jumpCount >= -10 :
                neg = 1
                if self.jumpCount < 0 :
                    neg = -1
                self.y -= (self.jumpCount ** 2) * 0.5 * neg
                self.jumpCount -= 1
            else :
                self.isJump = False
                self.jumpCount = 10

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