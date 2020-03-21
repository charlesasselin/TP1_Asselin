import argparse


def analyser_commande():
    parser = argparse.ArgumentParser(description='Jeu Quoridor - phase 1')
    parser.add_argument('idul', help='IDUL du joueur')
    parser.add_argument(
        '-l', '--lister', help='Lister les identifiants de vos 20 dernieres parties'
    )

    return parser.parse_args()


def afficher_damier_ascii(dico_etat_jeu):

    # ---------- ASCII START ---------

    print(f'Légende: 1={dico_etat_jeu["joueurs"][0]["nom"]}, 2=automate')
    print(' ----------------------------------- \n')

    # --------- OPTIONS ----------

    empty = ' . '
    empty_pair = '   '
    hori_corridor = '---'
    hori_corridor_pair = '-'
    vert_corridor = '|'

    # ---------- MODIFIER DICO ----------

    def transform_joueurs(dico_etat_jeu):
        list_joueurs = []
        for joueur in dico_etat_jeu['joueurs']:
            list_joueurs.append([(2*joueur['pos'][0])-1, (2*joueur['pos'][1])-1])
        return list_joueurs

    def transform_mur_vert(dico_etat_jeu):
        list_transformed_vert = []
        for mur_v in dico_etat_jeu['murs']['verticaux']:
            transformed_mur_v = [(2*mur_v[0])-1, (2*mur_v[1])-1]

            extend_wall_vert = []
            for i in range(3):
                extend_wall_vert.append([transformed_mur_v[0]-1, transformed_mur_v[1] + i])
            list_transformed_vert.extend(extend_wall_vert)

        return list_transformed_vert

    def transform_mur_hori(dico_etat_jeu):
        list_transformed_hori = []
        for mur_h in dico_etat_jeu['murs']['horizontaux']:
            transformed_mur_h = [(2*mur_h[0])-1, (2*mur_h[1])-1]
            extend_wall_hori = []
            for i in range(3):
                extend_wall_hori.append([transformed_mur_h[0] + i, transformed_mur_h[1]-1])
            list_transformed_hori.extend(extend_wall_hori)
        return list_transformed_hori

    # ---------- BOUCLES GRILLE ----------

    joueurs = transform_joueurs(dico_etat_jeu)
    murs_verticaux = transform_mur_vert(dico_etat_jeu)
    murs_horizontaux = transform_mur_hori(dico_etat_jeu)

    for line in range(17, 0, -1):
        if line % 2 != 0:
            print(str((line+1)//2) + ' |', end='')
        else:
            print('  |', end='')
        for col in range(1, 18):
            if [col, line] in joueurs:
                print(f' {joueurs.index([col, line])+1} ', end='')
            elif [col, line] in murs_verticaux:
                print(vert_corridor, end='')
            elif [col, line] in murs_horizontaux:
                if col % 2 == 0:
                    print(hori_corridor_pair, end='')
                else:
                    print(hori_corridor, end='')
            else:
                if line % 2 == 0:
                    if col % 2 != 0:
                        print(empty_pair, end='')
                    else:
                        print(' ', end='')
                else:

                    if col % 2 != 0:
                        print(empty, end='')
                    else:
                        print(' ', end='')
        print(' |')

    # ---------- ASCII END ----------
    print('--|------------------------------------- \n  | 1   2   3   4   5   6   7   8   9  ')
