import random as rd
from grid_2048 import create_grid

def grid_add_new_tile_at_position(game_grid, x, y):  ## Ajoute une tuile à la case (x,y)
    n = rd.randint(0,9)
    if n < 9:
        tile = 2
    else:
        tile = 4

    game_grid[x][y] = tile
    return game_grid

def get_all_tiles(game_grid):       ## Revoie la liste de toutes les tuiles
    tiles = []
    for lines in game_grid:
        for tile in lines:
            if tile in [' ','  '] :
                tiles.append(0)
            else:
                tiles.append(tile)
    return tiles

def get_empty_tiles_positions(grid):        ## Donne la position des tuiles vides
    empty_tiles = []
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] in [0, ' ']:
                empty_tiles.append((i,j))
    return empty_tiles

def grid_get_value(grid, x, y):
    if grid[x][y] == ' ':
        return 0
    return grid[x][y]

def get_new_position(grid):         ## Choisit une coordonée aléatoire parmis les tuiles vide
    empty_tiles = get_empty_tiles_positions(grid)
    n = len(empty_tiles)
    if n > 0:
        k = rd.randint(0,n-1)
        return empty_tiles[k]

def grid_add_new_tile(game_grid):           ## Rajoute une tuile à la grille
    x,y = get_new_position(game_grid)
    game_grid = grid_add_new_tile_at_position(game_grid, x, y)
    return game_grid

def init_game(n = 4):
    game_grid = create_grid(n)
    game_grid= grid_add_new_tile(game_grid)
    game_grid= grid_add_new_tile(game_grid)
    return game_grid
