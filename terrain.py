import random
import pygame as pg
from pygame.locals import *

pg.init()

class Grass(pg.sprite.Sprite) :
    def __init__(self) :
        self.width = 44
        self.height = 44
        self.surf = pg.image.load('grass.png').convert_alpha()
        self.rect = self.surf.get_rect()

    def draw(self, screen, x , y) :
        screen.blit(self.surf, (x, y))

class Dirt(pg.sprite.Sprite) :
    def __init__(self) :
        self.width = 44
        self.height = 30
        self.surf = pg.image.load('dirt.png').convert_alpha()
        self.rect = self.surf.get_rect()

    def draw(self, screen, x, y) :
        screen.blit(self.surf, (x,y))