# Codé par Papy Force X, jeune padawan de l'informatique

def dialogue_mot_de_passe():
    """indique si son mot de passe est correct

    Returns:
        str: le mot de passe
    """    
    login = input("Entrez votre nom : ")
    mot_de_passe_correct = False
    while not mot_de_passe_correct :
        mot_de_passe = input("Entrez votre mot de passe : ")
        # je vérifie la longueur
        longueur_ok_check = longueur_ok(mot_de_passe)
        # je vérifie s'il y a un chiffre
        chiffre_ok_check = chiffre_ok(mot_de_passe)
        # je vérifie qu'il n'y a pas d'espace
        sans_espace_check = sans_espace(mot_de_passe)
        # je vérifie qu'il n'y a pas 2 chiffre consecutif
        sans_deux_chiffre_consecutif_check = sans_deux_chiffre_consecutif(mot_de_passe)
        # je vérifie que le plus petit chiffre apparait une seul fois
        plus_petit_chiffre_apparait_une_seul_fois_check = plus_petit_chiffre_apparait_une_seul_fois(mot_de_passe)
        # Je gère l'affichage
        if not longueur_ok_check:
            print("Votre mot de passe doit comporter au moins 8 caractères")
        elif not chiffre_ok_check:
            print("Votre mot de passe doit comporter au moins 3 chiffres")
        elif not sans_espace_check:
            print("Votre mot de passe ne doit pas comporter d'espace")
        elif not sans_deux_chiffre_consecutif_check:
            print("Votre mot de passe ne doit pas contenir 2 chiffre consecutif")
        elif not plus_petit_chiffre_apparait_une_seul_fois_check:
            print("Votre mot de passe ne doit pas contenir le plus petit chiffre plusieurs fois") 
        else:
            mot_de_passe_correct = True        
    print("Votre mot de passe est correct")
    return mot_de_passe


def longueur_ok(chaine):
    """verifie qu'une chaine fait plus de 8 caracteres

    Args:
        chaine (str): une chaine de caracteres

    Returns:
        bool: True si la longueur de la chaine fait plus de 8 caracteres, False sinon
    """    
    return len(chaine) >= 8


def chiffre_ok(chaine):
    """verifie qu'une chaine de caracteres contient au moins 3 chiffres

    Args:
        chaine (str): une chaine de caracteres

    Returns:
        bool: True si la chaine contient au moins 3 chiffres, False sinon
    """
    nb_chiffre = 0
    for lettre in chaine:
        if lettre.isdigit():
            nb_chiffre += 1
    return nb_chiffre >= 3

def sans_espace(chaine):
    """verifie qu'une chaine de caracteres ne contient pas d'espace

    Args:
        chaine (str): une chaine de caracteres

    Returns:
        bool: True si la chaine ne contient pas d'espace, False sinon
    """
    for lettre in chaine:
        if lettre == " ":
            return False
    return True

def sans_deux_chiffre_consecutif(chaine):
    """verifie qu'une chaine ne contient pas 2 chiffre consecutif

    Args:
        chaine (str): une chaine de caracteres

    Returns:
        bool: True si la chaine ne contient pas 2 chiffre consecutif, False sinon
    """    
    if len(chaine) > 1:
        for lettre in range(1, len(chaine)):
             if chaine[lettre].isdigit() and chaine[lettre-1].isdigit():
                  return False
        return True
    return False


def plus_petit_chiffre_apparait_une_seul_fois(chaine):
    """verifie qu'une chaine ne contient qu'une seul fois le plus petit chiffre

    Args:
        chaine (str): une chaine de caracteres

    Returns:
        bool: True si la chaine ne contient qu'une seul fois le plus petit chiffre, False sinon
    """    
    nb_apparition_plus_petit_nombre = 0
    plus_petit_nombre = None
    for lettre in chaine:
        if lettre.isdigit():
            if plus_petit_nombre == None:
                plus_petit_nombre = lettre
                nb_apparition_plus_petit_nombre = 1
            elif lettre < plus_petit_nombre:
                plus_petit_nombre = lettre
                nb_apparition_plus_petit_nombre = 1
            elif lettre == plus_petit_nombre:
                nb_apparition_plus_petit_nombre += 1
    return nb_apparition_plus_petit_nombre == 1

def charger_mdr(nom_fichier = "./mdpUltraSecret.txt"):
    fic = open(nom_fichier, 'r', encoding="utf-8")

# def sauver_mdp():



# dialogue_mot_de_passe()
