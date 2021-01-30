import tkinter as tk

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
        font=("Trebuchet MS",24)
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
