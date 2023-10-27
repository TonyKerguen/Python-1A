import histoire2foot

# Ici vos fonctions dédiées aux interactions


def afficher_menu(titre="Met un titre !", liste_options=["Met au moins une option !"]):
    couleur = 31
    print("\033[1;"+str(couleur)+"m+-"+"-"*len(titre)+"-+")
    print("| "+str(titre)+" |")
    print("+-"+"-"*len(titre)+"-+\033[0m")
    couleur += 1
    for option in range(len(liste_options)):
        print(" \033[1;"+str(couleur)+"m"+str(option+1) +
              " -> "+str(liste_options[option]) + '\033[0m')
        couleur += 1
        if couleur == 36:
            couleur = 31

# afficher_menu()


def demander_nombre(message, borne_max):
    res = input(message)
    if res.isdecimal():
        if 0 < int(res) <= borne_max:
            return int(res)
    return None

# print(demander_nombre("donne moi un nombre : ",10))


def menu(titre, liste_options):
    afficher_menu(titre, liste_options)
    return (demander_nombre("\nEntrez votre choix [1-"+str(len(liste_options))+"] : ", len(liste_options)))

# print(menu("MENU DE MON APPLICATION", ["Charger un fichier",
#                      "Rechercher la population d'une commune",
#                      "Afficher la population d'un département",
#                      "Quitter"]))


