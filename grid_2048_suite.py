import numpy as np
from tiles import get_all_tiles
import copy

## Left move

def tiles_to_left(row): #On décale à gauche les tuiles
    n = len(row)
    if n > 0:
        if set(row) != {0}:
            if row[0] == 0:
                del row[0]
                row.append(0)
                return tiles_to_left(row)
            else:
                return [row[0]] + tiles_to_left(row[1:])
        else:
            return row
    return []

def move_row_left(row):     ##Décale toutes les tuiles de la grille à gauche
    n = len(row)
    for i in range(n-1):
        row[i:] = tiles_to_left(row[i:])
        if row[i] == row[i+1]:
            row[i] *= 2
            row[i+1] = 0
    return row

## Right move

def reverse(list):
    return list[::-1]

def tiles_to_right(row): #On décale à droite les tuiles
    n = len(row)
    if n > 0:
        if set(row) != {0}:
            if row[n-1] == 0:
                del row[n-1]
                return [0] + tiles_to_right(row)
            else:
                return tiles_to_right(row[0:n-1]) + [row[n-1]]
        else:
            return row
    return []

def move_row_right(row):
    return reverse(move_row_left(reverse(row)))

def move_grid(grid, d):
    gridbis = copy.deepcopy(grid)
    n = len(gridbis)
    if d == 'g':
        for i in range(n):
            gridbis[i] = move_row_left(gridbis[i])
        return gridbis
    if d == 'd':
        for i in range(n):
            gridbis[i] = move_row_right(gridbis[i])
        return gridbis
    if d == 'h':
        ##Pour faire un mouvement en haut, on transpose la grille, on déplace à gauche et on retranspose
        return (np.array(move_grid((np.array(gridbis).T).tolist(), 'g')).T).tolist()
    if d == 'b':
        return (np.array(move_grid((np.array(gridbis).T).tolist(), 'd')).T).tolist()

def is_grid_full(grid):
    return 0 not in get_all_tiles(grid)

def move_possible(grid):        ## Donne la liste des mouvements possible
    return [move_grid(grid, 'g') != grid, move_grid(grid, 'd') != grid, move_grid(grid, 'h') != grid, move_grid(grid, 'b') != grid]

def is_game_over(grid):
    return is_grid_full(grid) and (move_possible(grid) == [False, False, False, False])

def get_grid_tile_max(grid):
    return max(get_all_tiles(grid))


