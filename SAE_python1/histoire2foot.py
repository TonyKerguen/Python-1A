"""Fichier source de la SAE 1.01 partie 1
    Historique des matchs de football internationaux
    """

# ---------------------------------------------------------------------------------------------
# Exemples de données pour vous aider à faire des tests
# ---------------------------------------------------------------------------------------------

# exemples de matchs de foot
match1 = ('2021-06-28', 'France', 'Switzerland', 3,
          3, 'UEFAEuro', 'Bucharest', 'Romania', True)
match2 = ('1998-07-12', 'France', 'Brazil', 3, 0,
          'FIFA World Cup', 'Saint-Denis', 'France', False)
match3 = ('1978-04-05', 'Germany', 'Brazil', 0, 1,
          'Friendly', 'Hamburg', 'Germany', False)


# exemples de listes de matchs de foot
liste1 = [('1970-04-08', 'France', 'Bulgaria', 1, 1,
           'Friendly', 'Rouen', 'France', False),
          ('1970-04-28', 'France', 'Romania', 2, 0,
           'Friendly', 'Reims', 'France', False),
          ('1970-09-05', 'France', 'Czechoslovakia',
           3, 0, 'Friendly', 'Nice', 'France', False),
          ('1970-11-11', 'France', 'Norway', 3, 1,
           'UEFA Euro qualification', 'Lyon', 'France', False)
          ]


liste2 = [('1901-03-09', 'England', 'Northern Ireland', 3, 0,
           'British Championship', 'Southampton', 'England', False),
          ('1901-03-18', 'England', 'Wales', 6, 0,
           'British Championship', 'Newcastle', 'England', False),
          ('1901-03-30', 'England', 'Scotland', 2, 2,
           'British Championship', 'London', 'England', False),
          ('1902-05-03', 'England', 'Scotland', 2, 2,
           'British Championship', 'Birmingham', 'England', False),
          ('1903-02-14', 'England', 'Northern Ireland', 4, 0,
           'British Championship', 'Wolverhampton', 'England', False),
          ('1903-03-02', 'England', 'Wales', 2, 1,
           'British Championship', 'Portsmouth', 'England', False),
          ('1903-04-04', 'England', 'Scotland', 1, 2,
           'British Championship', 'Sheffield', 'England', False),
          ('1905-02-25', 'England', 'Northern Ireland', 1, 1,
           'British Championship', 'Middlesbrough', 'England', False),
          ('1905-03-27', 'England', 'Wales', 3, 1,
           'British Championship', 'Liverpool', 'England', False),
          ('1905-04-01', 'England', 'Scotland', 1, 0,
           'British Championship', 'London', 'England', False),
          ('1907-02-16', 'England', 'Northern Ireland', 1, 0,
           'British Championship', 'Liverpool', 'England', False),
          ('1907-03-18', 'England', 'Wales', 1, 1,
           'British Championship', 'London', 'England', False),
          ('1907-04-06', 'England', 'Scotland', 1, 1,
           'British Championship', 'Newcastle', 'England', False),
          ('1909-02-13', 'England', 'Northern Ireland', 4, 0,
           'British Championship', 'Bradford', 'England', False),
          ('1909-03-15', 'England', 'Wales', 2, 0,
           'British Championship', 'Nottingham', 'England', False),
          ('1909-04-03', 'England', 'Scotland', 2, 0,
           'British Championship', 'London', 'England', False)
          ]
liste3 = [('1901-03-30', 'Belgium', 'France', 1, 2,
           'Friendly', 'Bruxelles', 'Belgium', False),
          ('1901-03-30', 'England', 'Scotland', 2, 2,
           'British Championship', 'London', 'England', False),
          ('1903-04-04', 'Brazil', 'Argentina', 3, 0,
           'Friendly', 'Sao Paulo', 'Brazil', False),
          ('1903-04-04', 'England', 'Scotland', 1, 2,
           'British Championship', 'Sheffield', 'England', False),
          ('1970-09-05', 'France', 'Czechoslovakia',
           3, 0, 'Friendly', 'Nice', 'France', False),
          ('1970-11-11', 'France', 'Norway', 3, 1,
           'UEFA Euro qualification', 'Lyon', 'France', False)
          ]
