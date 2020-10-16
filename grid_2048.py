
def create_grid(n = 4):
    game_grid = []
    for i in range(0,n):
        game_grid.append([0 for _ in range(n)])
    return game_grid

