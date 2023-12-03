def parties_possible(partie:str):
    champs = partie.split(":")
    for tirage in champs[1].split(";"):
        for cubes in tirage.split(","):
            # print(cubes[1:])
            nombre = ""
            for carac in cubes[1:]:
                if carac.isnumeric():
                    nombre += carac
            # print(nombre)
            chiffre = ""
            for carac in cubes[1:]:
                if carac.isalpha():
                    chiffre += carac
            # print(chiffre)
            if chiffre == "red" and int(nombre) > 12:
                return False
            if chiffre == "green" and int(nombre) > 13:
                return False
            if chiffre == "blue" and int(nombre) > 14:
                return False
    return True

def get_id_partie(partie:str):
    champs = partie.split(":")
    id = ""
    for carac in champs[0]:
        if carac.isnumeric():
            id += carac
    return int(id)

# print(get_id_partie("Game 16: 2 green, 4 red, 6 blue; 2 green, 16 blue, 2 red; 13 blue, 7 green, 3 red"))

# print(parties_impossible("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"))

def Cube_Conundrum(fichier = "./input.txt"):
    fic = open(fichier, 'r', encoding="utf-8")
    res = 0
    for ligne in fic:
        # print(parties_possible(ligne))
        if parties_possible(ligne):
            res += get_id_partie(ligne)
            # print(res)
    return res

print(Cube_Conundrum("./jeu.txt"))

#################################################################################################

def get_nb_cube_couleur(partie:str):
    champs = partie.split(":")
    red = 0
    green = 0
    blue = 0
    for tirage in champs[1].split(";"):
        for cubes in tirage.split(","):
            nombre = ""
            for carac in cubes[1:]:
                if carac.isnumeric():
                    nombre += carac
            # print(nombre)
            chiffre = ""
            for carac in cubes[1:]:
                if carac in "abcdefghijklmnopqrstuvwxyz":
                    chiffre += carac
            # print(chiffre)
            if chiffre == "red" and int(nombre) > red:
                red = int(nombre)
            if chiffre == "green" and int(nombre) > green:
                green = int(nombre)
            if chiffre == "blue" and int(nombre) > blue:
                blue = int(nombre)
    return red*green*blue

# print(get_nb_cube_couleur("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"))


def Cube_Conundrum2(fichier = "./input.txt"):
    fic = open(fichier, 'r', encoding="utf-8")
    res = 0
    for ligne in fic:
        res += get_nb_cube_couleur(ligne)
    return res

# print(Cube_Conundrum2())