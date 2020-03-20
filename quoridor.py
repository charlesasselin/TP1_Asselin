import argparse

def analyser_commande():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-h', '--help', help = 'show this message and exit'
    )

    parser.add_argument(
        '-l', '--lister', help= 'Lister les identifiants de vos 20 dernieres parties'
    )

    return parser.parse_args()

def afficher_damier_ascii(dico_etat_jeu):

    #---------- ASCII START ---------
    print(' ----------------------------------- \n')
    # --------- OPTIONS ----------

    name1 = ' 1 '
    name2 = ' 2 '
    empty = ' . '
    emptyPair = '   '
    horiCorridor = '---'
    horiCorridorPair = '-'
    vertCorridor = '|'

    #---------- MODIFIER DICO ----------

    def transformJoueurs(dico_etat_jeu):
        listJoueurs = []
        for joueur in dico_etat_jeu['joueurs']:
            listJoueurs.append([(2*joueur['pos'][0])-1, (2*joueur['pos'][1])-1])
        return listJoueurs

    def transformMurVert(dico_etat_jeu):
        listTransformedVert = []
        for murV in dico_etat_jeu['murs']['verticaux']:
            transformedMurV = [(2*murV[0])-1, (2*murV[1])-1]

            extendWallVert = []
            for i in range(3):
                extendWallVert.append([transformedMurV[0]-1, transformedMurV[1] + i])
            listTransformedVert.extend(extendWallVert)

        return listTransformedVert


    def transformMurHori(dico_etat_jeu):
        listTransformedHori = []
        for murH in dico_etat_jeu['murs']['horizontaux']:
            transformedMurH = [(2*murH[0])-1, (2*murH[1])-1]

            extendWallHori = []
            for i in range(3):
                extendWallHori.append([transformedMurH[0] + i, transformedMurH[1]-1])
            listTransformedHori.extend(extendWallHori)
        return listTransformedHori

    #---------- BOUCLES GRILLE ----------

    joueurs = transformJoueurs(dico_etat_jeu)
    mursVerticaux = transformMurVert(dico_etat_jeu)
    mursHorizontaux = transformMurHori(dico_etat_jeu)

    for line in range(17, 0, -1):
        if line % 2 != 0:
            print(str((line+1)//2) + ' |', end='')
        else:
            print('  |', end='')
        for col in range(1, 18):
            if [col, line] in joueurs:
                print(f' {joueurs.index([col, line])+1} ', end='')
            elif [col, line] in mursVerticaux:
                print(vertCorridor, end='')
            elif [col, line] in mursHorizontaux:
                if col % 2 == 0:
                    print(horiCorridorPair, end='')
                else:
                    print(horiCorridor, end='')
            else:
                if line % 2 == 0:
                    if col % 2 != 0:
                        print(emptyPair, end='')
                    else:
                        print(' ', end='')
                else:

                    if col % 2 != 0:
                        print(empty, end='')
                    else:
                        print(' ', end='')
        print(' |')

    #---------- ASCII END ----------
    print('--|------------------------------------- \n  | 1   2   3   4   5   6   7   8   9  ')

