def intelligence_moyenne(heros):
    """renvoie la moyenne d'inteligence des héros

    Args:
        heros (dict): un dictionnaire de héros

    Returns:
        int: la moyenne d'inteligence des héros
    """    
    if len(heros) == 0:
        return 0
    res = 0
    for (_, intel, _) in heros.values():
        res += intel
    return res/len(heros)

def kikelplusfort(heros):
    """renvoie le nom du héros le plus fort

    Args:
        heros (dict): un dictionnaire de héros

    Returns:
        str: le nom du héros le plus fort
    """    
    res = None
    max_force = 0
    for (nom, (force, _, _)) in heros.items():
        if res == None or force > max_force:
            res = nom
            max_force = force
    return res

def combienDeCretins(heros):
    """renvoie le nombre de héros dont l'intelligence est inférieure à la moyenne

    Args:
        heros (dict): un dictionnaire de héros

    Returns:
        int: le nombre de héros dont l'intelligence est inférieure à la moyenne
    """    
    moyenne = intelligence_moyenne(heros)
    res = 0
    for (_, intel, _) in heros.values():
        if intel < moyenne:
            res += 1
    return res