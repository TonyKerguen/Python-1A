""" Matrices : API n 1 """


def construit_matrice(nb_lignes, nb_colonnes, valeur_par_defaut):
    """crée une nouvelle matrice en mettant la valeur par défaut dans chacune de ses cases.

    Args:
        nb_lignes (int): le nombre de lignes de la matrice
        nb_colonnes (int): le nombre de colonnes de la matrice
        valeur_par_defaut : La valeur que prendra chacun des éléments de la matrice

    Returns:
        une nouvelle matrice qui contient la valeur par défaut dans chacune de ses cases
    """

    return (nb_lignes, nb_colonnes, [valeur_par_defaut]*(nb_lignes*nb_colonnes))


def get_nb_lignes(matrice):
    """permet de connaître le nombre de lignes d'une matrice

    Args:
        matrice : une matrice

    Returns:
        int : le nombre de lignes de la matrice
    """
    return matrice[0]


def get_nb_colonnes(matrice):
    """permet de connaître le nombre de colonnes d'une matrice

    Args:
        matrice : une matrice

    Returns:
        int : le nombre de colonnes de la matrice
    """
    return matrice[1]


def set_val(matrice, ligne, colonne, nouvelle_valeur):
    """permet de modifier la valeur de l'élément qui se trouve à la ligne et à la colonne
    spécifiées. Cet élément prend alors la valeur nouvelle_valeur

    Args:
        matrice : une matrice
        ligne (int) : le numéro d'une ligne (la numérotation commence à zéro)
        colonne (int) : le numéro d'une colonne (la numérotation commence à zéro)
        nouvelle_valeur : la nouvelle valeur que l'on veut mettre dans la case

    Returns:
        None
    """
    matrice[2][ligne*get_nb_colonnes(matrice)+colonne] = nouvelle_valeur

test = construit_matrice(2, 3, 5)
# print(test)
set_val(test, 1, 2, 8)
# print(test)


def get_val(matrice, ligne, colonne):
    """permet de connaître la valeur de l'élément de la matrice dont on connaît
    le numéro de ligne et le numéro de colonne.

    Args:
        matrice : une matrice
        ligne (int) : le numéro d'une ligne (la numérotation commence à zéro)
        colonne (int) : le numéro d'une colonne (la numérotation commence à zéro)

    Returns:
        la valeur qui est dans la case située à la ligne et la colonne spécifiées
    """
    return matrice[2][ligne*get_nb_colonnes(matrice)+colonne]


# Fonctions pour l'affichage 

def affiche_ligne_separatrice(matrice, taille_cellule=4):
    """fonction auxilliaire qui permet d'afficher (dans le terminal)
    une ligne séparatrice

    Args:
        matrice : une matrice
        taille_cellule (int, optional): la taille d'une cellule. Defaults to 4.
    """
    print()
    for _ in range(get_nb_colonnes(matrice) + 1):
        print('-'*taille_cellule+'+', end='')
    print()


def affiche(matrice, taille_cellule=4):
    """permet d'afficher une matrice dans le terminal

    Args:
        matrice : une matrice
        taille_cellule (int, optional): la taille d'une cellule. Defaults to 4.
    """
    nb_colonnes = get_nb_colonnes(matrice)
    nb_lignes = get_nb_lignes(matrice)
    print('\n'+' '*taille_cellule+'|', end='')
    for i in range(nb_colonnes):
        print(str(i).center(taille_cellule) + '|', end='')
    affiche_ligne_separatrice(matrice, taille_cellule)
    for i in range(nb_lignes):
        print(str(i).rjust(taille_cellule) + '|', end='')
        for j in range(nb_colonnes):
            print(str(get_val(matrice, i, j)).rjust(taille_cellule) + '|', end='')
        affiche_ligne_separatrice(matrice, taille_cellule)
    print()

# Ajouter ici les fonctions supplémentaires, sans oublier de compléter le fichier
# tests_API_matrice.py avec des fonctions de tests

def charge_matrice_str(nom_fichier = "./matricetest.csv"):
    """permet créer une matrice de str à partir d'un fichier CSV.

    Args:
        nom_fichier (str): le nom d'un fichier CSV (séparateur  ',')

    Returns:
        une matrice de str
    """
    fic = open(nom_fichier, 'r', encoding="utf-8")
    val = []
    nbligne = 0
    for lignefic in fic:
        nbligne += 1
        for elem in lignefic.split(","):
            if elem != "\n":
                val.append(elem)
    fic.close()
    res = (nbligne, len(lignefic.split(","))-1, val)
    return res

# print(charge_matrice_str())

def sauve_matrice(matrice, nom_fichier = "./matrice.csv"):
    """permet sauvegarder une matrice dans un fichier CSV.
    Attention, avec cette fonction, on perd l'information sur le type des éléments

    Args:
        matrice : une matrice
        nom_fichier (str): le nom du fichier CSV que l'on veut créer (écraser)

    Returns:
        None
    """
    fic = open(nom_fichier, 'w', encoding="utf-8")
    for elem in range(len(matrice[2])):
        if elem % matrice[1] == 0 and elem != 0:
            fic.write("\n"+str(matrice[2][elem])+",")
        else:
            fic.write(str(matrice[2][elem])+",")
    fic.write("\n")
    fic.close()

# sauve_matrice((3, 4, [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]),"./matricetest.csv")
# 10 11 12 13
# 14 15 16 17
# 18 19 20 21

def get_ligne(matrice, ligne):
    return matrice[2][matrice[1]*ligne:(matrice[1]*ligne)+matrice[1]]

def get_colonne(matrice, colonne):
    res = []
    i = colonne
    while i < len(matrice[2]):
        res.append(matrice[2][i])
        i += matrice[1]
    return res

def get_diagonale_principale(matrice):
    res = []
    if matrice[0] == matrice[1]:
        for elem in range(0,matrice[0]):
            res.append(get_val(matrice, elem, elem))
        return res
    else:
        return None
    
def get_diagonale_secondaire(matrice):
    res = []
    if matrice[0] == matrice[1]:
        for elem in range(0,matrice[0]):
            res.append(get_val(matrice, elem, matrice[1]-elem-1))
        return res
    else:
        return None
    
def transpose(matrice):
    res = (matrice[1], matrice[0], [])
    for colonne in range(0, matrice[1]):
        for elem in get_colonne(matrice, colonne):
            res[2].append(elem)
    return res

def is_triangulaire_inf(matrice):
    i = 1
    for l in range(0, matrice[0]):
        for elem in get_ligne(matrice, l)[i:]:
            i += 1
            if elem != 0:
                return False
    return True

def bloc(matrice, ligne, colonne, hauteur, largeur):
    res = (hauteur, largeur, [])
    if ligne + hauteur > matrice[0] or colonne + largeur > matrice[1]:
        return None
    else:
        for l in range(ligne, ligne+hauteur):
            for elem in get_ligne(matrice, l)[colonne:colonne+largeur]:
                res[2].append(elem)
    return res
