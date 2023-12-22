"""
Permet de modéliser un le_plateau de jeu avec :
    - une matrice qui contient des nombres entiers
    - chaque nombre entier correspond à un item :
      MUR, COULOIR, PERSONNAGE, FANTOME
"""
import matrice

MUR = 1
COULOIR = 0
PERSONNAGE = 2
FANTOME = 3

NORD = 'z'
OUEST = 'q'
SUD = 's'
EST = 'd'


def init(nom_fichier="/home/iut45/Etudiants/o22205496/home_iut/INIT_PROG/Python-1A/TP12/labyrinthe/labyrinthe1.txt"):
    """Construit le plateau de jeu de la façon suivante :
        - crée une matrice à partir d'un fichier texte qui contient des COULOIR et MUR
        - met le PERSONNAGE en haut à gauche cad à la position (0, 0)
        - place un FANTOME en bas à droite
    Args:
        nom_fichier (str, optional): chemin vers un fichier csv qui contient COULOIR et MUR.
        Defaults to "./labyrinthe1.txt".

    Returns:
        le plateau de jeu avec les MUR, COULOIR, PERSONNAGE et FANTOME
    """
    # plateau = dict()
    # fic = open(nom_fichier, 'r', encoding="utf-8")
    # l = 0
    # for ligne in fic:
    #     c = 0
    #     for colonne in ligne[:-1].split(","):
    #         plateau[(l, c)] = colonne
    #         c += 1
    #     l += 1
    # plateau[(0, 0)] = PERSONNAGE
    # plateau[(l-1, c-1)] = FANTOME
    # return plateau
    plateau = matrice.charge_matrice(nom_fichier)
    matrice.set_val(plateau, 0, 0, PERSONNAGE)
    matrice.set_val(plateau, matrice.get_nb_lignes(plateau)-1, matrice.get_nb_colonnes(plateau)-1, FANTOME)
    return plateau

# print(init())


def est_sur_le_plateau(le_plateau, position):
    """Indique si la position est bien sur le plateau

    Args:
        le_plateau (plateau): un plateau de jeu
        position (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        [boolean]: True si la position est bien sur le plateau
    """
    if position[0] >= 0 and position[1] >= 0:
        if matrice.get_val(le_plateau,  position[0], position[1]) != None:
            return True
        else:
            return False
    else:
        return False
    
# print(est_sur_le_plateau(init(), (3, 10)))

def get(le_plateau, position):
    """renvoie la valeur de la case qui se trouve à la position donnée

    Args:
        le_plateau (plateau): un plateau de jeu
        position (tuple): un tuple d'entiers de la forme (no_ligne, no_colonne)

    Returns:
        int: la valeur de la case qui se trouve à la position donnée ou
             None si la position n'est pas sur le plateau
    """
    return matrice.get_val(le_plateau,  position[0], position[1])


def est_un_mur(le_plateau, position):
    """détermine s'il y a un mur à la poistion donnée

    Args:
        le_plateau (plateau): un plateau de jeu
        position (tuple): un tuple d'entiers de la forme (no_ligne, no_colonne)

    Returns:
        bool: True si la case à la position donnée est un MUR, False sinon
    """
    return matrice.get_val(le_plateau,  position[0], position[1]) == MUR


def contient_fantome(le_plateau, position):
    """Détermine s'il y a un fantôme à la position donnée

    Args:
        le_plateau (plateau): un plateau de jeu
        position (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        bool: True si la case à la position donnée est un FANTOME, False sinon
    """
    return matrice.get_val(le_plateau,  position[0], position[1]) == FANTOME

def est_la_sortie(le_plateau, position):
    """Détermine si la position donnée est la sortie
       cad la case en bas à droite du labyrinthe

    Args:
        le_plateau (plateau): un plateau de jeu
        position (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        bool: True si la case à la position donnée est la sortie, False sinon
    """
    return position[0] == matrice.get_nb_lignes(le_plateau)-1 and position[1] == matrice.get_nb_colonnes(le_plateau)-1


