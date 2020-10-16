from tkinter import *
from grid_2048_suite import *
from tiles import *
import copy


THEMES = {"0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}

TILES_BG_COLOR = {0: "#9e948a", 2: "#eee4da", 4: "#ede0c8", 8: "#f1b078", \
                  16: "#eb8c52", 32: "#f67c5f", 64: "#f65e3b", \
                  128: "#edcf72", 256: "#edcc61", 512: "#edc850", \
                  1024: "#edc53f", 2048: "#edc22e", 4096: "#5eda92", \
                  8192: "#24ba63"}

TILES_FG_COLOR = {0: "#776e65", 2: "#776e65", 4: "#776e65", 8: "#f9f6f2", \
                  16: "#f9f6f2", 32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2", \
                  256: "#f9f6f2", 512: "#f9f6f2", 1024: "#f9f6f2", \
                  2048: "#f9f6f2", 4096: "#f9f6f2", 8192: "#f9f6f2"}

TILES_FONT = ["Verdana", 40, "bold"]

def str_to_list(str) : #### On convertit un string de liste de liste en liste de liste
    L=[]
    Lloc=[]
    sloc=''
    n=len(str)
    for i in range(2,n) :
        if str[i]==']':
            sloc=sloc.replace('[','')
            sloc=sloc.replace(']','')
            sloc=sloc.replace(',','')
            Lloc.append(int(sloc))
            sloc=''
            L.append(Lloc)
            Lloc=[]
            if str[i+1]==']' :
                print(L)
                return L
            else :
                i+=2
        if str[i]==',' and str[i+1]!='[' :
            sloc=sloc.replace('[','')
            sloc=sloc.replace(']','')
            sloc=sloc.replace(',','')
            if sloc!=' ' :
                Lloc.append(int(sloc))
            sloc=''
        else :
            if str[i]=='[' :
                continue
            else :
                sloc+=str[i]


def graphical_grid_init():
    def Save() :
        ###Fonction pour sauvegarder la grille
        file=open("Save.txt","w+")
        file.seek(0)
        file.truncate()
        file.write(str(game_grid))
    def Load() :
        ### Fonction pour charger la sauvegarde
        global game_grid
        file=open("Save.txt","r+")
        game_grid=str_to_list(file.read())
        display_and_update_graphical_grid()

    def Cancel() :
        ### Fonction pour annuler le dernier coup joué
        global game_grid
        global game_grid_copy
        game_grid= copy.deepcopy(game_grid_copy)
        display_and_update_graphical_grid()

    root = Tk()     ##On crée la fenêtre
    root.title('2048')
    top = Toplevel(bg = '#9e948a')
    top.title('2048')
    top.lower()

    labeltaille = Label(root, text = 'Taille de la grille')     ## Jusqu'à la ligne 114, on configure la fenêtre de paramètres avec les boutons
    labeltaille.grid(row = 0)

    f1 = Frame(root)
    spinbox = Spinbox(f1, from_ = 4, to = 9)
    f1.grid(row = 1)
    spinbox.grid()

    f2 = Frame(root)

    listbox = Listbox(f2, height = 3, selectmode = 'single')
    listbox.insert(0, 'Default')
    listbox.insert(1, 'Chemistry')
    listbox.insert(2, 'Alphabet')

    f2.grid(row = 3)
    listbox.grid()

    labeltheme = Label(root, text = 'Thème')
    labeltheme.grid(row = 2)

    ftheme = Frame(root, bd = 1, relief = 'solid')
    Label(ftheme, text = '')

    Button(root, text='Load', command=Load).grid(row=2, column=1, sticky=W, pady=4)
    Button(root, text='Save', command=Save).grid(row=3, column=1, sticky=W, pady=4)
    Button(root, text='Cancel', command=Cancel).grid(row=4, column=0, sticky=W, pady=4)

    quit_button = Button(root,
                   text="QUIT",
                   activebackground = "blue",
                   fg="#8D021F",
                   command=quit)
    quit_button.grid(row = 0, column = 1)

    global background
    background = Frame(top)
    background.grid()

    global grid_size
    grid_size = 4 #taille par défaut
    global theme
    theme = "0" #thème par défaut


    global graphical_grid       ##Graphical_grid contient le label de chaque frame, qui est mis à jour à chaque mouvement, il est initialisé à une grille vide
    graphical_grid = [[Label(Frame(background, bg = TILES_BG_COLOR[0],\
                                bd = 2, relief = 'groove'), text = ' ',\
                                height = int(15/grid_size), width = int(20/grid_size),\
                                bg = TILES_BG_COLOR[0], bd = 2, relief = 'groove') for i in range(grid_size)]\
                        for j in range(grid_size)]

    def size_and_theme_choice():
        global grid_size
        global game_grid
        global theme
        global background
        global graphical_grid
        global game_grid_copy

        grid_size = int(spinbox.get())
        if len(listbox.curselection()) > 0:
            theme = str(listbox.curselection()[0])
        game_grid = init_game(grid_size)
        graphical_grid = [[Label(Frame(background), text = ' ', font = (TILES_FONT[0], TILES_FONT[1], TILES_FONT[2]), height = int(15/grid_size), width = int(20/grid_size), bg = TILES_BG_COLOR[0], bd = 2, relief = 'groove') for i in range(grid_size)] for j in range(grid_size)]

        background.destroy()
        background = Frame(top)
        background.grid()       ##On initialise le jeu en fonction des paramètres


        for i in range(grid_size):
            for j in range(grid_size):
                tile = Frame(background)
                graphical_grid[i][j] = Label(tile, text = ' ', height = int(30/grid_size), width = int(50/grid_size), bg = TILES_BG_COLOR[0], bd = 2, relief = 'groove')
                graphical_grid[i][j].grid(row = i, column = j)
                tile.grid(row = i, column = j)  ## On crée la grille
        display_and_update_graphical_grid()

    play_button = Button(root,
                   text="PLAY",
                   bg = "blue",
                   fg="#0F52BA",
                   command=size_and_theme_choice)
    play_button.grid(row = 4, column = 1)


    global game_grid
    game_grid = init_game(grid_size) #grille par défaut


    def display_and_update_graphical_grid():
        ##On change l'interface graphique en fonction des données contenues dans game_grid, qui est une variable globale

        global graphical_grid

        global grid_size
        for i in range(grid_size):
            for j in range(grid_size):
                tile_value = game_grid[i][j]
                if tile_value != 0:
                    graphical_grid[i][j].configure(text = THEMES[theme][tile_value], font = (TILES_FONT[0], TILES_FONT[1], TILES_FONT[2]), height = int(15/grid_size), width = int(20/grid_size), bg = TILES_BG_COLOR[tile_value], bd = 2, relief = 'ridge')

                else:
                    graphical_grid[i][j].configure(text = ' ', font = (TILES_FONT[0], TILES_FONT[1], TILES_FONT[2]), height = int(15/grid_size), width = int(20/grid_size), bg = TILES_BG_COLOR[tile_value], bd = 2, relief = 'groove')


    display_and_update_graphical_grid()

    def game_over_test(game_grid):
        if is_game_over(game_grid):
            if get_grid_tile_max(game_grid) < 2048:
                Label(top, text = 'game over', font = ('Verdana', 40, 'bold'), bg = '#9e948a').grid()
            else:
                Label(top, text = "c'est gagné", font = ('Verdana', 40, 'bold'), bg = '#9e948a').grid()

    def KeyPressed(event):
        ## On lie les flèches du clavier au jeu 2048
        global game_grid
        global game_grid_copy
        M = move_possible(game_grid)
        if event.keysym == 'Left':
            if M[0]:
                game_grid_copy=copy.deepcopy(game_grid)
                game_grid = move_grid(game_grid, 'g')
                game_grid = grid_add_new_tile(game_grid)
                game_over_test(game_grid)
                display_and_update_graphical_grid()
        if event.keysym == 'Right':
            if M[1]:
                game_grid_copy=copy.deepcopy(game_grid)
                game_grid = move_grid(game_grid, 'd')
                game_grid = grid_add_new_tile(game_grid)
                game_over_test(game_grid)
                display_and_update_graphical_grid()
        if event.keysym == 'Up':
            if M[2]:
                game_grid_copy=copy.deepcopy(game_grid)
                game_grid = move_grid(game_grid, 'h')
                game_grid = grid_add_new_tile(game_grid)
                game_over_test(game_grid)
                display_and_update_graphical_grid()
        if event.keysym == 'Down':
            if M[3]:
                game_grid_copy=copy.deepcopy(game_grid)
                game_grid = move_grid(game_grid, 'b')
                game_grid = grid_add_new_tile(game_grid)
                game_over_test(game_grid)
                display_and_update_graphical_grid()

    top.bind('<Key>', KeyPressed)

    root.mainloop()
    top.mainloop()


graphical_grid_init()
