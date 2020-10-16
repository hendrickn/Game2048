from grid_2048_suite import *
from grid_display import *
from tiles import *
from textual_2048 import *
import random as rd

THEMES = {"0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}


def random_play():
    n = read_size_grid()
    theme = THEMES[read_theme_grid()]
    grid = init_game(n)
    print(grid_to_string_with_size_and_theme(grid, theme, n))
    while not is_game_over(grid):
        M = move_possible(grid)
        moves = ''
        if M[0]:
            moves += 'g'
        if M[1]:
            moves += 'd'
        if M[2]:
            moves += 'h'
        if M[3]:
            moves += 'b'
        k = rd.randint(0,len(moves)-1)  ##On choisit un mouvement aléatoire parmis les possibles
        d = moves[k]
        grid = move_grid(grid, d)

        grid = grid_add_new_tile(grid)

        print(grid_to_string_with_size_and_theme(grid, theme, n))       ##On affiche a grille
    if get_grid_tile_max(grid) > 2048:
        print('Cest gagné')
    else:
        print('Perdu...')


def game_play():
    n = read_size_grid()
    theme = THEMES[str(read_theme_grid())]
    grid = init_game(n)
    print(grid_to_string_with_size_and_theme(grid, theme, n))
    while not is_game_over(grid):
        M = move_possible(grid)
        d = read_player_command()
        if d == 'g':
            k = 0
        if d == 'd':
            k = 1
        if d == 'h':
            k = 2
        if d == 'b':
            k = 3
        if not M[k]:
            continue
        grid = move_grid(grid, d)

        grid = grid_add_new_tile(grid)

        print(grid_to_string_with_size_and_theme(grid, theme, n))
    if get_grid_tile_max(grid) > 2048:
        print('Cest gagné')
    else:
        print('Perdu...')

game_play()
