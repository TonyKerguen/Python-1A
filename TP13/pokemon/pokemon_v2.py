"""
Un pokedex est modélisé par un dictionnaire dont les clefs sont les noms des pokemons 
et les valeurs associée des informations sur des pokemons.
Ces informations sont données sous la forme d'un tuple (familles, attaque, défense, poids).
"""

def mon_pokedex():
    """ renvoie mon pokedex avec la structure de données
        donnée dans la documentaion du module """
    return {'Bulbizarre': ({'Plante', 'Poison'}, 4, 3, 7),
            'Jungko': ({'Plante'}, 7, 1, 52),
            'Herbizarre': ({'Plante', 'Poison'}, 5, 5, 13),            
            'Abo': ({'Poison'}, 4, 2, 6)}


def get_attaque(pokemon):
    return pokemon[1]


def get_defense(pokemon):
    return pokemon[2]

def get_force(pokemon):
    return get_attaque(pokemon) + get_defense(pokemon)

def plus_forte_attaque(pokedex):
    poke = sorted(pokedex, key= get_attaque)[-1]
    return (poke, pokedex[poke][0], pokedex[poke][1], pokedex[poke][2], pokedex[poke][3])


def tri_selon_defense(pokedex):
    def get_def(poke):
        return pokedex[poke][2]
    return sorted(pokedex, key= get_def)


def plus_petite_force(pokedex):
    return sorted(pokedex, key= get_force)[0]


# def tri_selon_diversite(pokedex):
#     def get_nom(poke):
#     sorted(sorted(pokedex, key= get_nom), key= get_type)

