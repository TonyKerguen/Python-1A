""" TP7 une application complète
    ATTENTION VOUS DEVEZ METTRE DES DOCSTRING A TOUTES VOS FONCTIONS
"""
def afficher_menu(titre="met un titre bro ?", liste_options=["met au moins une option bro ?"]):
    print("+-"+"-"*len(titre)+"-+")
    print("| "+str(titre)+" |")
    print("+-"+"-"*len(titre)+"-+")
    for option in range(len(liste_options)):
        print(" "+str(option+1)+" -> "+liste_options[option])
    # print("Entrez votre choix [1-"+str(len(liste_options))+"]")

# afficher_menu()


def demander_nombre(message, borne_max):
    res = input(message)
    try:
        if 0 < int(res) <= borne_max+1:
            return int(res)
        return None
    except:
        return None

# print(demander_nombre("donne moi un nombre : ",10))


def menu(titre, liste_options):
    afficher_menu(titre, liste_options)
    return(demander_nombre("Entrez votre choix [1-"+str(len(liste_options))+"]("+str(len(liste_options)+1)+" pour quitter) : ",len(liste_options)))

# print(menu("MENU DE MON APPLICATION", ["Charger un fichier",
#                      "Rechercher la population d'une commune",
#                      "Afficher la population d'un département", 
#                      "Quitter"]))


def programme_principal():
    liste_options = ["Charger un fichier",
                     "Rechercher la population d'une commune",
                     "Afficher la population d'un département", 
                     "Quitter"]
    liste_communes = []
    while True:
        rep = menu("MENU DE MON APPLICATION", liste_options)
        if rep is None:
            print("Cette option n'existe pas")
        elif rep == 1:
            print("\nVous avez choisi", liste_options[rep - 1]+"\n")
            contenu_fic = charger_fichier_population("./"+input("Quel fichier charger ? "))
            print(contenu_fic)
        elif rep == 2:
            print("Vous avez choisi", liste_options[rep - 1])
        elif rep == 3:
            print("Vous avez choisi", liste_options[rep - 1])
        elif rep == len(liste_options)+1:
            break
        input("Appuyer sur Entrée pour continuer\n")
    print("Merci au revoir!")


def charger_fichier_population(nom_fic):
    res = []
    fic = open(nom_fic, 'r')
    fic.readline()
    for ligne in fic:
        l_champs = ligne.split(";")
        res.append((l_champs[0], l_champs[1], l_champs[4][:-1]))
    fic.close()
    return res

# print(charger_fichier_population("./extrait1.csv"))


def population_d_une_commune(liste_pop, nom_commune):
    ...

def liste_des_communes_commencant_par(liste_pop, debut_nom):
    ...

def commune_plus_peuplee_departement(liste_pop, num_dpt):
    ...

def nombre_de_communes_tranche_pop(liste_pop, pop_min, pop_max):
    ...

def place_top(commune, liste_pop):
    ...

def ajouter_trier(commune, liste_pop, taille_max):
    ...


def top_n_population(liste_pop, nbre):
    ...

def population_par_departement(liste_pop):
    ...

def sauve_population_dpt(nom_fic, liste_pop_dep):
    ...

# appel au programme principal
programme_principal()
