import characters
import terrain
import random
import pygame as pg
import tkinter as tk
from pygame.locals import *

def Main():

    Start_Menu()

def Game_Loop():

    platform_enemies = []
    floor_enemies = []
    enemiesCount = [0]
    bulldogs = []
    knights = []

    chars = {
    'player' : characters.Gator(),
    'bulldogs' : bulldogs,
    'knights' : knights
    }

    platforms = []
    
    terr = {
        'grass' : terrain.Grass(),
        'dirt' : terrain.Dirt(),
        'platforms' : platforms
    }

    screen_width = 1440
    screen_height = 720
    screen = pg.display.set_mode([screen_width, screen_height])
    background = pg.image.load('background.png')
    background_x = [0]
    clock = pg.time.Clock()

    haduk = []
    haduk_loop = 0

    steps = [0]

    pg.init()
    pg.time.set_timer(USEREVENT + 1, random.randrange(2500, 3500))

    # Run until the user asks to quit
    running = True
    while running:

        if haduk_loop > 0 :
            haduk_loop += 1
        if haduk_loop > 5 :
            haduk_loop = 0
        #get every event in the queue
        for event in pg.event.get():
            if event.type == KEYDOWN :
                if event.key == K_ESCAPE :
                    running = False
                elif event.key == K_m :
                    InGame_Menu()

            if event.type == USEREVENT + 1 and enemiesCount[0] < 1:
                r = random.randrange(0, 6)
                if platforms :
                    platSpawn = random.randrange(0, 3)
                else :
                    platSpawn = 0
                if platSpawn < 3 :
                    for x in platforms : 
                        r = random.randrange(0, 2)
                        if r == 0 :
                            dog = characters.Bulldog(x.x, x.y - 64, x.x + x.width * 2)
                            dog.onPlatform = True
                            bulldogs.append(dog)
                        else :
                            knight = characters.Knight(x.x, x.y - 64, x.x + x.width * 2)
                            knight.onPlatform = True
                            knights.append(knight)
                        enemiesCount[0] += 1
                else :
                    r = random.randrange(0, 5)
                    if r < 3 :
                        bulldogs.append(characters.Bulldog(0, 503, screen_width))
                    else :
                        knights.append(characters.Knight(0, 502, screen_width))
                    enemiesCount[0] += 1

            # Did the user click the window close button? If so, stop the loop.
            if event.type == QUIT:
                running = False

        #moving this up to allow enemies to spawn on potential platforns
        #USE THIS TO SPAWN ORANGES AS WELL
        if steps[0] == 720 :
            steps[0] = 0
            r = random.randrange(0, 21)
            y_pos = random.randrange(400, 461)
            #1 small brown platform
            if r < 6:
                platforms.append(terrain.Platform(background.get_rect().width, y_pos))
            else :
                #1 long brown platform
                platforms.append(terrain.LongPlatform(background.get_rect().width, y_pos))
                #1 long and 1 short above 
                if r > 13 :
                    y_pos = random.randrange(244, 322)
                    x_pos = random.randrange(0, 97)
                    platforms.append(terrain.Platform(background.get_rect().width + x_pos, y_pos))
        
        for had in haduk:
            if had.x < 1440 and had.x > 0:
                had.x = had.x + had.vel
            else:
                haduk.pop(haduk.index(had))
        
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
            if len(haduk) < 3:
                haduk.append(characters.Haduken(chars['player'].x, chars['player'].y, facing))
            haduk_loop = 1

        redrawGameWindow(screen, background, chars, terr, background_x, haduk, steps, enemiesCount)

        clock.tick(60)

    # Done! Time to quit.
    pg.quit()


def redrawGameWindow(screen, background, chars, terr, background_x, haduk, steps, enemiesCount) :
    relative_background_x = background_x[0] % background.get_rect().width
    screen_width = background.get_rect().width

    screen.blit(background, (relative_background_x - screen_width,0))

    if relative_background_x < screen_width :
        screen.blit(background, (relative_background_x, 0))

    for dog in chars['bulldogs'] :
        dog.option = 1
    for knight in chars['knights'] :
        knight.option = 1
    
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
            steps[0] += 5
            if terr['platforms'] :
                for x in terr['platforms'] :
                    x.x -= 5
                    if x.x < - (x.width * 3):
                        terr['platforms'].pop(0)
            for dog in chars['bulldogs'] :
                if dog.onPlatform :
                    dog.path[0] -= 5
                    dog.path[1] -= 5
                    if dog.path[1] < 0 :
                        dog.kill()
                        enemiesCount[0] -= 1
                    if dog.isRight :
                        dog.option = 2
            for knight in chars['knights'] :
                if knight.onPlatform :
                    knight.path[0] -= 5
                    knight.path[1] -= 5
                    if knight.path[1] < 0 :
                        knight.kill()
                        enemiesCount[0] -= 1
                if knight.isRight : 
                    knight.option = 2

    else :
        if chars['player'].wasLeft :
            screen.blit(chars['player'].player_standL, (chars['player'].x, chars['player'].y))
        else :
            screen.blit(chars['player'].player_standR, (chars['player'].x, chars['player'].y))
    
    for had in haduk:
        had.draw(screen)

    for x in terr['platforms'] :
        x.draw(screen)

    for y in range(24, 18, -1) :
        for x in range(33) :
            terr['dirt'].draw(screen, x * terr['dirt'].width, y * terr['dirt'].height)
    for x in range (33) :
        terr['grass'].draw(screen, x * terr['grass'].width, 570) #take screen_height and - dirt layers
    
    for dog in chars['bulldogs'] :
        dog.draw(screen)

    for knight in chars['knights'] :
        knight.draw(screen)

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
