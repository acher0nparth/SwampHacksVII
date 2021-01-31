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
    pg.init()

    knights = []
    bulldogs = []
    cash = []
    oranges = []
    enemiesCount = [0]
    oranges_s = []
    heart = []

    global chars
    chars = {
    'player' : characters.Gator(),
    'bulldog' : bulldogs, 
    'knight' : knights
    }

    platforms = []
    
    terr = {
        'grass' : terrain.Grass(),
        'dirt' : terrain.Dirt(),
        'platforms' : platforms
    }

    items = {
        'cash' : cash,
        'oranges' : oranges,
        'oranges_s' : oranges_s,
        'heart' : heart
    }

    haduk = []
    haduk_loop = 0

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
        
        if haduk_loop > 0:
            haduk_loop += 1
        if haduk_loop > 10:
            haduk_loop = 0
        #get every event in the queue
        if chars['player'].isDead:
            Death_Screen()
        if chars['player'].oranges==6:
            Victory_Screen()
        for event in pg.event.get():
            if event.type == KEYDOWN :
                if event.key == K_ESCAPE :
                    InGame_Menu()
                if event.key == K_m :
                    InGame_Menu()

            if event.type == USEREVENT + 1 and enemiesCount[0] < 8:
                r = random.randrange(0, 6)
                if platforms :
                    platSpawn = random.randrange(0, 4)
                else :
                    platSpawn = 1
                if platSpawn < 1 :
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
                orange = random.randrange(0, 35)
                if orange < 1 :
                    oranges.append(characters.Orange(background.get_rect().width + 35, y_pos))
                platforms.append(terrain.Platform(background.get_rect().width, y_pos))
            else :
                orange = False
                if r > 14 :
                #1 long brown platform
                    oj = random.randrange(0, 35)
                    if oj < 1 :
                        oranges.append(characters.Orange(background.get_rect().width + 48, y_pos - 108))
                        orange = True
                    platforms.append(terrain.LongPlatform(background.get_rect().width, y_pos))
                    #1 long and 1 short above 
                    y_pos = random.randrange(244, 322)
                    x_pos = random.randrange(0, 97)
                    if not orange :
                        oj = random.randrange(0, 1)
                        if oj < 1 :
                            oranges.append(characters.Orange(background.get_rect().width + 64, y_pos - 108))
                            orange = True
                    platforms.append(terrain.Platform(background.get_rect().width + x_pos, y_pos))
        



        for had in haduk:
            for bd in chars['bulldog']:
                if len(chars['bulldog']) > 0:
                    if had.y - 11 < bd.hitbox[1] + bd.hitbox[3] and had.y > bd.hitbox[1]:
                        if had.x + 13 > bd.hitbox[0] and had.x - 13 < bd.hitbox[0] + bd.hitbox[2]:
                            bd.hit()
                            haduk.pop(haduk.index(had))
                            cash.append(characters.Bucks(bd.x, bd.y))
                            chars['bulldog'].pop(chars['bulldog'].index(bd))
                            enemiesCount[0] -= 1
            for kn in chars['knight']:
                if len(chars['knight']) > 0:
                    if had.y - 11 < kn.hitbox[1] + kn.hitbox[3] and had.y > kn.hitbox[1]:
                        if had.x + 13 > kn.hitbox[0] and had.x - 13 < kn.hitbox[0] + kn.hitbox[2]:
                            kn.hit()
                            haduk.pop(haduk.index(had))
                            cash.append(characters.Bucks(kn.x, kn.y))
                            chars['knight'].pop(chars['knight'].index(kn))           
                            enemiesCount[0] -= 1

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
                        items['heart'].pop() 
        for kn in chars['knight']:
            if len(chars['knight']) > 0:
                if chars['player'].y < kn.hitbox[1] + kn.hitbox[3] and chars['player'].y > kn.hitbox[1]:
                    if chars['player'].x > kn.hitbox[0] and chars['player'].x < kn.hitbox[0] + kn.hitbox[2]:
                        chars['player'].take_damage()
                        items['heart'].pop() 
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
    

        redrawGameWindow(screen, background, chars, terr, background_x, haduk, items, steps, enemiesCount)

        clock.tick(60)

    # Done! Time to quit.
    pg.quit()


