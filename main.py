import characters
import terrain
import random
import pygame as pg
import tkinter as tk
from pygame.locals import *

def Main():

    Start_Menu() 

def Game_Loop():

    knights = []
    bulldogs = []
    cash = []
    oranges = []

    chars = {
    'player' : characters.Gator(),
    'bulldog' : bulldogs, 
    'knight' : knights
    }

    terr = {
        'grass' : terrain.Grass(),
        'dirt' : terrain.Dirt(),
        'platform_br' : terrain.Platform(1000, 400)
    }

    items = {
        'cash' : cash,
        'oranges' : oranges
    }

    chars['bulldog'].append(characters.Bulldog(100, 480, 1340))
    chars['knight'].append(characters.Knight(100, 450, 1180))

    items['cash'].append(characters.Bucks(200, 300))
    items['oranges'].append(characters.Orange(300, 300))

    haduk = []
    haduk_loop = 0

    screen_width = 1440
    screen_height = 720

    screen = pg.display.set_mode([screen_width, screen_height])
    background = pg.image.load('background.png')
    background_x = [0]

    clock = pg.time.Clock()

    pg.init()
    # Run until the user asks to quit
    running = True
    while running:
        
        if haduk_loop > 0:
            haduk_loop += 1
        if haduk_loop > 10:
            haduk_loop = 0
        #get every event in the queue
        for event in pg.event.get():
            if event.type == KEYDOWN :
                if event.key == K_ESCAPE :
                    running = False
                elif event.key == K_m :
                    InGame_Menu()

            # Did the user click the window close button? If so, stop the loop.
            if event.type == QUIT:
                running = False

        #collision detection for haduken
        for had in haduk:
            for bd in chars['bulldog']:
                if len(chars['bulldog']) > 0:
                    if had.y - 11 < bd.hitbox[1] + bd.hitbox[3] and had.y > bd.hitbox[1]:
                        if had.x + 13 > bd.hitbox[0] and had.x - 13 < bd.hitbox[0] + bd.hitbox[2]:
                            bd.hit()
                            haduk.pop(haduk.index(had))
                            cash.append(characters.Bucks(bd.x, bd.y))
                            chars['bulldog'].pop()
            for kn in chars['knight']:
                if len(chars['knight']) > 0:
                    if had.y - 11 < kn.hitbox[1] + kn.hitbox[3] and had.y > kn.hitbox[1]:
                        if had.x + 13 > kn.hitbox[0] and had.x - 13 < kn.hitbox[0] + kn.hitbox[2]:
                            kn.hit()
                            haduk.pop(haduk.index(had))
                            cash.append(characters.Bucks(kn.x, kn.y))
                            chars['knight'].pop()           

            if had.x < 1440 and had.x > 0:
                had.x = had.x + had.vel
            else:
                haduk.pop(haduk.index(had))

        #collision detection for player    
        for bd in chars['bulldog']:
            if len(chars['bulldog']) > 0:
                if chars['player'].y < bd.hitbox[1] + bd.hitbox[3] and chars['player'].y > bd.hitbox[1]:
                    if chars['player'].x > bd.hitbox[0] and chars['player'].x < bd.hitbox[0] + bd.hitbox[2]:
                        chars['player'].take_damage()
        for kn in chars['knight']:
            if len(chars['knight']) > 0:
                if chars['player'].y < kn.hitbox[1] + kn.hitbox[3] and chars['player'].y > kn.hitbox[1]:
                    if chars['player'].x > kn.hitbox[0] and chars['player'].x < kn.hitbox[0] + kn.hitbox[2]:
                        chars['player'].take_damage()
        for cs in items['cash']:
            if len(items['cash']) > 0:
                if chars['player'].y < cs.hitbox[1] + cs.hitbox[3] and chars['player'].y > cs.hitbox[1]:
                    if chars['player'].x > cs.hitbox[0] and chars['player'].x < cs.hitbox[0] + cs.hitbox[2]:
                        chars['player'].gain_coin()
                        items['cash'].pop(items['cash'].index(cs))
        for ora in items['oranges']:
            if len(items['oranges']) > 0:
                if chars['player'].y < ora.hitbox[1] + ora.hitbox[3] and chars['player'].y > ora.hitbox[1]:
                    if chars['player'].x > ora.hitbox[0] and chars['player'].x < ora.hitbox[0] + ora.hitbox[2]:
                        chars['player'].gain_orange()
                        items['oranges'].pop(items['oranges'].index(ora))

        pressed_keys = pg.key.get_pressed()
        chars['player'].update(pressed_keys)

        if pressed_keys[K_SPACE] and haduk_loop == 0:
            if chars['player'].left:
                facing = -1
            elif chars['player'].right:
                facing = 1
            else:
                if chars['player'].wasLeft:
                    facing = -1
                else:
                    facing = 1
            if len(haduk) < 5:
                #haduk.append(characters.Haduken(round((chars['player'].x + chars['player'].width)//2), round((chars['player'].y + chars['player'].height)//2), facing))
                haduk.append(characters.Haduken(chars['player'].x, chars['player'].y, facing))
            haduk_loop = 1

        redrawGameWindow(screen, background, chars, terr, background_x, haduk, items)

        clock.tick(60)

    # Done! Time to quit.
    pg.quit()


