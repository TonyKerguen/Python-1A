# TP8 B - Manipuler des listes, ensembles et dictionnaires


def total_animaux(troupeau):
    """ Calcule le nombre total d'animaux dans un troupeau

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        int: le nombre total d'animaux dans le troupeau
    """
    res = 0
    for nb_animaux in troupeau.values():
        res += nb_animaux
    return res

def tous_les_animaux(troupeau):
    """ Détermine l'ensemble des animaux dans un troupeau

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        set: l'ensemble des animaux du troupeau
    """
    res = set()
    for animaux in troupeau.keys():
        res.add(animaux)
    return res


def specialise(troupeau):
    """ Vérifie si le troupeau contient 30 individus ou plus d'un même type d'animal 

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        bool: True si le troupeau contient 30 (ou plus) individus d'un même type d'animal,
        False sinon 
    """
    for nb_animaux in troupeau.values():
        if nb_animaux >= 30:
            return True
    return False


def le_plus_represente(troupeau):
    """ Recherche le nom de l'animal qui a le plus d'individus dans le troupeau
    
    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        str: le nom de l'animal qui a le plus d'individus  dans le troupeau
        None si le troupeau est vide) 
    
    """
    res = None
    nb_max = 0
    for (animaux, nb_animaux) in troupeau.items():
        if res == None or nb_animaux > nb_max:
            nb_max = nb_animaux
            res = animaux
    return res


def quantite_suffisante(troupeau):
    """ Vérifie si le troupeau contient au moins 5 individus de chaque type d'animal

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        bool: True si le troupeau contient au moins 5 individus de chaque type d'animal
        False sinon    
    """
    for nb_animaux in troupeau.values():
        if nb_animaux < 5:
            return False
    return True


def reunion_troupeaux(troupeau1, troupeau2):
    """ Simule la réunion de deux troupeaux

    Args:
        troupeau1 (dict): un dictionnaire modélisant un premier troupeau {nom_animaux: nombre}
        troupeau2 (dict): un dictionnaire modélisant un deuxième troupeau        

    Returns:
        dict: le dictionnaire modélisant la réunion des deux troupeaux    
    """
    res = dict()
    for (animaux, nb_animaux) in troupeau1.items():
        if animaux in res:
            res[animaux] += nb_animaux
        else:
            res[animaux] = nb_animaux
    for (animaux, nb_animaux) in troupeau2.items():
        if animaux in res:
            res[animaux] += nb_animaux
        else:
            res[animaux] = nb_animaux
    return res