liste4 = [('1978-03-19', 'Argentina', 'Peru', 2, 1,
           'Copa Ramón Castilla', 'Buenos Aires', 'Argentina', False),
          ('1978-03-29', 'Argentina', 'Bulgaria', 3, 1,
           'Friendly', 'Buenos Aires', 'Argentina', False),
          ('1978-04-05', 'Argentina', 'Romania', 2, 0,
           'Friendly', 'Buenos Aires', 'Argentina', False),
          ('1978-05-03', 'Argentina', 'Uruguay', 3, 0,
           'Friendly', 'Buenos Aires', 'Argentina', False),
          ('1978-06-01', 'Germany', 'Poland', 0, 0,
           'FIFA World Cup', 'Buenos Aires', 'Argentina', True),
          ('1978-06-02', 'Argentina', 'Hungary', 2, 1,
           'FIFA World Cup', 'Buenos Aires', 'Argentina', False),
          ('1978-06-02', 'France', 'Italy', 1, 2,
           'FIFA World Cup', 'Mar del Plata', 'Argentina', True),
          ('1978-06-02', 'Mexico', 'Tunisia', 1, 3,
           'FIFA World Cup', 'Rosario', 'Argentina', True),
          ('1978-06-03', 'Austria', 'Spain', 2, 1,
           'FIFA World Cup', 'Buenos Aires', 'Argentina', True),
          ('1978-06-03', 'Brazil', 'Sweden', 1, 1,
           'FIFA World Cup', 'Mar del Plata', 'Argentina', True),
          ('1978-06-03', 'Iran', 'Netherlands', 0, 3,
           'FIFA World Cup', 'Mendoza', 'Argentina', True),
          ('1978-06-03', 'Peru', 'Scotland', 3, 1,
           'FIFA World Cup', 'Córdoba', 'Argentina', True),
          ('1978-06-06', 'Argentina', 'France', 2, 1,
           'FIFA World Cup', 'Buenos Aires', 'Argentina', False),
          ('1978-06-06', 'Germany', 'Mexico', 6, 0,
           'FIFA World Cup', 'Córdoba', 'Argentina', True),
          ('1978-06-06', 'Hungary', 'Italy', 1, 3,
           'FIFA World Cup', 'Mar del Plata', 'Argentina', True),
          ('1978-06-06', 'Poland', 'Tunisia', 1, 0,
           'FIFA World Cup', 'Rosario', 'Argentina', True),
          ('1978-06-07', 'Austria', 'Sweden', 1, 0,
           'FIFA World Cup', 'Buenos Aires', 'Argentina', True),
          ('1978-06-07', 'Brazil', 'Spain', 0, 0,
           'FIFA World Cup', 'Mar del Plata', 'Argentina', True),
          ('1978-06-07', 'Iran', 'Scotland', 1, 1,
           'FIFA World Cup', 'Córdoba', 'Argentina', True),
          ('1978-06-07', 'Netherlands', 'Peru', 0, 0,
           'FIFA World Cup', 'Mendoza', 'Argentina', True),
          ('1978-06-10', 'Argentina', 'Italy', 0, 1,
           'FIFA World Cup', 'Buenos Aires', 'Argentina', False),
          ('1978-06-10', 'France', 'Hungary', 3, 1,
           'FIFA World Cup', 'Mar del Plata', 'Argentina', True),
          ('1978-06-10', 'Germany', 'Poland', 1, 3,
           'FIFA World Cup', 'Rosario', 'Argentina', True),
          ('1978-06-11', 'Austria', 'Brazil', 0, 1,
           'FIFA World Cup', 'Mar del Plata', 'Argentina', True),
          ('1978-06-11', 'Iran', 'Peru', 1, 4,
           'FIFA World Cup', 'Córdoba', 'Argentina', True),
          ('1978-06-11', 'Netherlands', 'Scotland', 2, 3,
           'FIFA World Cup', 'Mendoza', 'Argentina', True),
          ('1978-06-11', 'Spain', 'Sweden', 1, 0,
           'FIFA World Cup', 'Buenos Aires', 'Argentina', True),
          ('1978-06-14', 'Argentina', 'Poland', 2, 0,
           'FIFA World Cup', 'Rosario', 'Argentina', False),
          ('1978-06-14', 'Austria', 'Netherlands', 1, 5,
           'FIFA World Cup', 'Córdoba', 'Argentina', True),
          ('1978-06-14', 'Brazil', 'Peru', 3, 0,
           'FIFA World Cup', 'Mendoza', 'Argentina', True),
          ('1978-06-14', 'Germany', 'Italy', 0, 0,
           'FIFA World Cup', 'Buenos Aires', 'Argentina', True),
          ('1978-06-18', 'Argentina', 'Brazil', 0, 0,
           'FIFA World Cup', 'Rosario', 'Argentina', False),
          ('1978-06-18', 'Austria', 'Italy', 0, 1,
           'FIFA World Cup', 'Buenos Aires', 'Argentina', True),
          ('1978-06-18', 'Germany', 'Netherlands', 2, 2,
           'FIFA World Cup', 'Córdoba', 'Argentina', True),
          ('1978-06-18', 'Peru', 'Poland', 0, 1,
           'FIFA World Cup', 'Mendoza', 'Argentina', True),
          ('1978-06-21', 'Argentina', 'Peru', 6, 0,
           'FIFA World Cup', 'Rosario', 'Argentina', False),
          ('1978-06-21', 'Austria', 'Germany', 3, 2,
           'FIFA World Cup', 'Córdoba', 'Argentina', True),
          ('1978-06-21', 'Brazil', 'Poland', 3, 1,
           'FIFA World Cup', 'Mendoza', 'Argentina', True),
          ('1978-06-21', 'Italy', 'Netherlands', 1, 2,
           'FIFA World Cup', 'Buenos Aires', 'Argentina', True),
          ('1978-06-24', 'Brazil', 'Italy', 2, 1,
           'FIFA World Cup', 'Buenos Aires', 'Argentina', True),
          ('1978-06-25', 'Argentina', 'Netherlands', 3, 1,
           'FIFA World Cup', 'Buenos Aires', 'Argentina', False)
          ]

