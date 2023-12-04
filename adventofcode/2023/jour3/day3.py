sc_list = list('%#*$/-&+@=')

# def signe(fichier = "C:/Users/Tony/Desktop/Init_Prog/Python-1A/adventofcode/2023/jour3/input.txt"):
#     fic = open(fichier, 'r', encoding="utf-8")
#     res = ""
#     for ligne in fic:
#         for carac in ligne:
#             if carac != "." and not carac.isnumeric() and carac not in res:
#                 res += carac
#     return res

def premiere_ligne(ligne:str, lignebas:str):
    res = 0
    nombre = ""
    for carac in range(len(ligne)):
        if ligne[carac].isnumeric():
            nombre += ligne[carac]
        elif nombre != "":
            if carac-1-len(nombre) < 0:
                if ligne[carac] in sc_list or {True for i in lignebas[carac-len(nombre):carac+1] if i in sc_list}:
                    res += int(nombre)
            else:
                if ligne[carac] in sc_list or ligne[carac-1-len(nombre)] in sc_list or {True for i in lignebas[carac-1-len(nombre):carac+1] if i in sc_list}:
                    res += int(nombre)
            nombre = ""
    if nombre != "":
        if ligne[carac-len(nombre)] in sc_list or {True for i in lignebas[carac-len(nombre):carac+1] if i in sc_list}:
            res += int(nombre)
    return res

def ligne_milieu(lignehaut:str, lignemilieu:str, lignebas:str):
    res = 0
    nombre = ""
    for carac in range(len(lignemilieu)):
        if lignemilieu[carac].isnumeric():
            nombre += lignemilieu[carac]
        elif nombre != "":
            if carac-1-len(nombre) < 0:
                if lignemilieu[carac] in sc_list or {True for i in lignehaut[carac-len(nombre):carac+1] if i in sc_list} or {True for i in lignebas[carac-len(nombre):carac+1] if i in sc_list}:
                    res += int(nombre)
            else:
                if lignemilieu[carac] in sc_list or lignemilieu[carac-1-len(nombre)] in sc_list or {True for i in lignehaut[carac-1-len(nombre):carac+1] if i in sc_list} or {True for i in lignebas[carac-1-len(nombre):carac+1] if i in sc_list}:
                    res += int(nombre)
            nombre = ""
    if nombre != "":
        if lignemilieu[carac-len(nombre)] in sc_list or {True for i in lignehaut[carac-len(nombre):carac+1] if i in sc_list} or {True for i in lignebas[carac-len(nombre):carac+1] if i in sc_list}:
            res += int(nombre)
    return res

def derniere_ligne(ligne:str, lignehaut:str):
    res = 0
    nombre = ""
    for carac in range(len(ligne)):
        if ligne[carac].isnumeric():
            nombre += ligne[carac]
        elif nombre != "":
            if carac-1-len(nombre) < 0:
                if ligne[carac] in sc_list or {True for i in lignehaut[carac-len(nombre):carac+1] if i in sc_list}:
                    res += int(nombre)
            else:
                if ligne[carac] in sc_list or ligne[carac-1-len(nombre)] in sc_list or {True for i in lignehaut[carac-1-len(nombre):carac+1] if i in sc_list}:
                    res += int(nombre)
            nombre = ""
    if nombre != "":
        if ligne[carac-len(nombre)] in sc_list or {True for i in lignehaut[carac-len(nombre):carac+1] if i in sc_list}:
            res += int(nombre)
    return res

def charger_fic(fichier = "./input.txt"):
    fic = open(fichier, 'r', encoding="utf-8")
    res = []
    for ligne in fic:
        res.append(str(ligne[:-1]))
    return res

# print(charger_fic()[-1])

def Gear_Ratios(fichier = "./input.txt"):
    fic = charger_fic(fichier)
    res = premiere_ligne(fic[0], fic[1]) + derniere_ligne(fic[-1], fic[-2])
    for ligne in range(1, len(fic)-1):
        res += ligne_milieu(fic[ligne-1], fic[ligne], fic[ligne+1])
    return res

# print(Gear_Ratios())

#################################################################################################

