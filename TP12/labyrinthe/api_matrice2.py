import random
import csv

def creer_matrice(nombre_lignes, nombre_colonnes):
    """_summary_

    Args:
        nombre_lignes (_type_): _description_
        nombre_colonnes (_type_): _description_

    Returns:
        _type_: _description_
    """    
    matrice = [(nombre_lignes, nombre_colonnes), []]
    for _ in range(nombre_lignes * nombre_colonnes):
        matrice[1].append(random.randint(0, 100))
    return matrice

def get_valeur(matrice, ligne, colonne):
    """_summary_

    Args:
        matrice (_type_): _description_
        ligne (_type_): _description_
        colonne (_type_): _description_

    Returns:
        _type_: _description_
    """    
    nombre_colonnes = matrice[0][1]
    index = ligne * nombre_colonnes + colonne
    return matrice[1][index]

def set_valeur(matrice, ligne, colonne, valeur):
    """_summary_

    Args:
        matrice (_type_): _description_
        ligne (_type_): _description_
        colonne (_type_): _description_
        valeur (_type_): _description_
    """    
    nombre_colonnes = matrice[0][1]
    index = ligne * nombre_colonnes + colonne
    matrice[1][index] = valeur

def get_nombre_de_colonnes(matrice):
    """_summary_

    Args:
        matrice (_type_): _description_

    Returns:
        _type_: _description_
    """    
    return matrice[0][1]

def get_nombre_de_lignes(matrice):
    """_summary_

    Args:
        matrice (_type_): _description_

    Returns:
        _type_: _description_
    """    
    return matrice[0][0]

def get_ligne(matrice, num_ligne):
    """_summary_

    Args:
        matrice (_type_): _description_
        num_ligne (_type_): _description_

    Returns:
        _type_: _description_
    """    
    nombre_colonnes = matrice[0][1]
    debut = num_ligne * nombre_colonnes
    fin = debut + nombre_colonnes
    return matrice[1][debut:fin]

def get_colonne(matrice, num_colonne):
    """_summary_

    Args:
        matrice (_type_): _description_
        num_colonne (_type_): _description_

    Returns:
        _type_: _description_
    """    
    nombre_lignes, nombre_colonnes = matrice[0]
    colonne = []
    for i in range(nombre_lignes):
        index = i * nombre_colonnes + num_colonne
        colonne.append(matrice[1][index])
    return colonne

def enregistre_matrice(matrice, nom_fichier):
    """_summary_

    Args:
        matrice (_type_): _description_
        nom_fichier (_type_): _description_
    """    
    nombre_lignes, nombre_colonnes = matrice[0]
    with open(nom_fichier, 'w', newline='') as fichier_csv:
        writer = csv.writer(fichier_csv)
        for i in range(nombre_lignes):
            debut = i * nombre_colonnes
            fin = debut + nombre_colonnes
            writer.writerow(matrice[1][debut:fin])

def charge_matrice(nom_fichier):
    """_summary_

    Args:
        nom_fichier (_type_): _description_

    Returns:
        _type_: _description_
    """    
    matrice_chargee = []
    with open(nom_fichier, 'r') as fichier_csv:
        reader = csv.reader(fichier_csv)
        for ligne in reader:
            matrice_chargee.extend(map(int, ligne))
    nombre_lignes = len(matrice_chargee) // len(ligne)
    nombre_colonnes = len(ligne)
    return [(nombre_lignes, nombre_colonnes), matrice_chargee]
