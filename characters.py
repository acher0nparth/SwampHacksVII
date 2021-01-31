import random
import pygame as pg
from pygame.locals import *
from settings import screen
from settings import screen_width
from settings import screen_height

class Gator(pg.sprite.Sprite):
    #can change name, just set to this for now
    player_standR = pg.image.load('gator_sprite1.png').convert_alpha()
    player_standL = pg.image.load('gator_LS1.png').convert_alpha()
    haduken = pg.image.load('haduken.png').convert_alpha()
    hadukenL = pg.image.load('hadukenL.png').convert_alpha()

    #used for assigning the walking animation when moving
    walkLeft = [pg.image.load('gator_LS1.png').convert_alpha(), pg.image.load('gator_LS2.png').convert_alpha(), pg.image.load('gator_LS1.png').convert_alpha(), pg.image.load('gator_LS2.png').convert_alpha(), pg.image.load('gator_LS1.png').convert_alpha(), pg.image.load('gator_LS2.png').convert_alpha()]
    walkRight = [pg.image.load('gator_sprite1.png').convert_alpha(), pg.image.load('gator_sprite2.png').convert_alpha(), pg.image.load('gator_sprite1.png').convert_alpha(), pg.image.load('gator_sprite2.png').convert_alpha(), pg.image.load('gator_sprite1.png').convert_alpha(), pg.image.load('gator_sprite2.png').convert_alpha()]


    def __init__(self):
        super(Gator, self).__init__()
        self.left = False
        self.right = False
        self.isJump = False
        self.wasLeft = False
        self.jumpCount = 10
        self.walkCount = 0
        self.width = 64 #CHANGE BASED ON SIZE OF SPRITE
        self.height = 64
        self.vel = 5
        self.x = screen_width / 2
        self.y = 538 #hard coded and dependent upon the resolution
        self.hitbox = (self.x, self.y, 24, 36)
        self.coins = 0
        self.oranges = 0

    def update(self, pressed_keys):
        if (pressed_keys[K_LEFT] or pressed_keys[K_a]) and self.x > self.vel :
            self.x -= self.vel
            self.left = True
            self.right = False
        elif (pressed_keys[K_RIGHT] or pressed_keys[K_d]) :
            if self.x < screen_width * 4 / 5 - self.width - self.vel :
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
        
    def take_damage(self):
        print('ouch')

    def gain_coin(self):
        self.coins += 1
        print('flex bucks: ', self.coins)

    def gain_orange(self):
        self.oranges += 1
        print('oranges: ', self.oranges)

    def exchange(self):
        self.coin = self.coins - 10
        self.oranges += 1
    

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
        self.x = x
        self.y = y
        self.height = Bulldog.height
        self.width = Bulldog.width
        self.walk_count = 0
        self.vel = 2
        self.hitbox = (self.x, self.y-20, 70, 60)
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
        self.hitbox = (self.x, self.y-20, 70, 60) 
        pg.draw.rect(screen, (0,255,0), self.hitbox, 2)         

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

    def hit(self):
        print('hit bulldog')

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
        self.x = x
        self.y = y
        self.height = Knight.height
        self.width = Knight.width
        self.walk_count = 0
        self.vel = 3
        self.hitbox = (self.x, self.y -10, 45, 65) 
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
        self.hitbox = (self.x, self.y-10, 45, 65) 
        pg.draw.rect(screen, (0,255,0), self.hitbox, 2)           

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
    
    def hit(self):
        print('hit knight')


class Haduken(pg.sprite.Sprite):
    vel = 8
    width = 55
    height = 45
    haduken = pg.image.load('haduken.png').convert_alpha()
    hadukenL = pg.image.load('hadukenL.png').convert_alpha()

    def __init__(self, x, y, facing):
        self.x = x
        self.y = y
        self.hitbox = (self.x + 8, self.y + 6, 26, 22) 
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, screen):
        if self.facing == 1:
            screen.blit(self.haduken, (self.x, self.y))
        else: 
            screen.blit(self.hadukenL, (self.x, self.y)) 
        self.hitbox = (self.x + 8, self.y + 6, 26, 22) 
        pg.draw.rect(screen, (0,255,0), self.hitbox, 2)             

class Orange(pg.sprite.Sprite):

    orange = pg.image.load('orange.png').convert_alpha()

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hitbox = (self.x + 35, self.y + 20, 70, 70) 

    def draw(self, screen):
        screen.blit(self.orange, (self.x, self.y))
        self.hitbox = (self.x + 35, self.y + 20, 70, 70) 
        pg.draw.rect(screen, (0,255,0), self.hitbox, 2)  


class Bucks(pg.sprite.Sprite):
    
    flex_bucks = pg.image.load('coin.png').convert_alpha()

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hitbox = (self.x + 10, self.y, 30, 40) 

    def draw(self, screen):
        screen.blit(self.flex_bucks, (self.x, self.y))
        self.hitbox = (self.x + 10, self.y, 30, 40) 
        pg.draw.rect(screen, (0,255,0), self.hitbox, 2) 