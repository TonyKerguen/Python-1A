def get_bon_numero(tirage:str):
    res = []
    for num in tirage.split(":")[1].split("|")[0].split(" "):
        if num != "" and num not in res:
            res.append(num)
    return res

def get_liste_mes_numeros(tirage:str):
    mes_num = tirage.split(":")[1].split("|")[1]
    numero = mes_num.split(" ")
    res = []
    for num in numero:
        if num != "" and num not in res:
            res.append(num)
    return res

def get_nombre_numero_correct(tirage):
    res = 0
    for nombre in get_liste_mes_numeros(tirage):
        if nombre in get_bon_numero(tirage):
            res += 1
    return res

def calcul_nb_point(tirage):
    nb_bon_num = get_nombre_numero_correct(tirage)
    if nb_bon_num == 0:
        return 0
    else:
        return 2**(nb_bon_num-1)

def Scratchcards(fichier = "./input.txt"):
    fic = open(fichier, 'r', encoding="utf-8")
    res = 0
    for ligne in fic:
        print(get_nombre_numero_correct(ligne))
        res += calcul_nb_point(ligne[:-1])
    return res

print(Scratchcards("./test.txt"))

#################################################################################################

def get_numero_tirage(tirage:str):
    res = ""
    for carac in tirage.split(":")[0]:
        if carac.isnumeric():
            res += carac
    return res

def creation_dico(fichier):
    dico = dict()
    with open(fichier, 'r', encoding="utf-8") as fic:
        for ligne in fic:
            dico[int(get_numero_tirage(ligne))] = 1
    for tirage in dico
    print(dico)

# creation_dico("./input.txt")