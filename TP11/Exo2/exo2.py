ATM={'Armand':'Beatrice','Beatrice':'Cesar','Cesar':'Dalida',
     'Dalida':'Cesar','Etienne':'Beatrice','Firmin':'Henri',
     'Gaston':'Beatrice','Henri':'Firmin'}

def trouver_couple_reciproque(dico_couple:dict):
    res = []
    for personne1, personne2 in dico_couple.items():
        if personne1 > personne2 and dico_couple[personne2] == personne1:
            res.append((personne1, personne2))
    return res

# print(trouver_couple_reciproque(ATM))

def soupirants(dico_couple:dict, nom:str):
    res = []
    for personne1, personne2 in dico_couple.items():
        if personne2 == nom:
            res.append(personne1)
    return res