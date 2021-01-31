import characters
import terrain
import random
import pygame as pg
import tkinter as tk
import os
from settings import screen,screen_width,screen_width 
from pygame.locals import *

def Main():

    Start_Menu() 

def Game_Loop():

    chars = {
    'player' : characters.Gator(),
    'bulldog' : characters.Bulldog(100, 360, 1340), 
    'knight' : characters.Knight(100, 450, 1180)
    }

    terr = {
        'grass' : terrain.Grass(),
        'dirt' : terrain.Dirt(),
        'platform_br' : terrain.Platform(1000, 400)
    }

    haduk = []

    background = pg.image.load('background.png')
    background_x = [0]

    clock = pg.time.Clock()
    # Run until the user asks to quit
    running = True
    dead = False
    while running:
        #get every event in the queue
        if dead:
            Death_Screen()
        for event in pg.event.get():
            if event.type == KEYDOWN :
                if event.key == K_ESCAPE :
                    InGame_Menu()
                if event.key == K_m :
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


        redrawGameWindow(screen, background, chars, terr, background_x, haduk)

        clock.tick(60)

    # Done! Time to quit.
    pg.quit()


def redrawGameWindow(screen, background, chars, terr, background_x, haduk) :
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
    
    for had in haduk:
        had.draw(screen)
    chars['bulldog'].draw(screen)
    chars['knight'].draw(screen)
    for y in range(24, 18, -1) :
        for x in range(33) :
            terr['dirt'].draw(screen, x * terr['dirt'].width, y * terr['dirt'].height)
    for x in range (33) :
        terr['grass'].draw(screen, x * terr['grass'].width, 570) #take screen_height and - dirt layers
    
    terr['platform_br'].draw(screen)
    pg.display.update()


def Start_Menu():
    Menu_Background()
    
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

    # create button image labels
    images = {
        'highscores' : tk.PhotoImage(file=r"Menu/Buttons/Leaderboard.png"),
        'back' : tk.PhotoImage(file="Menu/Buttons/Back.png"),
        'play' : tk.PhotoImage(file="Menu/Buttons/Play.png"),
        'close' : tk.PhotoImage(file="Menu/Buttons/Close.png"),
    }
    clickables = tk.Frame(master=window)
    title = tk.Label(master=window,text="Main Menu", font=("Trebuchet MS",42), bg='orange',
    fg = 'blue')
    title.grid(row=0,column=0,sticky='')

    start_game = tk.Button(
        master=clickables,
        text="   New Game",
        width = 334,
        height = 50, 
        font=("Trebuchet MS",24),
        command=lambda:multifunction(window.destroy(),Story(),Game_Loop()),
        bg = 'white',
        fg = 'blue',
        image = images['play'],
        compound=tk.LEFT
    )
    start_game.pack(side = tk.TOP)

    disp_highscores = tk.Button(
        master=clickables,
        text="   Highscores",
        width = 334,
        height = 50, 
        font=("Trebuchet MS",24),
        bg = 'white',
        fg = 'blue',
        image = images['highscores'],
        compound = tk.LEFT
    )
    disp_highscores.pack()

    quit_game = tk.Button(
        master=clickables,
        text="   Quit Game",
        width = 334,
        height = 50, 
        font=("Trebuchet MS",24),
        command=lambda: multifunction(window.destroy(),pg.quit()),
        bg = 'white',
        fg = 'blue', 
        image=images['close'], 
        compound = tk.LEFT,
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


def Story():
    window = tk.Tk()
    window.overrideredirect(1)
    w = 500# width for the Tk root
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
    window.after(5000, lambda:window.destroy())
    story_text = """Defend your swamp from the evil Knights and Bulldogs!\n\nCollect 6 delicious oranges to win!"""
    story=tk.Label(window, height = 50, width = 200, text = story_text,
     wraplength=550, justify=tk.CENTER, bg='blue',fg='orange',font=('Trebucet MS',24))
    story.pack(side=tk.TOP)
    window.mainloop()


def Death_Screen():
    window=tk.Tk()
    window['background']='red'
    window.overrideredirect(1)
    frame=tk.Frame(window,borderwidth=0,highlightthickness=0,bg='red')
    frame.pack()
    w = 1000# width for the Tk root
    h = 750 # height for the Tk root
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
    game_over=tk.PhotoImage(file="GameOver.png")
    game_over_canvas = tk.Canvas(master=frame, bg='red', width=1000, height=500, highlightthickness=0)
    game_over_canvas.pack()
    game_over_canvas.create_image(500,261,image=game_over)

    dead_gator=tk.PhotoImage(file='DeadGator.png')
    dead_gator_canvas=tk.Canvas(master=frame,bg='red',width=200,height=125,highlightthickness=0)
    dead_gator_canvas.pack(side=tk.TOP)
    dead_gator_canvas.create_image(90,77,image=dead_gator)

    start_game = tk.Button(
        text="New Game",
        width = 15,
        height = 1, 
        font=("Trebuchet MS",24),
        command=lambda:multifunction(window.destroy(),Game_Loop()),
        bg = 'black',
        fg = 'red',
        compound=tk.LEFT
    )
    start_game.pack()

    quit_game = tk.Button(
        window,
        text="Quit to Desktop",
        width = 15,
        height = 1, 
        font=("Trebuchet MS",24),
        command=lambda:multifunction(window.destroy(),pg.quit()),
        bg = 'black',
        fg = 'red'
    )
    quit_game.pack()

    window.mainloop()


def Menu_Background():

    background = pg.image.load('background.png')
    screen.blit(background, (0,0))
    pg.display.update()


def multifunction(*args):
    for function in args:
        function()


Main()