def redrawGameWindow(screen, background, chars, terr, background_x, haduk, items, steps, enemiesCount) :
    relative_background_x = background_x[0] % background.get_rect().width
    screen_width = background.get_rect().width

    screen.blit(background, (relative_background_x - screen_width,0))

    if relative_background_x < screen_width :
        screen.blit(background, (relative_background_x, 0))

    for dog in chars['bulldog'] :
        dog.option = 1
    for knight in chars['knight'] :
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
            for buck in items['cash'] :
                buck.x -= 5
            for orange in items['oranges'] :
                orange.x -= 5
            if terr['platforms'] :
                for x in terr['platforms'] :
                    x.x -= 5
                    if x.x < - (x.width * 3):
                        terr['platforms'].pop(0)
            for dog in chars['bulldog'] :
                if dog.onPlatform :
                    dog.path[0] -= 5
                    dog.path[1] -= 5
                    if dog.path[1] < 0 :
                        chars['bulldog'].pop(chars['bulldog'].index(dog))
                        enemiesCount[0] -= 1
                    if dog.isRight :
                        dog.option = 2
            for knight in chars['knight'] :
                if knight.onPlatform :
                    knight.path[0] -= 5
                    knight.path[1] -= 5
                    if knight.path[1] < 0 :
                        chars['knight'].pop(chars['knight'].index(knight))
                        enemiesCount[0] -= 1
                if knight.isRight : 
                    knight.option = 2

    else :
        if chars['player'].wasLeft :
            screen.blit(chars['player'].player_standL, (chars['player'].x, chars['player'].y))
        else :
            screen.blit(chars['player'].player_standR, (chars['player'].x, chars['player'].y))
    chars['player'].hitbox = (chars['player'].x, chars['player'].y, 24, 36)
    pg.draw.rect(screen, (255,0,0), chars['player'].hitbox, 2)

    for had in haduk:
        had.draw(screen)

    for x in terr['platforms'] :
        x.draw(screen)
    for bull in chars['bulldog']:
        bull.draw(screen)
    for kni in chars['knight']:
        kni.draw(screen)
    for buck in items['cash']:
        buck.draw(screen) 
    for citrus in items['oranges']:
        citrus.draw(screen) 
    items['heart'].clear()
    for ht in range(chars['player'].health):
        items['heart'].append(characters.Heart(ht*48, 0))
    for love in items['heart']:
        love.draw(screen)
    items['oranges_s'].clear()
    for ora in range(chars['player'].oranges):
        items['oranges_s'].append(characters.Orange_Small(ora*32, 48))
    for small_citrus in items['oranges_s']:
        small_citrus.draw(screen)
    

    for y in range(24, 18, -1) :
        for x in range(33) :
            terr['dirt'].draw(screen, x * terr['dirt'].width, y * terr['dirt'].height)
    for x in range (33) :
        terr['grass'].draw(screen, x * terr['grass'].width, 570) #take screen_height and - dirt layers

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
    h = 460 # height for the Tk root

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
    clickables = tk.Frame(master=window, bg = 'white')
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

    ex_oranges = tk.Button(
        master=clickables,
        text="Flex Bucks to Oranges\n10:1",
        width = 18,
        height = 1, 
        font=("Trebuchet MS",24),
        bg = 'white',
        fg = 'blue', 
    )
    ex_oranges.config(command=lambda:Exchange_Oranges(ex_oranges))
    ex_oranges.pack()

    ex_health = tk.Button(
        master=clickables,
        text="Flex Bucks to HP\n5:1",
        width = 18,
        height = 1, 
        font=("Trebuchet MS",24),
        bg = 'white',
        fg = 'blue', 
    )
    ex_health.config(command=lambda:Exchange_Health(ex_health))
    ex_health.pack()

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
    w = 550# width for the Tk root
    h = 720 # height for the Tk root
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
    game_over_canvas = tk.Canvas(master=frame, bg='red', width=550, height=400, highlightthickness=0)
    game_over_canvas.pack()
    game_over_canvas.create_image(275,225,image=game_over)

    dead_gator=tk.PhotoImage(file='DeadGator.png')
    dead_gator_canvas=tk.Canvas(master=frame,bg='red',width=100,height=100,highlightthickness=0)
    dead_gator_canvas.pack(side=tk.TOP)
    dead_gator_canvas.create_image(50,50,image=dead_gator)


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
    quit_game.pack(side=tk.BOTTOM)

    start_game = tk.Button(
        text="New Game",
        width = 15,
        height = 1, 
        font=("Trebuchet MS",24),
        command=lambda:multifunction(window.destroy(),Game_Loop()),
        bg = 'black',
        fg = 'red',
    )
    start_game.pack(side=tk.BOTTOM)

    window.mainloop()