# ici votre programme principal
def programme_principal():
    liste_options = ["Charger un fichier",  # 1
                     "Rechercher les matchs qui se sont déroulés dans une ville donnée",  # 2
                     "Afficher le nombre moyen de buts marqués par match pour une compétition donnée",  # 3
                     "Vérifier si la liste de matchs est bien trié",  # 4
                     "Fusionner deux fichiers qui contiennent des listes de matchs",  # 5
                     "Quel sont les statistiques d'une équipe donnée",  # 6
                     "Afficher la liste des matchs pour lesquels l'écart de buts entre le vainqueur et le perdant est le plus grand",  # 7
                     "Afficher la liste des équipes qui ont participé aux matchs de la liste",  # 8
                     "Afficher la date de la première victoire d'une equipe",  # 9
                     "Afficher le plus grand nombre de matchs consécutifs sans défaite pour une equipe donnée",  # 10
                     "Vérifier si une équipe donnée a obtenu plus de victoires que de défaites",  # 11
                     "Afficher la liste des matchs les plus spectaculaires",  # 12
                     "la liste des équipes de la liste qui ont le plus petit nombre de defaites",  # 13
                     "Quitter"]  # 14
    # liste_matchs = None
    liste_matchs = histoire2foot.charger_matchs("histoire1.csv")
    while True:
        rep = menu("MENU DE MON APPLICATION", liste_options)
        if rep is None:
            print("Cette option n'existe pas")
        else:
            message_choix_option = str(
                "\nVous avez choisi : "+liste_options[rep - 1])+"\n"
        print(message_choix_option)
        # Option 1
        if rep == 1:
            non_réussi = True
            while non_réussi:
                try:
                    liste_matchs = histoire2foot.charger_matchs(
                        "./"+input("Quel fichier charger ? \n"))
                    print(str(len(liste_matchs))+" matchs trouvées !")
                    non_réussi = False
                except:
                    quitter = input(
                        "Ce fichier n'a pas pu être trouver. Veux tu quitter ? (o pour quitter sinon entrée)\n")
                    if quitter == "o":
                        non_réussi = False
        # Option 2
        if rep == 2:
            if liste_matchs == None:
                print("Il faut charger un fichier avant !\n")
            else:
                non_réussi = True
                while non_réussi:
                    ville = input("Dans quelle ville veux tu rechercher ?\n")
                    matchs_ville = histoire2foot.matchs_ville(
                        liste_matchs, str(ville))
                    if matchs_ville == []:
                        print("Aucun match ne c'est déroulé dans cette ville\n")
                    elif matchs_ville != None:
                        print("Voici tout les matchs qui ce sont dérouler dans la ville de " +
                              str(ville)+" : "+str(matchs_ville))
                        non_réussi = False
        # Option 3
        if rep == 3:
            if liste_matchs == None:
                print("Il faut charger un fichier avant !\n")
            else:
                non_réussi = True
                while non_réussi:
                    ville = input(
                        "De quelle compétition veux tu le nombre de buts moyen ? ")
                    nb_moyen_buts = histoire2foot.nombre_moyen_buts(
                        liste_matchs, ville)
                    if matchs_ville != None:
                        print("Il y a eu une moyenne de " +
                              str(nb_moyen_buts)+" dans cette compétition")
                    else:
                        quitter = input(
                            "Ce nom de compétition n'a pas été trouvée. Veux tu quitter ? (o pour quitter sinon entrée)")
                        if quitter == "o":
                            non_réussi = False
        # Option 4
        if rep == 4:
            if liste_matchs == None:
                print("Il faut charger un fichier avant !\n")
            else:
                if histoire2foot.est_bien_trie(liste_matchs):
                    print("Ce fichier de liste de match est bien trié")
                else:
                    print("Ce fichier de liste de match n'est pas bien trié")
        # Option 5
        if rep == 5:
            non_réussi1 = True
            non_réussi2 = True
            non_réussi = True
            while (non_réussi1 or non_réussi2) and non_réussi:
                while non_réussi1 and non_réussi:
                    try:
                        fic1 = histoire2foot.charger_matchs(
                            "./"+input("Quel est le premier fichier que tu veux charger ? \n"))
                        print(str(len(fic1))+" matchs trouvées !")
                        non_réussi1 = False
                    except:
                        quitter = input(
                            "Ce fichier n'a pas pu être trouver. Veux tu quitter ? (o pour quitter sinon entrée)\n")
                        if quitter == "o":
                            non_réussi = False
                while non_réussi2 and non_réussi:
                    try:
                        fic2 = histoire2foot.charger_matchs(
                            "./"+input("Quel est le deuxieme fichier que tu veux charger ? \n"))
                        print(str(len(fic2))+" matchs trouvées !")
                        non_réussi2 = False
                    except:
                        quitter = input(
                            "Ce fichier n'a pas pu être trouver. Veux tu quitter ? (o pour quitter sinon entrée)\n")
                        if quitter == "o":
                            non_réussi = False
            if non_réussi:
                fusion = histoire2foot.fusionner_matchs(fic1, fic2)
                histoire2foot.sauver_matchs(fusion, "fusion.csv")
                print(
                    "\nLe résultat de la fusion se trouve maintenant dans le fichier fusion.csv\n")
        # Option 6
        if rep == 6:
            if liste_matchs == None:
                print("Il faut charger un fichier avant !\n")
            else:
                stats = histoire2foot.resultats_equipe(liste_matchs, input(
                    "De quelle équipe veux tu les statistiques ?"))
                if stats == (0, 0, 0):
                    print("Cette équipe n'a jamais joué")
                else:
                    print("Cette équipe a joué "+str(stats[0]+stats[1]+stats[2])+" matchs dont : "+str(
                        stats[0])+" victoires, "+str(stats[1])+" nuls et "+str(stats[2])+" défaites")
        # Option 7
        if rep == 7:
            if liste_matchs == None:
                print("Il faut charger un fichier avant !\n")
            else:
                match_max_ecart = histoire2foot.plus_gros_scores(liste_matchs)
                if match_max_ecart == []:
                    print("il y a eu aucun match dans le fichier que tu m'as donné")
                else:
                    print(
                        "Voici la liste des match avec le plus grand écart de buts entre  vainqueur et perdant : "+str(match_max_ecart))
        # Option 8
        if rep == 8:
            if liste_matchs == None:
                print("Il faut charger un fichier avant !\n")
            else:
                liste_equipes = histoire2foot.liste_des_equipes(liste_matchs)
                if liste_equipes == []:
                    print("il y a eu aucun match dans le fichier que tu m'as donné")
                else:
                    print(
                        "Voici la liste de toutes les équipe qui ont particper à des matchs : "+str(liste_equipes))
        # Option quitter
        elif rep == len(liste_options):
            break
        input("Appuyer sur Entrée pour continuer\n")
    print("Merci au revoir!")


programme_principal()
# print(histoire2foot.resultats_equipe(histoire2foot.charger_matchs("histoire1.csv"),"ff"))
