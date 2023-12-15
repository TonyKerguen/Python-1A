import random
import csv

def creer_matrice(ligne, colonne):
    """résumé :

    Args:
        ligne (type): 
        colonne (type): 

    Retourne:
        _type_: 
    """    
    matrice = []
    for i in range(ligne):
        ligne_matrice = []
        for j in range(colonne):
            ligne_matrice.append(random.randint(0, 100))
        matrice.append(ligne_matrice)
    return matrice

def get_valeur(matrice, ligne, colonne):
    """résumé :

    Args:
        matrice (type): 
        ligne (type): 
        colonne (type): 

    Retourne:
        _type_: 
    """    
    return matrice[ligne][colonne]

def set_valeur(matrice, ligne, colonne, valeur):
    """résumé :

    Args:
        matrice (type): 
        ligne (type): 
        colonne (type): 
        valeur (type): 
    """    
    matrice[ligne][colonne] = valeur

def get_nombre_de_colonnes(matrice):
    """résumé :

    Args:
        matrice (type): 

    Retourne:
        _type_: 
    """    
    return len(matrice[0]) if matrice else 0

def get_nombre_de_lignes(matrice):
    """résumé :

    Args:
        matrice (type): 

    Retourne:
        _type_: 
    """    
    return len(matrice)

def get_ligne(matrice, num_ligne):
    """_summary_

    Args:
        matrice (_type_): _description_
        num_ligne (_type_): _description_

    Returns:
        _type_: _description_
    """    
    return matrice[num_ligne]

def get_colonne(matrice, num_colonne):
    """_summary_

    Args:
        matrice (_type_): _description_
        num_colonne (_type_): _description_

    Returns:
        _type_: _description_
    """    
    res = []
    i = num_colonne
    while i < len(matrice[2]):
        res.append(matrice[2][i])
        i += matrice[1]
    return res

def enregistre_matrice(matrice, nom_fichier):
    """résumé :

    Args:
        matrice (type): 
        nom_fichier (type): 
    """    
    with open(nom_fichier, 'w', newline='') as fichier_csv:
        writer = csv.writer(fichier_csv)
        for ligne in matrice:
            writer.writerow(ligne)

def charge_matrice(nom_fichier):
    """résumé :

    Args:
        nom_fichier (type): 

    Retourne:
        _type_: 
    """    
    matrice_chargee = []
    with open(nom_fichier, 'r') as fichier_csv:
        reader = csv.reader(fichier_csv)
        for ligne in reader:
            ligne_entiers = []
            for valeur in ligne:
                ligne_entiers.append(int(valeur))
            matrice_chargee.append(ligne_entiers)
    return matrice_chargee

