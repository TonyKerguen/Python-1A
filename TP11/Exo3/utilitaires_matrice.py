""" Fonctions utilitaires pour manipuler les matrices """

import API_matrice1 as matricee

def get_diagonale_principale(matrice):
    if matricee.get_nb_lignes(matrice) == matricee.get_nb_colonnes(matrice):
        res = []
        for elem in range(0, matricee.get_nb_lignes(matrice)):
            res.append(matricee.get_val(matrice, elem, elem))
        return res
    else:
        return None
    
def get_diagonale_secondaire(matrice):
    if matricee.get_nb_lignes(matrice) == matricee.get_nb_colonnes(matrice):
        res = []
        for elem in range(0,matrice[0]):
            res.append(matricee.get_val(matrice, elem, matrice[1]-elem-1))
        return res
    else:
        return None
    
def transpose(matrice):
    res = (matricee.get_nb_colonnes(matrice), matricee.get_nb_lignes(matrice), [])
    for colonne in range(0, matricee.get_nb_colonnes(matrice)):
        for elem in matricee.get_colonne(matrice, colonne):
            res[2].append(elem)
    return res

def is_triangulaire_inf(matrice):
    i = 1
    for l in range(0, matrice[0]):
        for elem in matricee.get_ligne(matrice, l)[i:]:
            i += 1
            if elem != 0:
                return False
    return True

def bloc(matrice, ligne, colonne, hauteur, largeur):
    res = (hauteur, largeur, [])
    if ligne + hauteur > matricee.get_nb_lignes(matrice) or colonne + largeur > matricee.get_nb_colonnes(matrice):
        return None
    else:
        for l in range(ligne, ligne + hauteur):
            for elem in matricee.get_ligne(matrice, l)[colonne:colonne+largeur]:
                res[2].append(elem)
        return res