# -----------------------------------------------------------------------------------------------------
# listes des fonctions à implémenter
# -----------------------------------------------------------------------------------------------------

# Fonctions à implémenter dont les tests sont fournis


def match_est_correct(match):
    """indique si le tuple du match est correctement implementé

    Args:
        match (tuple): un match

    Returns:
        bool: True si le tuple du match est correctement implementé, False sinon
    """
    return len(match) == 9 and type(match[0]) == str and type(match[1]) == str and type(match[2]) == str and type(match[5]) == str and type(match[6]) == str and type(match[7]) == str and type(match[3]) == int and type(match[4]) == int and type(match[8]) == bool


def equipe_gagnante(match):
    """retourne le nom de l'équipe qui a gagné le match. Si c'est un match nul on retourne None

    Args:
        match (tuple): un match

    Returns:
        str: le nom de l'équipe gagnante (ou None si match nul)
    """
    if match_est_correct(match) and match[3] != match[4]:
        if match[3] > match[4]:
            return match[1]
        else:
            return match[2]
    return None


def victoire_a_domicile(match):
    """indique si le match correspond à une victoire à domicile

    Args:
        match (tuple): un match

    Returns:
        bool: True si le match ne se déroule pas en terrain neutre et que l'équipe qui reçoit a gagné
    """
    if match_est_correct(match):
        return not match[8] and match[3] > match[4]
    return None


def nb_buts_marques(match):
    """indique le nombre total de buts marqués lors de ce match

    Args:
        match (tuple): un match

    Returns:
        int: le nombre de buts du match 
    """
    if match_est_correct(match):
        return match[3] + match[4]
    return None


