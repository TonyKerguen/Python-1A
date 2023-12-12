import API_matrice1 as matricee

def sm(matrice:list, ligne:int, colonne:int, hauteur:int, largeur:int):
    """renvoie la sous matrice de la matrice en fonction des paramètre donnés

    Args:
        matrice (list): une matrice
        ligne (int): la ligne à partir de laquelle on veut trouver la sous matrice
        colonne (int): la colonne à partir de laquelle on veut trouver la sous matrice
        hauteur (int): la hauteur de la sous matrice que l'on cherche
        largeur (int): la largeur de la sous matrice que l'on cherche

    Returns:
        list: la sous matrice de la matrice en fonction des paramètre donnés
    """    
    res = (hauteur, largeur, [])
    if ligne + hauteur > matricee.get_nb_lignes(matrice) or colonne + largeur > matricee.get_nb_colonnes(matrice):
        return None
    else:
        for l in range(ligne, ligne + hauteur):
            for elem in matricee.get_ligne(matrice, l)[colonne:colonne+largeur]:
                res[2].append(elem)
        return res
    
def colle_sous_matrice(matrice:list, sousmatrice:list, ligne:int, colonne:int):
    """colle une sousmatrice sur une autre matrice en fontion des paramètre donnés

    Args:
        matrice (list): une matrice
        sousmatrice (list): une sousmatrice
        ligne (int): la ligne à laquelle on veut coller la sousmatrice
        colonne (int): la colonne à laquelle on veut coller la sousmatrice

    Returns:
        list: la matrice fusionnée avec la sous matrice
    """    
    res = matrice.copy()
    for ligneSM in range(len(sousmatrice)):
        for colonneSM in range(len(sousmatrice[ligneSM])):
            matricee.set_val(res, ligne + ligneSM, colonne + colonneSM, sousmatrice[ligneSM][colonneSM])
    return res
