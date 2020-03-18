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

    def transformJoueurs():
        listJoueurs = []
        for joueur in dico_etat_jeu['joueurs']:
            listJoueurs.append([(2*joueur['pos'][0])-1, (2*joueur['pos'][1])-1])

    def transformMurVert():
       listTransformedVert = []
        for murV in dico_etat_jeu['murs']['verticaux']:
            transformedMurV = [(2*murV[0])-1, (2*murV[1])-1]

            extendWall = []
            for i in range(3):
                extendWall.append([transformedMurV[0]-1, transformedMurV[1] + i])
            listTransformedVert.extend(extendWall)



    #---------- BOUCLES GRILLE ----------

    for i in range(17, 1, -1):
        for j in range(1, 10):

    #il faudra iterer selon les valeurs du dictionnaire ici

    #---------- ASCII END ----------
    ligneX = '--|--------------------------------- \n'
    ligneXValues = '  | 1   2   3   4   5   6   7   8   9  '