def matchs_ville(liste_matchs, ville):
    """retourne la liste des matchs qui se sont déroulés dans une ville donnée

    Args:
        liste_matchs (list): une liste de matchs
        ville (str): le nom d'une ville

    Returns:
        list: la liste des matchs qui se sont déroulé dans la ville ville    
    """
    res = []
    for match in liste_matchs:
        if match_est_correct(match):
            if match[6] == ville:
                res.append(match)
        else:
            return None
    return res


def nombre_moyen_buts(liste_matchs, nom_competition):
    """retourne le nombre moyen de buts marqués par match pour une compétition donnée

    Args:
        liste_matchs (list): une liste de matchs
        nom_competition (str): le nom d'une compétition

    Returns:
        float: le nombre moyen de buts par match pour la compétition
    """
    nb_but = 0
    nb_match = 0
    for match in liste_matchs:
        if match_est_correct(match):
            if match[5] == nom_competition:
                nb_but += match[3]+match[4]
                nb_match += 1
        else:
            return None
    if nb_match == 0 and nb_match == 0:
        return None
    if nb_match == 0:
        return 0
    return nb_but/nb_match


def est_bien_trie(liste_matchs):
    """vérifie si une liste de matchs est bien trié dans l'ordre chronologique
       puis pour les matchs se déroulant le même jour, dans l'ordre alphabétique
       des équipes locales

    Args:
        liste_matchs (list): une liste de matchs

    Returns:
        bool: True si la liste est bien triée et False sinon
    """
    for match in range(1, len(liste_matchs)):
        if match_est_correct(liste_matchs[match]) and match_est_correct(liste_matchs[match-1]):
            if liste_matchs[match][0] < liste_matchs[match-1][0] or liste_matchs[match][0] == liste_matchs[match-1][0] and liste_matchs[match][1] < liste_matchs[match-1][1]:
                return False
        else:
            return None
    return True


def fusionner_matchs(liste_matchs1, liste_matchs2):
    """Fusionne deux listes de matchs triées sans doublons en une liste triée sans doublon
    sachant qu'un même match peut être présent dans les deux listes

    Args:
        liste_matchs1 (list): la première liste de matchs
        liste_matchs2 (list): la seconde liste de matchs

    Returns:
        list: la liste triée sans doublon comportant tous les matchs de liste_matchs1 et liste_matchs2
    """
    res = []
    ind1 = 0
    ind2 = 0
    while ind1 < len(liste_matchs1) and ind2 < len(liste_matchs2):
        if liste_matchs1[ind1] == liste_matchs2[ind2]:
            ind1 += 1
        elif est_bien_trie([liste_matchs1[ind1], liste_matchs2[ind2]]):
            res.append(liste_matchs1[ind1])
            ind1 += 1
        else:
            res.append(liste_matchs2[ind2])
            ind2 += 1
    while ind1 == len(liste_matchs1) and ind2 < len(liste_matchs2):
        res.append(liste_matchs2[ind2])
        ind2 += 1
    while ind2 == len(liste_matchs2) and ind1 < len(liste_matchs1):
        res.append(liste_matchs1[ind1])
        ind1 += 1
    return res


def resultats_equipe(liste_matchs, equipe):
    """donne le nombre de victoire, de matchs nuls et de défaites pour une équipe donnée

    Args:
        liste_matchs (list): une liste de matchs
        equipe (str): le nom d'une équipe (pays)

    Returns:
        tuple: un triplet d'entiers contenant le nombre de victoires, nuls et défaites de l'équipe
    """
    nb_vic = 0
    nb_nul = 0
    nb_def = 0
    for match in range(len(liste_matchs)):
        if match_est_correct(liste_matchs[match]):
            if liste_matchs[match][1] == equipe or liste_matchs[match][2] == equipe:
                equipe_win = equipe_gagnante(liste_matchs[match])
                if equipe_win == equipe:
                    nb_vic += 1
                elif equipe_win == None:
                    nb_nul += 1
                else:
                    nb_def += 1
        else:
            return None
    return (nb_vic, nb_nul, nb_def)


