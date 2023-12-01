""" Matrices : API n 1 """


def construit_matrice(nb_lignes, nb_colonnes, valeur_par_defaut = 0):
    """crée une nouvelle matrice en mettant la valeur par défaut dans chacune de ses cases.

    Args:
        nb_lignes (int): le nombre de lignes de la matrice
        nb_colonnes (int): le nombre de colonnes de la matrice
        valeur_par_defaut : La valeur que prendra chacun des éléments de la matrice

    Returns:
        une nouvelle matrice qui contient la valeur par défaut dans chacune de ses cases
    """
    res = []
    for _ in range(0, nb_lignes):
        ligne = []
        for _ in range(0, nb_colonnes):
            ligne.append(valeur_par_defaut)
        res.append(ligne)
    return res

def get_nb_lignes(matrice):
    """permet de connaître le nombre de lignes d'une matrice

    Args:
        matrice : une matrice

    Returns:
        int : le nombre de lignes de la matrice
    """
    return len(matrice)


def get_nb_colonnes(matrice):
    """permet de connaître le nombre de colonnes d'une matrice

    Args:
        matrice : une matrice

    Returns:
        int : le nombre de colonnes de la matrice
    """
    return len(matrice[0])


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
    matrice[ligne][colonne] = nouvelle_valeur


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
    return matrice[ligne][colonne]


def get_ligne(matrice, ligne):
    return matrice[ligne]

def get_colonne(matrice, colonne):
    res = []
    for ligne in matrice:
        res.append(ligne[colonne])
    return res

def get_diagonale_principale(matrice):
    if len(matrice) == len(matrice[0]):
        res = []
        i = 0
        while i < len(matrice):
            res.append(matrice[i][i])
            i += 1
        return res
    else:
        return None
    
def get_diagonale_secondaire(matrice):
    if len(matrice) == len(matrice[0]):
        res = []
        i = 0
        while i < len(matrice):
            res.append(matrice[i][len(matrice)-i-1])
            i += 1
        return res
    else:
        return None
    
def transpose(matrice):
    res = []
    for i in range(0, len(matrice[0])):
        res.append(get_colonne(matrice, i))
    return res

def is_triangulaire_inf(matrice):
    i = 1
    for l in range(0, len(matrice)):
        for elem in get_ligne(matrice, l)[i:]:
            i += 1
            if elem != 0:
                return False
    return True

def is_triangulaire_sup(matrice):
    i = 1
    for l in range(1, len(matrice)):
        for elem in get_ligne(matrice, l)[:i]:
            i += 1
            if elem != 0:
                return False
    return True

def bloc(matrice, ligne, colonne, hauteur, largeur):
    res = []
    if ligne + hauteur > len(matrice) or colonne + largeur > len(matrice[0]):
        return None
    else:
        for l in range(ligne, ligne + hauteur):
            res.append(get_ligne(matrice, l)[colonne:colonne+largeur])
        return res
    
def somme(matrice1, matrice2):
    if len(matrice1) == len(matrice2) and len(matrice1[0]) == len(matrice2[0]):
        res = construit_matrice(get_nb_lignes(matrice1), get_nb_colonnes(matrice2))
        for ligne in range(0, len(res)):
            for colonne in range(0, len(res[0])):
                set_val(res, ligne, colonne, get_val(matrice1, ligne, colonne)+get_val(matrice2, ligne, colonne))
        return res
    else:
        return None

def somme_des_elem_2_listes(liste1, liste2):
    res = 0
    i = 0
    while i < len(liste1):
        res += liste1[i]*liste2[i]
        i += 1
    return res



def produit(matrice1, matrice2):
    if len(matrice1[0]) == len(matrice2):
        res = construit_matrice(get_nb_lignes(matrice1), get_nb_colonnes(matrice2))
        for ligne in range(0, len(res)):
            for colonne in range(0, len(res[0])):
                set_val(res, ligne, colonne, somme_des_elem_2_listes(get_ligne(matrice1, ligne), get_colonne(matrice2, colonne)))
        return res
    else:
        return None