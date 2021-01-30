import random
import pygame as pg
from pygame.locals import *

pg.init()

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

# class Platform(pg.sprite.Sprite) :
#     def __init__(self, x, y) :
#         self.width = 32
#         self.height = 8
#         self.x = x
#         self.y = y
#         self.hitbox = (x, y, self.width, self.height)
#         self.texture = pg.image.load('brown_platform.png')

#         def draw(self, screen) :
#             self.hitbox = ()
#             screen.blit(self.texture, (self.x, self.y))