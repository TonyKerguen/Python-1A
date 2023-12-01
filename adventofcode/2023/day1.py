chiffre_en_lettre = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def remplace_lettre_en_chiffre(chaine:str):
    for chiffre in range(0, len(chiffre_en_lettre)):
        while chiffre_en_lettre[chiffre] in chaine:
            chaine = chaine.replace(str(chiffre_en_lettre[chiffre]),str(chiffre_en_lettre[chiffre][0])+str(int(chiffre)+1)+str(chiffre_en_lettre[chiffre][-1]))
    return chaine

def Trebuchet(fichier = "./input.txt"):
    fic = open(fichier, 'r', encoding="utf-8")
    res = 0
    for ligne in fic:
        lignemodif = remplace_lettre_en_chiffre(ligne)
        premier_chiffre = 0
        dernier_chiffre = 0
        for carac in lignemodif:
            if carac.isnumeric(): 
                if premier_chiffre == 0:
                    premier_chiffre = carac
                    dernier_chiffre = carac
                if premier_chiffre != 0:
                    dernier_chiffre = carac
        res += int(premier_chiffre)*10 + int(dernier_chiffre)
    return res

print(Trebuchet())
