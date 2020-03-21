from api import lister_parties, initialiser_partie, jouer_coup
from quoridor import afficher_damier_ascii, analyser_commande

dico_etat_jeu = {
    "joueurs": [
        {"nom": "idul", "murs": 7, "pos": [5, 5]},
        {"nom": "automate", "murs": 3, "pos": [8, 6]}
    ],
    "murs": {
        "horizontaux": [[4, 4], [2, 6], [3, 8], [5, 8], [7, 8]],
        "verticaux": [[6, 2], [4, 4], [2, 6], [7, 5], [7, 7]]
    }
}

if __name__ == "__main__":
    parsed_args = analyser_commande()
    initialiser_partie(parsed_args)
    lister_parties(parsed_args)
    game_completed = False

    while game_completed is False:
        # do game logic here