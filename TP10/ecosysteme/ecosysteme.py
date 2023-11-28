"""
Init Dev : TP10
Exercice 2 : Ecosystème
"""

def extinction_immediate(ecosysteme, animal):
    """
    renvoie True si animal s'éteint immédiatement dans l'écosystème faute
    de nourriture
    """
    if ecosysteme[animal] is None:
        return False
    else:
        return ecosysteme[animal] not in ecosysteme.keys() and ecosysteme[animal] != None


def en_voie_disparition(ecosysteme, animal):
    """
    renvoie True si animal s'éteint est voué à disparaitre à long terme
    """
    i = 0
    while not extinction_immediate(ecosysteme, animal) and i < len(ecosysteme):
        animal = ecosysteme[animal]
        i += 1
        if animal is None:
            return False
    if extinction_immediate(ecosysteme, animal):
        return True
    else:
        return False

def animaux_en_danger(ecosysteme):
    """ renvoie l'ensemble des animaux qui sont en danger d'extinction immédiate"""
    res = set()
    for animal in ecosysteme.keys():
        if extinction_immediate(ecosysteme, animal):
            res.add(animal)
    return res

def especes_en_voie_disparition(ecosysteme):
    """ renvoie l'ensemble des animaux qui sont en voués à disparaitre à long terme
    """
    res = set()
    for animal in ecosysteme.keys():
        if en_voie_disparition(ecosysteme, animal):
            res.add(animal)
    return res

