"""Permet de jouer au jeu du labyrinthe"""
import os
import plateau
import getch
import matrice
import matrice_graphique

def affiche_menu1():
    """Affiche le premier menu en sortie standart"""
    print(' ===== MON SUPER JEU =====')
    print(' (J)ouer ?')
    print(' (A)utre labyrinthe ?')
    print(' (Q)uitter ?')

def affiche_menudif():
    print(' ===== MODE DE JEU =====')
    print(' (N)ormal ?')
    print(' (F)lash ?')
    print(' (E)xpert ?')


def affiche_menu2():
    """Affiche le deuxième menu (pour jouer) sur la sortie standart"""
    print(' ===== MON SUPER JEU =====')
    print('Choisissez une direction')
    print(plateau.NORD+":NORD\n "+
          plateau.EST+":EST\n "+
          plateau.SUD+":SUD\n "+
          plateau.OUEST+":OUEST\n")


def affiche_jeu(le_plateau, affichage_graphique=None):
    """Permet à l'utilisateur d'interagir avec le jeu
    Sur la sortie standart :
        - le terminal est clear
        - on affiche le deuxième menu
        - on affiche le plateau de jeu
    En mode graphique (si affiche_graphique n'est pas à None)
        - on met à jour l'affichage de la matrice dans une fenêtre pygame
    """
    # os.system('clear')
    affiche_menu2()
    matrice.affiche(le_plateau)
    if affichage_graphique is not None:
        affichage_graphique.affiche_matrice()


def saisie_un_seul_caractere():
    """
    Attend que l'utilisateur tape un caractère au clavier et
    renvoie ce caractère sans avoir besoin d'appuyer sur la touche Entrée
    """
    return getch.getch()


def lance_menu():
    """
    Permet à l'utilisateur d'interagir avec le premier menu :
    lancer le jeu ou quitter l'application
    """
    affiche_menu1()
    quitte = False
    while not quitte:
        caractere = saisie_un_seul_caractere()
        if caractere.upper() == 'Q':
            quitte = True
        elif caractere.upper() == 'J':
            affiche_menudif()
            caractere = saisie_un_seul_caractere()
            if caractere.upper() == 'N':
                joue()
            elif caractere.upper() == 'F':
                joue("F")
            elif caractere.upper() == 'E':
                joue("E")
            elif caractere.upper() == 'I':
                joue("I")


def affiche_message(message, affichage_graphique=None):
    """Affiche un message
    Sur la sortie standart :
        -  affiche le message sur la sortie standart
    En mode graphique (si affiche_graphique n'est pas à None)
        - affiche le message dans la fenêtre pygame
    """
    print(message)
    if affichage_graphique is not None:
        affichage_graphique.affiche_message(message)


def fin_du_jeu(gagne, affichage_graphique=None):
    """Gère les affichage en fin de partie"""
    if gagne:
        message = 'Bravo ! vous avez gagné !'
    else:
        message = 'Oh non ! Le fantome vous a attrapé !?'
    affiche_message(message, affichage_graphique)
    lance_menu()


