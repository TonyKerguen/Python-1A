"""Init Dev : TP10"""

# =====================================================================
# Exercice 1 : Choix de modélisation et complexité
# =====================================================================
# Modélisation n°1
# =====================================================================

# Penser à completer la fonction exemples_pokedex_v1 dans le fichier de tests

def appartient_v1(pokemon, pokedex):  #O(N)
    """ renvoie True si pokemon (str) est présent dans le pokedex """
    for nompokemon, _ in pokedex:
        if nompokemon == pokemon:
            return True
    return False


def toutes_les_attaques_v1(pokemon, pokedex): #O(N)
    """
    param: un pokedex et le nom d'un pokemon (str) qui appartient au pokedex
    resultat: renvoie l'ensemble des types d'attaque du pokemon passé en paramètre
    """
    res = set()
    for nompokemon, type in pokedex:
        if nompokemon == pokemon:
            res.add(type)
    return res


def nombre_de_v1(attaque, pokedex): #O(N)
    """
    param: un pokedex et un type d'attaque (str)
    resultat: renvoie le nombre de pokemons de ce type d'attaque
    dans le pokedex
    """
    res = 0
    for _, type in pokedex:
        if type == attaque:
            res += 1
    return res

def attaque_preferee_v1(pokedex):  #O(N)
    """
    Renvoie le nom du type d'attaque qui est la plus fréquente dans le pokedex
    """
    dicoattaque = dict()
    for _, type in pokedex:
        if type in dicoattaque.keys():
            dicoattaque[type] += 1
        else:
            dicoattaque[type] = 1
    nbmax = 0
    nomnbmax = None
    for nomattaque, nbattaque in dicoattaque.items():
        if nbattaque > nbmax:
            nomnbmax = nomattaque
            nbmax = nbattaque
    return nomnbmax

# =====================================================================
# Modélisation n°2
# =====================================================================

# Penser à completer la fonction exemples_pokedex_v2 dans le fichier de tests

def appartient_v2(pokemon, pokedex): #O(1)
    """ renvoie True si pokemon (str) est présent dans le pokedex """
    return pokemon in pokedex.keys()


def toutes_les_attaques_v2(pokemon, pokedex): #O(1)
    """
    param: un pokedex et le nom d'un pokemon (str) qui appartient au pokedex
    resultat: renvoie l'ensemble des types d'attaque du pokemon passé en paramètre
    """
    return pokedex[pokemon]


def nombre_de_v2(attaque, pokedex): #O(N)
    """
    param: un pokedex et un type d'attaque (str)
    resultat: renvoie le nombre de pokemons de ce type d'attaque
    dans le pokedex
    """
    res = 0
    for types in pokedex.values():
        if attaque in types:
            res += 1
    return res

def attaque_preferee_v2(pokedex): #O(N)
    """
    Renvoie le nom du type d'attaque qui est la plus fréquente dans le pokedex
    """
    dicoattaque = dict()
    for types in pokedex.values():
        for type in types:
            if type in dicoattaque.keys():
                dicoattaque[type] += 1
            else:
                dicoattaque[type] = 1
    nbmax = 0
    nomnbmax = None
    for nomattaque, nbattaque in dicoattaque.items():
        if nbattaque > nbmax:
            nomnbmax = nomattaque
            nbmax = nbattaque
    return nomnbmax

# =====================================================================
# Modélisation n°3
# =====================================================================

# Penser à completer la fonction exemples_pokedex_v3 dans le fichier de tests


def appartient_v3(pokemon, pokedex): #O(N)
    """ renvoie True si pokemon (str) est présent dans le pokedex """
    for nompokes in pokedex.values():
        if pokemon in nompokes:
            return True
    return False


def toutes_les_attaques_v3(pokemon, pokedex): #O(N)
    """
    param: un pokedex et le nom d'un pokemon (str) qui appartient au pokedex
    resultat: renvoie l'ensemble des types d'attaque du pokemon passé en paramètre
    """
    res = set()
    for attaque, nompoke in pokedex.items():
        if pokemon in nompoke:
            res.add(attaque)
    return res


def nombre_de_v3(attaque, pokedex): #O(1)
    """
    param: un pokedex et un type d'attaque (str)
    resultat: renvoie le nombre de pokemons de ce type d'attaque
    dans le pokedex
    """
    try:
        return len(pokedex[attaque])
    except:
        return 0

def attaque_preferee_v3(pokedex): #O(N)
    """
    Renvoie le nom du type d'attaque qui est la plus fréquente dans le pokedex
    """
    res = None
    nbmax = 0
    for type, poke in pokedex.items():
        if len(poke) > nbmax:
            nbmax = len(poke)
            res = type
    return res

# =====================================================================
# Transformations
# =====================================================================

# Version 1 ==> Version 2

def v1_to_v2(pokedex_v1):
    """
    param: prend en paramètre un pokedex version 1
    renvoie le même pokedex mais en version 2
    """
    res = dict()
    for nom, type in pokedex_v1:
        if nom in res.keys():
            res[nom].add(type)
        else:
            res[nom] = {type}
    return res


# Version 1 ==> Version 2

def v2_to_v3(pokedex_v2):
    """
    param: prend en paramètre un pokedex version2
    renvoie le même pokedex mais en version3
    """
    res = dict()
    for nom, types in pokedex_v2.items():
        for type in types:
            if type in res.keys():
                res[type].add(nom)
            else:
                res[type] = {nom}
    return res