def deplace_personnage(le_plateau, personnage, direction):
    """déplace le PERSONNAGE sur le plateau si le déplacement est valide
       Le personnage ne peut pas sortir du plateau ni traverser les murs
       Si le déplacement n'est pas valide, le personnage reste sur place

    Args:
        le_plateau (plateau): un plateau de jeu
        personnage (tuple): la position du personnage sur le plateau
        direction (str): la direction de déplacement SUD, EST, NORD, OUEST

    Returns:
        [tuple]: la nouvelle position du personnage
    """
    if direction == NORD and not est_un_mur(le_plateau, (personnage[0]-1, personnage[1])) and est_sur_le_plateau(le_plateau, (personnage[0]-1, personnage[1])):
        matrice.set_val(le_plateau, personnage[0], personnage[1], COULOIR)
        personnage = (personnage[0]-1, personnage[1])
        matrice.set_val(le_plateau, personnage[0], personnage[1], PERSONNAGE)

    if direction == SUD and not est_un_mur(le_plateau, (personnage[0]+1, personnage[1])) and est_sur_le_plateau(le_plateau, (personnage[0]+1, personnage[1])):
        matrice.set_val(le_plateau, personnage[0], personnage[1], COULOIR)
        personnage = (personnage[0]+1, personnage[1])
        matrice.set_val(le_plateau, personnage[0], personnage[1], PERSONNAGE)

    if direction == OUEST and not est_un_mur(le_plateau, (personnage[0], personnage[1]-1)) and est_sur_le_plateau(le_plateau, (personnage[0], personnage[1]-1)):
        matrice.set_val(le_plateau, personnage[0], personnage[1], COULOIR)
        personnage = (personnage[0], personnage[1]-1)
        matrice.set_val(le_plateau, personnage[0], personnage[1], PERSONNAGE)

    if direction == EST and not est_un_mur(le_plateau, (personnage[0], personnage[1]+1)) and est_sur_le_plateau(le_plateau, (personnage[0], personnage[1]+1)):
        matrice.set_val(le_plateau, personnage[0], personnage[1], COULOIR)
        personnage = (personnage[0], personnage[1]+1)
        matrice.set_val(le_plateau, personnage[0], personnage[1], PERSONNAGE)

    return personnage

def voisins(le_plateau, position):
    """Renvoie l'ensemble des positions cases voisines accessibles de la position renseignées
       Une case accessible est une case qui est sur le plateau et qui n'est pas un mur
    Args:
        le_plateau (plateau): un plateau de jeu
        position (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        set: l'ensemble des positions des cases voisines accessibles
    """
    accessibles = set()

    if not est_un_mur(le_plateau, (position[0]-1, position[1])) and est_sur_le_plateau(le_plateau, (position[0]-1, position[1])):
        accessibles.add((position[0]-1, position[1]))

    if not est_un_mur(le_plateau, (position[0]+1, position[1])) and est_sur_le_plateau(le_plateau, (position[0]+1, position[1])):
        accessibles.add((position[0]+1, position[1]))

    if not est_un_mur(le_plateau, (position[0], position[1]-1)) and est_sur_le_plateau(le_plateau, (position[0], position[1]-1)):
        accessibles.add((position[0], position[1]-1))

    if not est_un_mur(le_plateau, (position[0], position[1]+1)) and est_sur_le_plateau(le_plateau, (position[0], position[1]+1)):
        accessibles.add((position[0], position[1]+1))

    return accessibles


def fabrique_le_calque(le_plateau, position_depart):
    """fabrique le calque d'un labyrinthe en utilisation le principe de l'inondation :
       
    Args:
        le_plateau (plateau): un plateau de jeu
        position_depart (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        matrice: une matrice qui a la taille du plateau dont la case qui se trouve à la
       position_de_depart est à 0 les autres cases contiennent la longueur du
       plus court chemin pour y arriver (les murs et les cases innaccessibles sont à None)
    """
    calque = matrice.new_matrice(matrice.get_nb_lignes(le_plateau), matrice.get_nb_colonnes(le_plateau), None)
    matrice.set_val(calque, position_depart[0], position_depart[1], 0)
    inondation = True
    actu = 0
    while inondation:
        inondation = False
        for l in range(matrice.get_nb_lignes(calque)):
            for c in range(matrice.get_nb_colonnes(calque)):
                if get(calque, (l, c)) == actu:
                    for voisin in voisins(le_plateau, (l, c)):
                        if get(calque, voisin) == None and not est_un_mur(le_plateau,voisin):
                            matrice.set_val(calque, voisin[0], voisin[1], actu+1)
                            inondation = True
        actu += 1
    return calque

def fabrique_chemin(le_plateau, position_depart, position_arrivee):
    """Renvoie le plus court chemin entre position_depart position_arrivee

    Args:
        le_plateau (plateau): un plateau de jeu
        position_depart (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 
        position_arrivee (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        list: Une liste de positions entre position_arrivee et position_depart
        qui représente un plus court chemin entre les deux positions
    """
    res = []
    calque = fabrique_le_calque(le_plateau, position_arrivee)
    pos_actu = position_depart
    while pos_actu != position_arrivee:
        trouve = False
        for voisin in voisins(le_plateau, pos_actu):
            if get(calque, voisin) == get(calque, pos_actu)-1 and not trouve:
                pos_actu = voisin
                trouve = True
                res.insert(0, pos_actu)
    if res == []:
        res.append(position_depart)
    return res


def deplace_fantome(le_plateau, fantome, personnage):
    """déplace le FANTOME sur le plateau vers le personnage en prenant le chemin le plus court

    Args:
        le_plateau (plateau): un plateau de jeu
        fantome (tuple): la position du fantome sur le plateau
        personnage (tuple): la position du personnage sur le plateau

    Returns:
        [tuple]: la nouvelle position du FANTOME
    """
    new_pos = fabrique_chemin(le_plateau, fantome, personnage)[-1]
    matrice.set_val(le_plateau, fantome[0], fantome[1], COULOIR)
    matrice.set_val(le_plateau, new_pos[0], new_pos[1], FANTOME)
    return new_pos