def joue(mode = "N"):
    """Permet de lancer le jeu du labyrinthe et y jouer"""
    if mode == "I":
        mon_plateau = plateau.init("/home/iut45/Etudiants/o22205496/home_iut/INIT_PROG/Python-1A/TP12/labyrinthe/impossible.csv")
        print(mon_plateau)
        personnage = (4, 4)
        fantome1 =  (0, 0)
        fantome2 =  (2, 0)
        fantome3 =  (4, 0)
        fantome4 =  (6, 0)
        fantome5 =  (8, 0)
        fantome6 =  (0, 8)
        fantome7 =  (2, 8)
        fantome8 =  (4, 8)
        fantome9 =  (6, 8)
        fantome10 = (8, 8)
        fantome11 = (0, 2)
        fantome12 = (0, 4)
        fantome13 = (0, 6)
        fantome14 = (8, 2)
        fantome15 = (8, 4)
        fantome16 = (8, 6)
    else:
        if mode == "F" or mode == "N":
            mon_plateau = plateau.init()
            personnage = (0, 0)
            fantome1 = (matrice.get_nb_lignes(mon_plateau) - 1, matrice.get_nb_colonnes(mon_plateau) - 1)
            fantome2 = None
        if mode == "E":
            mon_plateau = plateau.init()
            personnage = (0, 0)
            fantome1 = (matrice.get_nb_lignes(mon_plateau) - 1, matrice.get_nb_colonnes(mon_plateau) - 1)
            fantome2 = (2, 7)
        fantome3 = None
        fantome4 = None
        fantome5 = None
        fantome6 = None
        fantome7 = None
        fantome8 = None
        fantome9 = None
        fantome10 = None
        fantome11 = None
        fantome12 = None
        fantome13 = None
        fantome14 = None
        fantome15 = None
        fantome16 = None
    sortie = (matrice.get_nb_lignes(mon_plateau) - 1, matrice.get_nb_colonnes(mon_plateau) - 1)
    print(mon_plateau)
    affichage_graphique = matrice_graphique.MatriceGraphique(mon_plateau)
    affiche_jeu(mon_plateau, affichage_graphique)
    quitte = False
    while not quitte:
        direction = saisie_un_seul_caractere()
        if mode == "N":
            personnage = plateau.deplace_personnage(mon_plateau, personnage, direction, mode)
            fantome1 = plateau.deplace_fantome(mon_plateau, fantome1, personnage)
        elif mode == "F":
            personnage = plateau.deplace_personnage(mon_plateau, personnage, direction, mode)
            fantome1 = plateau.deplace_fantome(mon_plateau, fantome1, personnage)
            fantome1 = plateau.deplace_fantome(mon_plateau, fantome1, personnage)
        elif mode == "E":
            personnage = plateau.deplace_personnage(mon_plateau, personnage, direction, mode)
            fantome1 = plateau.deplace_fantome(mon_plateau, fantome1, personnage)
            fantome2 = plateau.deplace_fantome(mon_plateau, fantome2, personnage)
        elif mode == "I":
            fantome1 = plateau.deplace_fantome(mon_plateau, fantome1, personnage)
            fantome2 = plateau.deplace_fantome(mon_plateau, fantome2, personnage)
            fantome3 = plateau.deplace_fantome(mon_plateau, fantome3, personnage)
            fantome4 = plateau.deplace_fantome(mon_plateau, fantome4, personnage)
            fantome5 = plateau.deplace_fantome(mon_plateau, fantome5, personnage)
            fantome6 = plateau.deplace_fantome(mon_plateau, fantome6, personnage)
            fantome7 = plateau.deplace_fantome(mon_plateau, fantome7, personnage)
            fantome8 = plateau.deplace_fantome(mon_plateau, fantome8, personnage)
            fantome9 = plateau.deplace_fantome(mon_plateau, fantome9, personnage)
            fantome10 = plateau.deplace_fantome(mon_plateau, fantome10, personnage)
            fantome11 = plateau.deplace_fantome(mon_plateau, fantome11, personnage)
            fantome12 = plateau.deplace_fantome(mon_plateau, fantome12, personnage)
            fantome13 = plateau.deplace_fantome(mon_plateau, fantome13, personnage)
            fantome14 = plateau.deplace_fantome(mon_plateau, fantome14, personnage)
            fantome15 = plateau.deplace_fantome(mon_plateau, fantome15, personnage)
            fantome16 = plateau.deplace_fantome(mon_plateau, fantome16, personnage)
            personnage = plateau.deplace_personnage(mon_plateau, personnage, direction, mode)
        affiche_jeu(mon_plateau, affichage_graphique)
        if mode == "I":
            if personnage == fantome1:
                matrice.set_val(mon_plateau, fantome1[0], fantome1[1], 0)
                fantome1 == None
            if personnage == fantome2:
                fantome2 == None
                matrice.set_val(mon_plateau, fantome1[0], fantome1[1], 0)
            if personnage == fantome3:
                fantome3 == None
                matrice.set_val(mon_plateau, fantome1[0], fantome1[1], 0)
            if personnage == fantome4:
                fantome4 == None
            if personnage == fantome5:
                fantome5 == None
            if personnage == fantome5:
                fantome6 == None
            if personnage == fantome7:
                fantome7 == None
            if personnage == fantome8:
                fantome8 == None
            if personnage == fantome9:
                fantome9 == None
            if personnage == fantome10:
                fantome10 == None
            if personnage == fantome11:
                fantome11 == None
            if personnage == fantome12:
                fantome12 == None
            if personnage == fantome13:
                fantome13 == None
            if personnage == fantome14:
                fantome14 == None
            if personnage == fantome15:
                fantome15 == None
            if personnage == fantome16:
                fantome16 == None
        elif personnage == fantome1 or personnage == fantome2:
            fin_du_jeu(False, affichage_graphique)
            quitte = True

        elif personnage == sortie:
            fin_du_jeu(True, affichage_graphique)
            quitte = True


lance_menu()
