ATM={'Armand':'Beatrice','Beatrice':'Cesar','Cesar':'Dalida',
     'Dalida':'Cesar','Etienne':'Beatrice','Firmin':'Henri',
     'Gaston':'Beatrice','Henri':'Firmin', 'toto':'titi'}

def trouver_couple_reciproque(dico_couple:dict):
    """renvoie les couples dont l’amour est réciproque

    Args:
        dico_couple (dict): un dictionnaire dont les clés sont les membres de l’ATM, et la valeur associée à chaque clé est le nom de l’élu·e de son cœur

    Returns:
        set: les couples dont l’amour est réciproque
    """    
    res = set()
    for personne1, personne2 in dico_couple.items():
        if personne2 in dico_couple.keys():
            if personne1 > personne2 and dico_couple[personne2] == personne1:
                res.add((personne1, personne2))
    return res


def soupirants(dico_couple:dict, nom:str):
    """renvoie toutes les personnes qui sont amoureuses de la personne passer en paramètre

    Args:
        dico_couple (dict): un dictionnaire dont les clés sont les membres de l’ATM, et la valeur associée à chaque clé est le nom de l’élu·e de son cœur
        nom (str): le nom de la personne dont on cherche qui est amoureux

    Returns:
        set: toutes les personnes qui sont amoureuses de la personne passer en paramètre
    """    
    res = set()
    for personne1, personne2 in dico_couple.items():
        if personne2 == nom:
            res.add(personne1)
    return res