def ecart_but(match):
    """retourne le nombre de but d'écart entre les 2 equipes dans un match

    Args:
        match (tuple): un match

    Returns:
        int: le nombre de but d'écart entre les 2 equipes du match
    """
    if match_est_correct(match):
        if match[3]-match[4] < 0:
            return (match[3]-match[4])*-1
        return match[3]-match[4]
    else:
        return None


def plus_gros_scores(liste_matchs):
    """retourne la liste des matchs pour lesquels l'écart de buts entre le vainqueur et le perdant est le plus grand

    Args:
        liste_matchs (list): une liste de matchs

    Returns:
        list: la liste des matchs avec le plus grand écart entre vainqueur et perdant
    """
    ecart_max = 0
    match_max_ecart = []
    for match in range(len(liste_matchs)):
        if match_est_correct(liste_matchs[match]):
            if ecart_but(liste_matchs[match]) > ecart_max:
                ecart_max = ecart_but(liste_matchs[match])
                match_max_ecart = []
                match_max_ecart.append(liste_matchs[match])
            elif ecart_but(liste_matchs[match]) == ecart_max:
                match_max_ecart.append(liste_matchs[match])
        else:
            return None
    return match_max_ecart


def liste_des_equipes(liste_matchs):
    """retourne la liste des équipes qui ont participé aux matchs de la liste
    Attention on ne veut voir apparaitre le nom de chaque équipe qu'une seule fois

    Args:
        liste_matchs (list): une liste de matchs

    Returns:
        list: une liste de str contenant le noms des équipes ayant jouer des matchs
    """
    res = []
    for match in liste_matchs:
        if match_est_correct(match):
            if match[1] not in res:
                res.append(match[1])
            if match[2] not in res:
                res.append(match[2])
        else:
            return None
    return res

def premiere_victoire(liste_matchs, equipe):
    """retourne la date de la première victoire de l'equipe. Si l'equipe n'a jamais gagné de match on retourne None

    Args:
        liste_matchs (list): une liste de matchs
        equipe (str): le nom d'une équipe (pays)

    Returns:
        str: la date de la première victoire de l'equipe
    """
    for match in liste_matchs:
        if match_est_correct(match):
            if (match[1] == equipe or match[2] == equipe) and equipe_gagnante(match) == equipe:
                return match[0]
        else:
            return None
    return None


def nb_matchs_sans_defaites(liste_matchs, equipe):
    """retourne le plus grand nombre de matchs consécutifs sans défaite pour une equipe donnée.

    Args:
        liste_matchs (list): une liste de matchs
        equipe (str): le nom d'une équipe (pays)

    Returns:
        int: le plus grand nombre de matchs consécutifs sans défaite du pays nom_pays
    """
    # Pour cette fonction je ne savais pas si un match nul annulait la serie de victoire. J'ai consideré que non. Si un match nul annule la série de victoire il faut prendre la fonction en commentaire juste en dessous de celle-ci, c'est la même chose pour mes test.
    serie_match_sans_defaite = 0
    max_serie_match_sans_defaite = 0
    for match in liste_matchs:
        if match_est_correct(match):
            if (match[1] == equipe or match[2] == equipe) and (equipe_gagnante(match) == equipe or equipe_gagnante(match) is None):
                serie_match_sans_defaite += 1
                if serie_match_sans_defaite > max_serie_match_sans_defaite:
                    max_serie_match_sans_defaite = serie_match_sans_defaite
            elif (match[1] == equipe or match[2] == equipe) and equipe_gagnante(match) != equipe:
                serie_match_sans_defaite = 0
        else:
            return None
    return max_serie_match_sans_defaite
    # serie_match_sans_defaite = 0
    # max_serie_match_sans_defaite = 0
    # for match in liste_matchs:
    #     if match_est_correct(match):
    #         if (match[1] == equipe or match[2] == equipe) and equipe_gagnante(match) == equipe :
    #             serie_match_sans_defaite += 1
    #             if serie_match_sans_defaite > max_serie_match_sans_defaite:
    #                 max_serie_match_sans_defaite = serie_match_sans_defaite
    #         elif (match[1] == equipe or match[2] == equipe) and equipe_gagnante(match) != equipe:
    #             serie_match_sans_defaite = 0
    #     else:
    #         return None
    # return max_serie_match_sans_defaite