def rechercheautouretoile(lignehaut:str, lignemilieu:str, lignebas:str, numligne):
    res = dict()
    nombre = ""
    for carac in range(1, len(lignemilieu)):
        if lignemilieu[carac] == "*":
            res[(numligne, carac)] = []
            # ... #
            # XO. #
            # ... #
            if lignemilieu[carac-1].isnumeric():
                i = 0
                while lignemilieu[carac-1-i].isnumeric() and carac-1-i >= 0:
                    nombre = lignemilieu[carac-1-i]+nombre
                    i += 1
                if nombre != "":
                        res[(numligne, carac)].append(nombre)
                nombre = ""
            # ... #
            # .OX #
            # ... #
            if lignemilieu[carac+1].isnumeric():
                i = 0
                while carac+1+i < len(lignemilieu) and lignemilieu[carac+1+i].isnumeric():
                    nombre = nombre+lignemilieu[carac+1+i]
                    i += 1
                if nombre != "":
                        res[(numligne, carac)].append(nombre)
                nombre = ""
            # X.. #
            # .O. #
            # ... #
            if lignehaut[carac-1].isnumeric() and lignehaut[carac] == ".":
                i = 0
                while lignehaut[carac-1-i].isnumeric() and carac-1-i >= 0:
                    nombre = lignehaut[carac-1-i]+nombre
                    i += 1
                if nombre != "":
                    res[(numligne, carac)].append(nombre)
                nombre = ""
            # XX. #
            # .O. #
            # ... #
            if lignehaut[carac-1].isnumeric() and lignehaut[carac].isnumeric() and lignehaut[carac+1] == ".":
                i = 0
                while lignehaut[carac-i].isnumeric() and carac-1-i >= 0:
                    nombre = lignehaut[carac-i] + nombre
                    i += 1
                if nombre != "":
                    res[(numligne, carac)].append(nombre)
                nombre = ""
            # XXX #
            # .O. #
            # ... #
            if lignehaut[carac-1].isnumeric() and lignehaut[carac].isnumeric() and lignehaut[carac+1].isnumeric():
                i = 0
                while lignehaut[carac-i].isnumeric() and carac-1-i >= 0:
                    nombre = lignehaut[carac-i] + nombre
                    i += 1
                i = 0
                nombre = nombre[:-1]
                while carac+i < len(lignehaut) and lignehaut[carac+i].isnumeric():
                    nombre = nombre + lignehaut[carac+i]
                    i += 1
                if nombre != "":
                    res[(numligne, carac)].append(nombre)
                nombre = ""
            # .XX #
            # .O. #
            # ... #
            if lignehaut[carac-1] == "." and lignehaut[carac].isnumeric() and lignehaut[carac+1].isnumeric():
                i = 0
                while carac+i < len(lignehaut) and lignehaut[carac+i].isnumeric():
                    nombre = nombre + lignehaut[carac+i]
                    i += 1
                if nombre != "":
                    res[(numligne, carac)].append(nombre)
                nombre = ""
            # .X. #
            # .O. #
            # ... #
            if lignehaut[carac-1] == "." and lignehaut[carac].isnumeric() and lignehaut[carac+1] == ".":
                nombre = lignehaut[carac]
                if nombre != "":
                    res[(numligne, carac)].append(nombre)
                nombre = ""
            # ..X #
            # .O. #
            # ... #
            if lignehaut[carac] == "." and lignehaut[carac+1].isnumeric():
                i = 0
                while carac+1+i < len(lignehaut) and lignehaut[carac+1+i].isnumeric():
                    nombre = nombre + lignehaut[carac+1+i]
                    i += 1
                if nombre != "":
                    res[(numligne, carac)].append(nombre)
                nombre = ""
            # ... #
            # .O. #
            # X.. #
            if lignebas[carac-1].isnumeric() and lignebas[carac] == ".":
                i = 0
                while lignebas[carac-1-i].isnumeric() and carac-1-i >= 0:
                    nombre = lignebas[carac-1-i]+nombre
                    i += 1
                if nombre != "":
                    res[(numligne, carac)].append(nombre)
                nombre = ""
            # ... #
            # .O. #
            # XX. #
            if lignebas[carac-1].isnumeric() and lignebas[carac].isnumeric() and lignebas[carac+1] == ".":
                i = 0
                while lignebas[carac-i].isnumeric() and carac-1-i >= 0:
                    nombre = lignebas[carac-i] + nombre
                    i += 1
                if nombre != "":
                    res[(numligne, carac)].append(nombre)
                nombre = ""
            # ... #
            # .O. #
            # XXX #
            if lignebas[carac-1].isnumeric() and lignebas[carac].isnumeric() and lignebas[carac+1].isnumeric():
                i = 0
                while lignebas[carac-i].isnumeric() and carac-1-i >= 0:
                    nombre = lignebas[carac-i] + nombre
                    i += 1
                i = 0
                nombre = nombre[:-1]
                while carac+i < len(lignebas) and lignebas[carac+i].isnumeric():
                    nombre = nombre + lignebas[carac+i]
                    i += 1
                if nombre != "":
                    res[(numligne, carac)].append(nombre)
                nombre = ""
            # ... #
            # .O. #
            # .X. #
            if lignebas[carac-1] == "." and lignebas[carac].isnumeric() and lignebas[carac+1] == ".":
                nombre = lignebas[carac]
                if nombre != "":
                    res[(numligne, carac)].append(nombre)
                nombre = ""
            # ... #
            # .O. #
            # .XX #
            if lignebas[carac-1] == "." and lignebas[carac].isnumeric() and lignebas[carac+1].isnumeric():
                i = 0
                while carac+i < len(lignebas) and lignebas[carac+i].isnumeric():
                    nombre = nombre + lignebas[carac+i]
                    i += 1
                if nombre != "":
                    res[(numligne, carac)].append(nombre)
                nombre = ""
            # ... #
            # .O. #
            # ..X #
            if lignebas[carac] == "." and lignebas[carac+1].isnumeric():
                i = 0
                while carac+1+i < len(lignebas) and lignebas[carac+1+i].isnumeric():
                    nombre = nombre + lignebas[carac+1+i]
                    i += 1
                if nombre != "":
                    res[(numligne, carac)].append(nombre)
                nombre = ""
    return res


print(rechercheautouretoile(".788...",
                            ".63*47.",
                            "...05..",
                            1))

def Gear_Ratios2(fichier = "./input.txt"):
    fic = charger_fic(fichier)
    res = dict()
    nombrefinal = 0
    for ligne in range(1, len(fic)-1):
        dictligne = rechercheautouretoile(fic[ligne-1], fic[ligne], fic[ligne+1], ligne)
        if dictligne != {}:
            res = res|dictligne
    for valeurs in res.values():
        if len(valeurs) > 1:
            nombrefinal += int(valeurs[0])*int(valeurs[1])
    return nombrefinal

# print(Gear_Ratios2("./test.txt"))
print(Gear_Ratios2())