def redrawGameWindow(screen, background, chars, terr, background_x, haduk, items) :
    relative_background_x = background_x[0] % background.get_rect().width
    screen_width = background.get_rect().width

    screen.blit(background, (relative_background_x - screen_width,0))

    if relative_background_x < screen_width :
        screen.blit(background, (relative_background_x, 0))

    if chars['player'].walkCount + 1 >= 59 :
        chars['player'].walkCount = 0
    if chars['player'].left :
        screen.blit(chars['player'].walkLeft[chars['player'].walkCount//10], (chars['player'].x, chars['player'].y))
        chars['player'].walkCount += 1
    elif chars['player'].right :
        screen.blit(chars['player'].walkRight[chars['player'].walkCount//10], (chars['player'].x, chars['player'].y))
        chars['player'].walkCount += 1
        if chars['player'].x >= screen_width * 4 / 5 - chars['player'].width * 3 - chars['player'].vel :
            background_x[0] -= 5
    else :
        if chars['player'].wasLeft :
            screen.blit(chars['player'].player_standL, (chars['player'].x, chars['player'].y))
        else :
            screen.blit(chars['player'].player_standR, (chars['player'].x, chars['player'].y))
    chars['player'].hitbox = (chars['player'].x, chars['player'].y, 24, 36)
    pg.draw.rect(screen, (255,0,0), chars['player'].hitbox, 2)

    for had in haduk:
        had.draw(screen)
    for bull in chars['bulldog']:
        bull.draw(screen)
    for kni in chars['knight']:
        kni.draw(screen)
    for buck in items['cash']:
        buck.draw(screen) 
    for citrus in items['oranges']:
        citrus.draw(screen)    
    

    for y in range(24, 18, -1) :
        for x in range(33) :
            terr['dirt'].draw(screen, x * terr['dirt'].width, y * terr['dirt'].height)
    for x in range (33) :
        terr['grass'].draw(screen, x * terr['grass'].width, 570) #take screen_height and - dirt layers
    
    terr['platform_br'].draw(screen)
    pg.display.update()


def Start_Menu():
    window = tk.Tk()
    window['background']='orange'
    window.overrideredirect(1)

    w = 334# width for the Tk root
    h = 286 # height for the Tk root

    # get screen width and height
    ws = window.winfo_screenwidth() # width of the screen
    hs = window.winfo_screenheight() # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    # set the dimensions of the screen 
    # and where it is placed
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    window.resizable(False,False)
    clickables = tk.Frame(master=window)
    title = tk.Label(master=window,text="Main Menu", font=("Trebuchet MS",42), bg='orange',
    fg = 'blue')
    title.grid(row=0,column=0)

    start_game = tk.Button(
        master=clickables,
        text="Start New Game",
        width = 18,
        height = 1, 
        font=("Trebuchet MS",24),
        command=lambda:multifunction(window.destroy(),Game_Loop()),
        bg = 'white',
        fg = 'blue'
    )
    start_game.pack()
    disp_highscores = tk.Button(
        master=clickables,
        text="Display Highscores",
        width = 18,
        height = 1, 
        font=("Trebuchet MS",24),
        bg = 'white',
        fg = 'blue'
    )
    disp_highscores.pack()
    quit_game = tk.Button(
        master=clickables,
        text="Quit to Desktop",
        width = 18,
        height = 1, 
        font=("Trebuchet MS",24),
        command=lambda: multifunction(window.destroy(), pg.quit()),
        bg = 'white',
        fg = 'blue'
    )
    quit_game.pack()
 
    clickables.grid(row=1,column=0)

    window.mainloop()


def InGame_Menu():
    window = tk.Tk()
    window['background'] = 'orange'
    window.overrideredirect(1)

    w = 334# width for the Tk root
    h = 356 # height for the Tk root

    # get screen width and height
    ws = window.winfo_screenwidth() # width of the screen
    hs = window.winfo_screenheight() # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    # set the dimensions of the screen 
    # and where it is placed
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    window.resizable(False,False)
    clickables = tk.Frame(master=window)
    title = tk.Label(master=window,text="Game Menu", font=("Trebuchet MS",42), bg='orange',
    fg = 'blue')
    title.grid(row=0,column=0)

    resume_game = tk.Button(
        master=clickables,
        text="Resume Game",
        width = 18,
        height = 1, 
        font=("Trebuchet MS",24),
        command=lambda:window.destroy(), 
        bg = 'white',
        fg = 'blue'
    )
    resume_game.pack()
    exchange = tk.Button(
        master=clickables,
        text="Exchange Flex Bucks",
        width = 18,
        height = 1, 
        font=("Trebuchet MS",24),
        bg = 'white',
        fg = 'blue'
    )
    exchange.pack()
    return_main_menu = tk.Button(
        master=clickables,
        text="Quit to Main Menu",
        width = 18,
        height = 1, 
        font=("Trebuchet MS",24),
        command=lambda:multifunction(window.destroy(),Start_Menu()),
        bg = 'white',
        fg = 'blue'
    )
    return_main_menu.pack()
    quit_game = tk.Button(
        master=clickables,
        text="Quit to Desktop",
        width = 18,
        height = 1, 
        font=("Trebuchet MS",24),
        command=lambda:multifunction(window.destroy(),pg.quit()),
        bg = 'white',
        fg = 'blue'
    )
    quit_game.pack()

    clickables.grid(row=1,column=0)

    window.mainloop()


def multifunction(*args):
    for function in args:
        function()


Main()