def charger_matchs(nom_fichier):
    """charge un fichier de matchs donné au format CSV en une liste de matchs

    Args:
        nom_fichier (str): nom du fichier CSV contenant les matchs

    Returns:
        list: la liste des matchs du fichier
    """
    fic = open(nom_fichier, 'r', encoding="utf-8")
    fic.readline()
    res = []
    for ligne in fic:
        l_champs = ligne.split(",")
        res.append((str(l_champs[0]), str(l_champs[1]), str(l_champs[2]), int(l_champs[3]), int(l_champs[4]), str(
            l_champs[5]), str(l_champs[6]), str(l_champs[7]), eval(l_champs[8][0].upper()+l_champs[8][1:-1].lower())))
    fic.close()
    return res

# print(charger_matchs("histoire1.csv"))


def sauver_matchs(liste_matchs, nom_fichier):
    """sauvegarde dans un fichier au format CSV une liste de matchs

    Args:
        liste_matchs (list): la liste des matchs à sauvegarder
        nom_fichier (str): nom du fichier CSV

    Returns:
        None: cette fonction ne retourne rien
    """
    fic = open(nom_fichier, 'w', encoding="utf-8")
    fic.write(
        "date,home_team,away_team,home_score,away_score,tournament,city,country,neutral\n")
    for match in liste_matchs:
        fic.write(match[0]+","+match[1]+","+match[2]+","+str(match[3])+"," +
                  str(match[4])+","+match[5]+","+match[6]+","+match[7]+","+str(match[8])+"\n")
    fic.close()


# Fonctions à implémenter dont il faut également implémenter les tests


def plus_de_victoires_que_defaites(liste_matchs, equipe):
    """vérifie si une équipe donnée a obtenu plus de victoires que de défaites
    Args:
        liste_matchs (list): une liste de matchs
        equipe (str): le nom d'une équipe (pays)

    Returns:
        bool: True si l'equipe a obtenu plus de victoires que de défaites
    """
    nb_victoires = 0
    nb_defaites = 0
    for match in liste_matchs:
        if match_est_correct(match):
            if (match[1] == equipe or match[2] == equipe) and equipe_gagnante(match) == equipe:
                nb_victoires += 1
            elif (match[1] == equipe or match[2] == equipe) and equipe_gagnante(match) != equipe and equipe_gagnante(match) != None:
                nb_defaites += 1
        else:
            return None
    return nb_victoires > nb_defaites


def matchs_spectaculaires(liste_matchs):
    """retourne la liste des matchs les plus spectaculaires, c'est à dire les
    matchs dont le nombre total de buts marqués est le plus grand

    Args:
        liste_matchs (list): une liste de matchs

    Returns:
        list: la liste des matchs les plus spectaculaires
    """
    nb_buts_max = 0
    res = []
    for match in liste_matchs:
        if match_est_correct(match):
            if match[3] + match[4] > nb_buts_max:
                res = []
                res.append(match)
                nb_buts_max = match[3] + match[4]
            elif match[3] + match[4] == nb_buts_max:
                res.append(match)
        else:
            return None
    return res


def meilleures_equipes(liste_matchs):
    """retourne la liste des équipes de la liste qui ont le plus petit nombre de defaites

    Args:
        liste_matchs (list): une liste de matchs

    Returns:
        list: la liste des équipes qui ont le plus petit nombre de defaites
    """
    res = []
    liste_equipes = liste_des_equipes(liste_matchs)
    min_def = None
    for equipe in liste_equipes:
        if min_def == None or resultats_equipe(liste_matchs, equipe)[2] < min_def:
            min_def = resultats_equipe(liste_matchs, equipe)[2]
            res = []
            res.append(equipe)
        elif resultats_equipe(liste_matchs, equipe)[2] == min_def:
            res.append(equipe)
    return res