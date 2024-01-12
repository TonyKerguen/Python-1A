"""
Un pokedex est modélisé par une liste contenant des informations sur des pokemons.
Ces informations sont données sous la forme d'un tuple (nom, familles, attaque, défense, poids).
"""

def mon_pokedex():
    """ renvoie mon pokedex avec la structure de données
        donnée dans la documentaion du module """
    return [('Bulbizarre', {'Plante', 'Poison'}, 4, 3, 7),
            ('Jungko', {'Plante'}, 7, 1, 52),
            ('Herbizarre', {'Plante', 'Poison'}, 5, 5, 13),            
            ('Abo', {'Poison'}, 4, 2, 6)]

def get_poke(pokemon):
    return pokemon

def get_nom(pokemon):
    return pokemon[0]

def get_type(pokemon):
    return pokemon[1]

def get_attaque(pokemon):
    return pokemon[2]

def get_defense(pokemon):
    return pokemon[3]

def get_poids(pokemon):
    return pokemon[4]

def get_force(pokemon):
    return get_attaque(pokemon) + get_defense(pokemon)

def plus_forte_attaque(pokedex):
    return max(pokedex, key= get_attaque)

def tri_selon_defense(pokedex):
    res = []
    for poke in sorted(pokedex, key= get_defense):
        res.append(poke[0])
    return res


def plus_petite_force(pokedex):
    return min(pokedex, key= get_force)[0]


def tri_selon_diversite(pokedex):
    return sorted(sorted(pokedex, key= get_nom), key= get_type)