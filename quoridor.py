def afficher_damier_ascii(dico_etat_jeu):

    #---------- ASCII START ---------
    patron = ''
    ligneStart = ' ----------------------------------- \n'
    # --------- OPTIONS ----------

    name1 = ' 1 '
    name2 = ' 2 '
    empty = ' . '
    vertCorridor = '-------'
    horiCorridor = '| '

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
            for i in range(7):
                extendWallHori.append([transformedMurH[0] + i, transformedMurH[0]-1])
            listTransformedHori.extend(extendWallHori)
        return listTransformedHori
    #---------- BOUCLES GRILLE ----------

    joueurs = transformJoueurs(dico_etat_jeu)
    mursVerticaux = transformMurVert(dico_etat_jeu)
    mursHorizontaux = transformMurHori(dico_etat_jeu)
    for i in range(17, 1, -1):
        for j in range(1, 10):
            if [i, j] in joueurs:
                print(joueurs.index([i, j])+1)





    #il faudra iterer selon les valeurs du dictionnaire ici

    #---------- ASCII END ----------
    ligneX = '--|--------------------------------- \n'
    ligneXValues = '  | 1   2   3   4   5   6   7   8   9  '


