
# Jeu du morpion

def init_grille():
    return [[None, None, None],[None, None, None],[None, None, None]]


def init_joueur():
    return "X"


def change(joueur):
    if joueur == 'X':
        new_joueur = 'O'
    if joueur == 'O':
        new_joueur = 'X'
    return new_joueur


def init_jeu(taille=3):
    ...

            

def ajoute_ligne(largeur, gauche, milieu, droite):
    """
    Petite fonction utilitaire pour ajouter des bordures à
    l'affichage des tableau2D
    """ 
    return "   "+gauche + ("───"+milieu)*(largeur-1) + ("───"+droite) +"\n"
    
def affiche(tableau2d):
    """
    Affiche un tableau2D à condition que :
        - le tableau est carré (largeur = hauteur)
        - le tableau ne contient que des chaines de caractères de longueur 0, 1 ou 2
        - le tableau2D est modélisé par une liste de listes
    """
    taille = len(tableau2d)

    affiche = "    "
    for colonne in range(taille):
        affiche+=" C"+str(colonne)+" "
    affiche+="\n"
    affiche += ajoute_ligne(taille, "┌","┬","┐")
    for ligne in range(taille):
        affiche+="L"+str(ligne) + " │"
        for colonne in range(taille):
            valeur = tableau2d[ligne][colonne]
            if valeur is None:
                valeur = " "
            if valeur == 'X':
                couleur=31
            else:
                couleur=34
            affiche+= ' \033[1;'+str(couleur)+"m"+ valeur + '\033[0m │'
        affiche+="\n"
        if ligne != taille-1:
            affiche+= ajoute_ligne(taille, "├","┼","┤")
        else:
            affiche+= ajoute_ligne(taille, "└","┴","┘")
    print("\n"+affiche)


def csv_to_liste(fichier):
    ...


def verification_des_lignes(joueur, grille):
    for i in range(len(grille)):
        if joueur == grille[i][0] == grille[i][1] == grille[i][2]:
            return True
    return False
    
def verification_des_colonnes(joueur, grille):
    for i in range(len(grille)):
        if joueur == grille[0][i] == grille[1][i] == grille[2][i]:
            return True
    return False

def verification_des_diagonales(joueur, grille):
    if joueur == grille[0][0] == grille[1][1] == grille[2][2] or joueur == grille[2][0] == grille[1][1] == grille[0][2]:
        return True
    return False

def gagne(joueur, grille):
    return verification_des_lignes(joueur, grille) or verification_des_colonnes(joueur, grille) or verification_des_diagonales(joueur, grille)

def joue(joueur, grille, ligne, colonne):
    """
    Le joueur joue à la position ligne/colonne.
    La fonction met le jeu à jour et envoie True si tout s'est bien passé
    False sinon
    """
    if grille[ligne][colonne] == None :
        grille[ligne][colonne] = joueur
        if grille[ligne][colonne] == joueur:
            return True
    return False

def jeu_est_fini(joueur):
    if joueur == "X":
        couleur=31
    else:
        couleur=34
    
    print("GG au joueur \033[1;"+str(couleur)+"m"+ joueur + "\033[0m !")

def get_ligne(joueur):
    reponse = None
    if joueur == 'X':
        couleur=31
    else:
        couleur=34
    while reponse == '' or reponse == None or int(reponse) < 0 or int(reponse) > len(init_grille())-1:
        reponse = input("=====================\nAu joueur \033[1;"+str(couleur)+"m"+joueur+"\033[0m de jouer\nQuelle ligne ? ")
    ligne = int(reponse)
    return ligne

def get_colonne(joueur):
    reponse = None
    if joueur == 'X':
        couleur=31
    else:
        couleur=34
    while reponse == '' or reponse == None or int(reponse) < 0 or int(reponse) > len(init_grille())-1:
        reponse = input("=====================\nAu joueur \033[1;"+str(couleur)+"m"+joueur+"\033[0m de jouer\nQuelle colonne ? ")
    colonne = int(reponse)
    return colonne

def grille_rempli(grille):
    for ligne in grille:
        for colonne in ligne:
            if colonne == None:
                return False
    return True

def lance_jeu():
    grille = init_grille()
    joueur = init_joueur()
    fin = False
    while not grille_rempli(grille) and not fin:

        affiche(grille)

        ligne=get_ligne(joueur)

        colonne=get_colonne(joueur)
        
        while not joue(joueur, grille, ligne, colonne):
            print("\n\033[1;31mCette case est deja remplie !\033[0m\n")
            ligne=get_ligne(joueur)

            colonne=get_colonne(joueur)

        joue(joueur, grille, ligne, colonne)

        if gagne(joueur, grille):
            affiche(grille)
            jeu_est_fini(joueur)
            fin = True
        joueur = change(joueur)
    if grille_rempli(grille) and not fin:
        affiche(grille)
        print("\nAucun joueur n'a gagné :(")

                    


def affiche_menu():
    fin = False
    while not fin:
        reponse = input("=====================\nJeu du morpion\nQuel est votre choix ?\n(J)ouer ou (Q)uitter ? ")
        if reponse == 'J':
            lance_jeu()
            fin = True
        elif reponse == 'Q':
            fin = True


affiche_menu()
