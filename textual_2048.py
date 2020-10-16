import ast


def read_player_command():
    move = input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")
    while move not in ['g', 'd', 'h', 'b']:
        move = input("Commande invalide. Entrez à nouveau une commande (g (gauche), d (droite), h (haut), b (bas))")
    return move

def read_size_grid():
    size = int(input("Choisissez la taille de la grille : "))
    while size < 1:
        size = int(input("Une taille strictement positive si possible : "))
    return size

def read_theme_grid():
    theme = ast.literal_eval(input("Choisissez un thème pour la grille : "))
    return theme

if __name__ == '__main__':
    game_play()
    exit(1)
