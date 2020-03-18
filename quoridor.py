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

        posJoueur1 = dico_etat_jeu['joueurs'][0]['pos']
        listeJoueur1 = [(posJoueur1[0]*2)-1, (posJoueur1[1]*2)-1]

        posJoueur2 = dico_etat_jeu['joueurs'][1]['pos']
        listeJoueur2 = [(posJoueur1[0] * 2) - 1, (posJoueur1[1] * 2) - 1]

    def transformMurs():
        mursHorizontaux = dico_etat_jeu['murs'][0]['horizontaux']
        for murH in mursHorizontaux:



    #---------- BOUCLES GRILLE ----------

    for i in range(17, 1, -1):
        for j in range(1, 10):

    #il faudra iterer selon les valeurs du dictionnaire ici

    #---------- ASCII END ----------
    ligneX = '--|--------------------------------- \n'
    ligneXValues = '  | 1   2   3   4   5   6   7   8   9  '


