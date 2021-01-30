import characters
import random
import pygame as pg
import tkinter as tk
from pygame.locals import *



screen_width = 1920
screen_height = 1080

screen = pg.display.set_mode([screen_width, screen_height])
background = pg.image.load('background.png')

clock = pg.time.Clock()

player = characters.Gator()
bulldog = characters.Bulldog()
knight = characters.Knight()

def redrawGameWindow() :
    screen.blit(background, (0,0))
    screen.blit(bulldog.surf, bulldog.rect)
    screen.blit(knight.surf, knight.rect)

    if player.walkCount + 1 >= 59 :
        player.walkCount = 0
    if player.left :
        screen.blit(player.walkLeft[player.walkCount//10], (player.x, player.y))
        player.walkCount += 1
    elif player.right :
        screen.blit(player.walkRight[player.walkCount//10], (player.x, player.y))
        player.walkCount += 1
    else :
        if player.wasLeft :
            screen.blit(player.player_standL, (player.x, player.y))
        else :
            screen.blit(player.player_standR, (player.x, player.y))
        
    pg.display.update()

def Main():

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
        player.update(pressed_keys)
        redrawGameWindow()

        clock.tick(60)

    # Done! Time to quit.
    pg.quit()

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
    buttons = tk.Frame(master=window)
    title = tk.Label(master=window,text="Main Menu", font=("Trebuchet MS",42))
    title.grid(row=0,column=0)

    start_game = tk.Button(
        master=buttons,
        text="Start New Game",
        width = 18,
        height = 1, 
        font=("Trebuchet MS",24),
        command=lambda : Start(window)
    )
    start_game.pack()
    disp_highscores = tk.Button(
        master=buttons,
        text="Display Highscores",
        width = 18,
        height = 1, 
        font=("Trebuchet MS",24)
    )
    disp_highscores.pack()
    exchange = tk.Button(
        master=buttons,
        text="Exchange Flex Bucks",
        width = 18,
        height = 1, 
        font=("Trebuchet MS",24)
    )
    exchange.pack()
    leave = tk.Button(
        master=buttons,
        text="Exit Main Menu",
        width = 18,
        height = 1,
        font=("Trebuchet MS",24)
    )
    leave.pack()

    buttons.grid(row=1,column=0)

    window.mainloop()
    
def Start(menu_window):
    menu_window.destroy()
    Main()

Menu()
