import characters
import random
import pygame as pg
import tkinter as tk
from pygame.locals import *




def Main():

    Start_Menu() 

def Game_Loop():

    chars = {
    'player' : characters.Gator(),
    'bulldog' : characters.Bulldog(100, 360, 1340), 
    'knight' : characters.Knight(100, 450, 1180)
    }
    haduk = []

    screen_width = 1440
    screen_height = 720

    screen = pg.display.set_mode([screen_width, screen_height])
    background = pg.image.load('background.png')

    clock = pg.time.Clock()

    pg.init()
    # Run until the user asks to quit
    running = True
    while running:

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
        
        for had in haduk:
            if had.x < 1440 and had.x > 0:
                had.x = had.x + had.vel
            else:
                haduk.pop(haduk.index(had))

        pressed_keys = pg.key.get_pressed()
        chars['player'].update(pressed_keys)

        if pressed_keys[K_SPACE]:
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
                #haduk.append(characters.Haduken(round((chars['player'].x + chars['player'].width)//2), round((chars['player'].y + chars['player'].height)//2), facing))
                haduk.append(characters.Haduken(chars['player'].x, chars['player'].y, facing))

        redrawGameWindow(screen, background, chars, haduk)

        clock.tick(60)

    # Done! Time to quit.
    pg.quit()


def redrawGameWindow(screen, background, chars, haduk):
    screen.blit(background, (0,0))

    if chars['player'].walkCount + 1 >= 59 :
        chars['player'].walkCount = 0
    if chars['player'].left :
        screen.blit(chars['player'].walkLeft[chars['player'].walkCount//10], (chars['player'].x, chars['player'].y))
        chars['player'].walkCount += 1
    elif chars['player'].right :
        screen.blit(chars['player'].walkRight[chars['player'].walkCount//10], (chars['player'].x, chars['player'].y))
        chars['player'].walkCount += 1
    else :
        if chars['player'].wasLeft :
            screen.blit(chars['player'].player_standL, (chars['player'].x, chars['player'].y))
        else :
            screen.blit(chars['player'].player_standR, (chars['player'].x, chars['player'].y))
    
    for had in haduk:
        had.draw(screen)
    chars['bulldog'].draw(screen)
    chars['knight'].draw(screen)

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
