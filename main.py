import characters
import random
import pygame as pg
import tkinter as tk
from pygame.locals import *




def Main():

    Menu()
    Game_Loop() 

def Game_Loop():

    chars = {
    'player' : characters.Gator(),
    'bulldog' : characters.Bulldog(100, 360, 1340), 
    'knight' : characters.Knight(100, 450, 1180)
    }

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
                    Menu()

            # Did the user click the window close button? If so, stop the loop.
            if event.type == QUIT:
                running = False
        
        pressed_keys = pg.key.get_pressed()
        chars['player'].update(pressed_keys)
        redrawGameWindow(screen, background, chars)

        clock.tick(60)

    # Done! Time to quit.
    pg.quit()


def redrawGameWindow(screen, background, chars) :
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
    
    chars['bulldog'].draw(screen)
    chars['knight'].draw(screen)

    pg.display.update()


def Menu():
    window = tk.Tk()

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
    title = tk.Label(master=window,text="Main Menu", font=("Trebuchet MS",42))
    title.grid(row=0,column=0)

    start_game = tk.Button(
        master=clickables,
        text="Start New Game",
        width = 18,
        height = 1, 
        font=("Trebuchet MS",24),
        command=lambda:multifunction(window.destroy(), Game_Loop())
    )
    start_game.pack()
    disp_highscores = tk.Button(
        master=clickables,
        text="Display Highscores",
        width = 18,
        height = 1, 
        font=("Trebuchet MS",24)
    )
    disp_highscores.pack()
    exchange = tk.Button(
        master=clickables,
        text="Exchange Flex Bucks",
        width = 18,
        height = 1, 
        font=("Trebuchet MS",24)
    )
    exchange.pack()
    resume = tk.Button(
        master=clickables,
        text="Resume Game",
        width = 18,
        height = 1,
        font=("Trebuchet MS",24),
        command=lambda:Resume_Game(window)
    )
    resume.pack()

    clickables.grid(row=1,column=0)

    window.mainloop()
    

def Resume_Game(menu_window):
    menu_window.destroy()


def multifunction(*args):
    for function in args:
        function()


Main()

