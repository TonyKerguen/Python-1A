# Exercice 1

def moyenne_positif_while(liste_nombe):
    somme = 0
    cpt = 0
    i = 0
    while i < len(liste_nombe):
        if liste_nombe[i] >= 0:
            somme += liste_nombe[i]
            cpt += 1
        i += 1
    if cpt == 0:
        return None
    else:
        return somme/cpt
    
# print(moyenne_positif_while([0,0,0,1]))
# print(moyenne_positif_while([-1]))

    
def est_triee_while(liste_pers):
    i = 1
    test = True
    while i < len(liste_pers) and test:
        if liste_pers[i][1] > liste_pers[i-1][1]:
            test = False
        i += 1
    return test

# print(est_triee_while([("a",1),("b",2)]))
# print(est_triee_while([("b",2),("a",1)]))


def est_palindrome_while(chaine):
    i = 0
    test = True
    while i < (len(chaine)//2) and test:
        if chaine[i] != chaine[len(chaine)-1-i]:
            test = False
        i += 1
    return test

# print(est_palindrome_while("laval"))
# print(est_palindrome_while("tony"))

# Exercice 2

def fusion_liste(liste1, liste2):
    ind1 = 0
    ind2 = 0
    res = []
    while ind1 < len(liste1) and ind2 < len(liste2):
        if liste1[ind1] == liste2[ind2]:
            ind1 += 1
        elif liste1[ind1][0] < liste2[ind2][0]:
            res.append(liste1[ind1])
            ind1 += 1
        else:
            res.append(liste2[ind2])
            ind2 += 1
    while ind1 == len(liste1) and ind2 < len(liste2):
        res.append(liste2[ind2])
        ind2 += 1
    while ind2 == len(liste2) and ind1 < len(liste1):
        res.append(liste1[ind1])
        ind1 += 1
    return res

# print(fusion_liste([(1,"",0),(3,"",0),(4,"",0),(5,"",0)],[(1,"",0),((2,"",0))]))

def recherche_prod(liste, ref):
    i = 0
    while i < len(liste):
        if liste[i][0] == ref:
            return liste[i]
        i += 1
    return None

# print(recherche_prod([(1,"",0),(2,"",0),(3,"",0),(4,"",0),(5,"",0)],4))


# Exercice 3

def nombre_entre_2_borne(inf, sup):
    message = "donne moi un chiffre entre "+str(inf)+" et "+str(sup)+"\n"
    res = input(message)
    while not (inf <= int(res) <= sup):
        res = input(message)
    return "bravo"

# print(nombre_entre_2_borne(1,5))


def donne_moi_pallindome():
    message = "donne moi un pallindrome\n"
    res = input(message)
    while not est_palindrome_while(res):
        res = input(message)
    return "bravo"

# print(donne_moi_pallindome())


# Exercice 4
import random

def juste_prix(min, sup):
    val = random.randint(min,sup)
    print("\033[1;31m"+str(val)+"\033[0m")
    message = "\033[1;35mdonne moi un chiffre entre "+str(min)+" et "+str(sup)+"\033[0m\n"
    reponse = input(message)
    while int(reponse) != val:
        if int(reponse) < val:
            print("\nle nombre recherché est plus grand !")
        else:
            print("\nle nombre recherché est plus petit !")
        reponse = input(message)
    return "\033[1;33mbravo\033[0m"

print(juste_prix(1,100))