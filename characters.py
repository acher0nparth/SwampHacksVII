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
    haduken = pg.image.load('haduken.png').convert_alpha()
    hadukenL = pg.image.load('hadukenL.png').convert_alpha()

    #used for assigning the walking animation when moving
    walkLeft = [pg.image.load('gator_LS1.png').convert_alpha(), pg.image.load('gator_LS2.png').convert_alpha(), pg.image.load('gator_LS1.png').convert_alpha(), pg.image.load('gator_LS2.png').convert_alpha(), pg.image.load('gator_LS1.png').convert_alpha(), pg.image.load('gator_LS2.png').convert_alpha()]
    walkRight = [pg.image.load('gator_sprite1.png').convert_alpha(), pg.image.load('gator_sprite2.png').convert_alpha(), pg.image.load('gator_sprite1.png').convert_alpha(), pg.image.load('gator_sprite2.png').convert_alpha(), pg.image.load('gator_sprite1.png').convert_alpha(), pg.image.load('gator_sprite2.png').convert_alpha()]


    def __init__(self):
        super(Gator, self).__init__()
        self.surf = self.player_standL
        self.hitbox = (self.x + 20, self.y, 24, 48)
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
        elif (pressed_keys[K_RIGHT] or pressed_keys[K_d]) :
            if self.x < screen_width * 2 / 3 - self.width - self.vel :
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
    width = 64 #CHANGE BASED ON SIZE OF SPRITE
    height = 64 #CHANGE BASED ON SIZE OF SPRITE

    bulldog1 = pg.image.load('bulldog1.png').convert_alpha()
    bulldog2 = pg.image.load('bulldog2.png').convert_alpha()
    bulldog_attack = pg.image.load('bulldog_attack.png').convert_alpha()
    bulldog1R = pg.image.load('bulldog1R.png').convert_alpha()
    bulldog2R = pg.image.load('bulldog2R.png').convert_alpha()
    bulldog_attackR = pg.image.load('bulldog_attackR.png').convert_alpha()

    walkLeft = [bulldog1, bulldog1, bulldog2, bulldog2, bulldog_attack, bulldog_attack, bulldog1, bulldog1, bulldog2, bulldog2, bulldog_attack, bulldog_attack]
    walkRight = [bulldog1R, bulldog1R, bulldog2R, bulldog2R, bulldog_attackR, bulldog_attackR, bulldog1R, bulldog1R, bulldog2R, bulldog2R, bulldog_attackR, bulldog_attackR]


    def __init__(self, x, y, end):
        super(Bulldog, self).__init__()
        self.x = x
        self.y = y
        self.height = Bulldog.height
        self.width = Bulldog.width
        self.walk_count = 0
        self.vel = 2
        self.path = [x, end]

    def draw(self, screen):
        self.move()
        if self.walk_count + 1 >= 36:
            self.walk_count = 0
    
        if self.vel > 0:
            screen.blit(self.walkRight[self.walk_count//3], (self.x, self.y))
            self.walk_count += 1
        else:
            screen.blit(self.walkLeft[self.walk_count//3], (self.x, self.y))
            self.walk_count += 1            

    def move(self): 
        if self.vel > 0:
            if self.x  + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walk_count = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walk_count = 0

    



class Knight(pg.sprite.Sprite):
    width = 64 #CHANGE BASED ON SIZE OF SPRITE
    height = 64 #CHANGE BASED ON SIZE OF SPRITE
    vel = 3

    knight1 = pg.image.load('knight1.png').convert_alpha()
    knight2 = pg.image.load('knight2.png').convert_alpha()
    knight_attack = pg.image.load('knight_attack.png').convert_alpha()
    knight1L = pg.image.load('knight1L.png').convert_alpha()
    knight2L = pg.image.load('knight2L.png').convert_alpha()
    knight_attackL = pg.image.load('knight_attackL.png').convert_alpha()

    walkLeft = [knight1L, knight1L, knight2L, knight2L, knight_attackL, knight_attackL,  knight_attackL, knight1L, knight1L, knight2L, knight2L, knight_attackL, knight_attackL, knight_attackL]
    walkRight = [knight1, knight1, knight2, knight2, knight_attack, knight_attack, knight_attack, knight1, knight1, knight2, knight2, knight_attack, knight_attack, knight_attack]


    def __init__(self, x, y, end):
        super(Knight, self).__init__()
        self.x = x
        self.y = y
        self.height = Knight.height
        self.width = Knight.width
        self.walk_count = 0
        self.vel = 3
        self.path = [x, end]

    def draw(self, screen):
        self.move()
        if self.walk_count + 1 >= 39:
            self.walk_count = 0
    
        if self.vel > 0:
            screen.blit(self.walkRight[self.walk_count//3], (self.x, self.y))
            self.walk_count += 1
        else:
            screen.blit(self.walkLeft[self.walk_count//3], (self.x, self.y))
            self.walk_count += 1            

    def move(self):
        if self.vel > 0:
            if self.x  + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walk_count = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walk_count = 0



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