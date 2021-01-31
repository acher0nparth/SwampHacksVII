import random
import pygame as pg
from pygame.locals import *

class Grass(pg.sprite.Sprite) :
    def __init__(self) :
        self.width = 44
        self.height = 44
        self.texture = pg.image.load('grass.png').convert_alpha()

    def draw(self, screen, x , y) :
        screen.blit(self.texture, (x, y))

class Dirt(pg.sprite.Sprite) :
    def __init__(self) :
        self.width = 44
        self.height = 30
        self.texture = pg.image.load('dirt.png').convert_alpha()

    def draw(self, screen, x, y) :
        screen.blit(self.texture, (x,y))

class Platform(pg.sprite.Sprite) :
    def __init__(self, x, y) :
        self.width = 32
        self.height = 8
        self.x = x
        self.y = y
        self.hitbox = (x, y, self.width * 3, self.height * 2)
        self.texture = pg.image.load('brown_platform.png')

    def draw(self, screen) :
        self.hitbox = (self.x, self.y, self.width * 3, self.height * 2)
        screen.blit(pg.transform.scale(self.texture, (96, 16)), (self.x, self.y))
        #pg.draw.rect(screen, (255,0 ,0), self.hitbox, 2)

class LongPlatform(pg.sprite.Sprite) :
    def __init__(self, x, y) :
        self.width = 64
        self.height = 8
        self.x = x
        self.y = y
        self.hitbox = (x, y, self.width * 3, self.height * 2)
        self.texture = pg.image.load('longbrown_platform.png')

    def draw(self, screen) :
        self.hitbox = (self.x, self.y, self.width * 3, self.height * 2)
        screen.blit(pg.transform.scale(self.texture, (192, 16)), (self.x, self.y))
        #pg.draw.rect(screen, (255, 0, 0), self.hitbox, 2)