def Victory_Screen():
    window=tk.Tk()
    window['background']='blue'
    window.overrideredirect(1)
    frame=tk.Frame(window,borderwidth=0,highlightthickness=0,bg='blue')
    frame.pack(side=tk.TOP)
    w = 450# width for the Tk root
    h = 720 # height for the Tk root
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
    win=tk.PhotoImage(file="YouWin.png")
    win_canvas = tk.Canvas(master=frame, bg='blue', width=450, height=400, highlightthickness=0)
    win_canvas.pack()
    win_canvas.create_image(225,225, image=win)

    gator=tk.PhotoImage(file='WinGator.png')
    gator_canvas=tk.Canvas(master=frame,bg='blue',width=100,height=100,highlightthickness=0)
    gator_canvas.pack(side=tk.TOP)
    gator_canvas.create_image(50,50,image=gator)

    quit_game = tk.Button(
        window,
        text="Quit to Desktop",
        width = 15,
        height = 1, 
        font=("Trebuchet MS",24),
        command=lambda:multifunction(window.destroy(),pg.quit()),
        bg = 'orange',
        fg = 'blue'
    )
    quit_game.pack(side=tk.BOTTOM)

    start_game = tk.Button(
        text="New Game",
        width = 15,
        height = 1, 
        font=("Trebuchet MS",24),
        command=lambda:multifunction(window.destroy(),Game_Loop()),
        bg = 'orange',
        fg = 'blue'
    )
    start_game.pack(side=tk.BOTTOM)

    window.mainloop()


def Menu_Background():

    background = pg.image.load('background.png')
    screen.blit(background, (0,0))
    pg.display.update()


def Exchange_Oranges(button):
    if (chars['player'].coins >= 10):
        chars['player'].exchange_oranges()
        coins_left = str(chars['player'].coins)
        button.config(text="Exchange Complete!\n" + coins_left + " Flex Bucks left.",
        state=tk.DISABLED)
    else:
        coins_needed = str(10-chars['player'].coins)
        button.config(text="Not Enough Flex Bucks!\nYou need " + coins_needed + " more.",
        state=tk.DISABLED)

 
def Exchange_Health(button):
    if (chars['player'].coins >= 5 and chars['player'].health < 3):
        chars['player'].exchange_health()
        coins_left = str(chars['player'].coins)
        button.config(text="Exchange Complete!\n" + coins_left + " Flex Bucks left.",
        state=tk.DISABLED)
    elif chars['player'].health >= 3:
        button.config(text="You have max health!",
        state=tk.DISABLED)
    else:
        coins_needed = str(5-chars['player'].coins)
        button.config(text="Not Enough Flex Bucks!\nYou need " + coins_needed + " more.",
        state=tk.DISABLED)


def multifunction(*args):
    for function in args:
        function()


Main() 
