from api import lister_parties, initialiser_partie, jouer_coup
from quoridor import afficher_damier_ascii, analyser_commande

if __name__ == "__main__":
    parsed_args = analyser_commande()
    game_idul = initialiser_partie(parsed_args.idul)
    game_state = game_idul['état']
    lister_parties(parsed_args.idul)
    game_completed = False

    while game_completed is False:
        afficher_damier_ascii(game_state)
        print('Types de coups disponibles: \n - D: Deplacement \n - MH: Mur Horizontal \n - MV: Mur Vertical \n\n')

        type_coup = input('Choisissez votre type de coup (D, MH ou MV)')
        print('Vous avez effectué le coup ' + type_coup)

        ligne = input("Definissez la ligne de votre coup")
        print('Vous avez entré la ligne ' + ligne)

        colonne = input('Definissez la colonne de votre coup')
        print('Vous avez entré la colonne ' + colonne)

        position = [ligne, colonne]
        id_partie = game_idul['id']
        jouer_coup(id_partie, type_coup, position)
