""" TP7 une application complète
    ATTENTION VOUS DEVEZ METTRE DES DOCSTRING A TOUTES VOS FONCTIONS
"""

liste_test = [(18,"villedu18",5000),(18,"autrevilledu18",8000),(18,"encorevilledu18",5),(45,"villedu45",600)]


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
    return(demander_nombre("Entrez votre choix [1-"+str(len(liste_options))+"] : ",len(liste_options)))

# print(menu("MENU DE MON APPLICATION", ["Charger un fichier",
#                      "Rechercher la population d'une commune",
#                      "Afficher la population d'un département", 
#                      "Quitter"]))


def programme_principal():
    liste_options = ["Charger un fichier",
                     "Rechercher la population d'une commune",
                     "Afficher la population d'un département",
                     "Afficher les communes qui commencent par ...",
                     "Afficher la commune la plus peuplé d'un département",
                     "Afficher le nombre de communes qui ont un nombre d'habitant compris dans une tranche",
                     "Quitter"]
    liste_communes = []
    contenu_fic = None
    while True:
        rep = menu("MENU DE MON APPLICATION", liste_options)
        message_choix_option = str("\nVous avez choisi : "+liste_options[rep - 1])+"\n"
        if rep is None:
            print("Cette option n'existe pas")
        # Option 1
        elif rep == 1:
            print(message_choix_option)
            contenu_fic = charger_fichier_population("./"+input("Quel fichier charger ? "))
            print(str(len(contenu_fic))+" communes trouvées !")
        # Option 2
        elif rep == 2:
            if contenu_fic == None:
                print("Il faut charger un fichier avant !")
            else:
                print(message_choix_option)
                nb_hab = population_d_une_commune(contenu_fic, input("Nom de la commune ? "))
                if nb_hab == None:
                    print("Le nom de votre commune n'apparait pas dans le fichier chargé :(")
                else:
                    print(str(nb_hab))
        # Option 3
        elif rep == 3:
            if contenu_fic == None: 
                print("Il faut charger un fichier avant !")
            else:
                print(message_choix_option)
        # Option 4
        elif rep == 4:
            if contenu_fic == None:
                print("Il faut charger un fichier avant !")
            else:
                print(message_choix_option)
                print(liste_des_communes_commencant_par(contenu_fic, input("Par quoi doivent commencer le nom des communes ? ")))
        # Option 5
        elif rep == 5:
            if contenu_fic == None:
                print("Il faut charger un fichier avant !")
            else:
                print(message_choix_option)
                print(commune_plus_peuplee_departement(contenu_fic, input("De quel département voulez-vous la commune la plus peuplé ? ")))
        # Option 6
        elif rep == 6:
            if contenu_fic == None:
                print("Il faut charger un fichier avant !")
            else:
                print(message_choix_option)
                print(nombre_de_communes_tranche_pop(contenu_fic, int(input("Le nombre minimum d'habitant ? ")), int(input("Le nombre maximun d'habitant ? "))))
        
        # Option quitter
        elif rep == len(liste_options):
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
    for tuple in liste_pop:
        if tuple[1] == nom_commune:
            return tuple[0]
    return None

def liste_des_communes_commencant_par(liste_pop, debut_nom):
    res = []
    for tuple in liste_pop:
        # if tuple[1][:len(debut_nom)] == debut_nom:
        #     res.append(tuple[1])
        if str(tuple[1]).startswith(str(debut_nom)):
            res.append(tuple[1])
    return res

# print(liste_des_communes_commencant_par([(0,"testresf"),(0,"eeee"),(0,"tes"),(0,"te")],"tes"))


def commune_plus_peuplee_departement(liste_pop, num_dpt):
    res = "Ce departement n'apparait pas dans le fichier"
    pop_max = None
    for tuple in liste_pop:
        if str(tuple[0]).startswith(str(num_dpt)) and (pop_max == None or pop_max < int(tuple[2])):
            res = tuple[1]
            pop_max = int(tuple[2])
    return res


# print(commune_plus_peuplee_departement(liste_test, 66))


def nombre_de_communes_tranche_pop(liste_pop, pop_min, pop_max):
    res = 0
    for tuple in liste_pop:
        if pop_min <= int(tuple[2]) <= pop_max:
            res += 1
    return res

# print(nombre_de_communes_tranche_pop(liste_test, 0, 2))

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
