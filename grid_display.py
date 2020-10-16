from tiles import *

def grid_to_string(game_grid, n):
    string = ''
    for i in range(n):
        for j in range(n):
            string += ' ==='
        string += '\n'
        for j in range(n):
            string += '| '
            string += str(game_grid[i][j])
            string += ' '
        string += '|'
        string += '\n'
    for j in range(n):
        string += ' ==='
    string += '\n'

    return string

def long_value(game_grid):
    tiles = get_all_tiles(game_grid)
    return max([len(str(x)) for x in tiles])


def grid_to_string_with_size(game_grid, n):
    string = ''
    k = long_value(game_grid)
    for i in range(n):
        for j in range(n):
            string += ' ='
            string += '=' * k
            string += '='
        string += '\n'
        for j in range(n):
            string += '| '
            tile = str(game_grid[i][j])
            p = len(tile)
            string += ' ' * (k - p)
            string += tile
            string += ' '
        string += '|'
        string += '\n'
    for j in range(n):
        string += ' ='
        string += '=' * k
        string += '='
    string += '\n'

    return string


def long_value_with_theme(grid, theme):
    tiles = get_all_tiles(grid)
    return max([len(theme[x]) for x in tiles])

def grid_to_string_with_size_and_theme(game_grid, theme, n):
    string = ''
    k = long_value_with_theme(game_grid, theme)
    for i in range(n):

        string += '=' * (k + 1) * n
        string += '='
        string += '\n'
        for j in range(n):
            string += '|'
            if game_grid[i][j] == ' ':
                tile = theme[0]
            else:
                tile = theme[game_grid[i][j]]
            p = len(tile)
            string += tile
            string += ' ' * (k - p)
        string += '|'
        string += '\n'
    string += '=' * (k + 1) * n
    string += '='
    string += '\n'

    return string
