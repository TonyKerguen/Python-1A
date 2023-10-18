# --------------------------------------
# DONNEES
# --------------------------------------

# exemple de liste d'oiseaux observables
oiseaux = [("Merle", "Turtidé"), ("Moineau", "Passereau"), ("Mésange", "Passereau"),
           ("Pic vert", "Picidae"), ("Pie", "Corvidé"), ("Pinson", "Passereau"),
           ("Rouge-gorge", "Passereau"), ("Tourterelle", "Colombidé")] 

# exemples de listes de comptage ces listes ont la même longueur que oiseaux
comptage1 = [2, 5, 0, 1, 2, 0, 3, 5]
comptage2 = [2, 1, 3, 0, 0, 3, 5, 1]
comptage3 = [0, 0, 4, 3, 2, 1, 2, 4]

# exemples de listes d'observations. Notez que chaque liste correspond à la liste de comptage de
# même numéro
observations1 = [("Merle", 2), ("Moineau", 5), ("Pic vert", 1), ("Pie", 2),
                 ("Rouge-gorge", 3), ("Tourterelle", 5)]

observations2 = [("Merle", 2), ("Mésange", 1), ("Moineau", 3),
                 ("Pinson", 3), ("Tourterelle", 5), ("Rouge-gorge", 1)]

observations3 = [("Mésange", 4), ("Pic vert", 3), ("Pie", 2), ("Pinson", 1),
                 ("Rouge-gorge", 2), ("Tourterelle", 4)]

observations4=[("Mésange", 4), ("Pic vert", 3), ("Pie", 2), ("Pinson", 1),
                 ("Rouge-gorge", 2), ("Tourterelle", 0)]

observations5=[("ZZZZZMésange", 4), ("xPic vert", 3), ("zPie", 2), ("Pinson", 1),
                 ("Rouge-gorge", 2), ("Tourterelle", 4)]


# --------------------------------------
# FONCTIONS
# --------------------------------------

def oiseau_le_plus_observe(liste_observations):
    """ recherche le nom de l'oiseau le plus observé de la liste
        (si il y en a plusieur on donne le 1er trouve)

    Args:
        liste_observations (list): une liste de tuples (nom_oiseau, nb_observes)

    Returns:
        str: l'oiseau le plus observé (None si la liste est vide)
    """
#    oiseau_max = (None,0)
#    for observation in liste_observations:
#        if observation[1] > oiseau_max[1]:
#            oiseau_max = observation
#    return oiseau_max[0]
    oiseaux_max=(None,0)
    for i in range(len(liste_observations)):
        if liste_observations[i][1]>oiseaux_max[1]:
            oiseaux_max=liste_observations[i]
    return oiseaux_max[0]

def recherche_oiseau(liste_oiseaux,oiseau):
    for oiseaux in liste_oiseaux:
        if oiseaux[0]==oiseau:
            return oiseaux
    return None

def recherche_par_famille(liste_oiseaux,famille):
    res=[]
    for oiseaux in liste_oiseaux:
        if oiseaux[1]==famille:
            res.append(oiseaux[0])
    return res

def est_liste_observations(liste_observations):
    dernier_oiseau=liste_observations[0]
    for i in range(1,len(liste_observations)):
        if dernier_oiseau[0]>liste_observations[i][0] or dernier_oiseau[1]==0 or liste_observations[i][1]==0 :
            return False
        dernier_oiseau=liste_observations[i]
    return True


def max_observations(liste_observations):
    res=0
    for oiseaux in liste_observations:
        if oiseaux[1]>res:
            res=oiseaux[1]
    return res        

def moyenne_oiseaux_observes(liste_observations):
    cpt_oiseaux=0
    cpt=0
    for oiseaux in liste_observations:
        cpt_oiseaux+=oiseaux[1]
        cpt+=1
    if cpt==0:
        return None    
    return cpt_oiseaux/cpt

def total_famille(liste_observations,liste_oiseaux,famille):
    res=recherche_par_famille(liste_oiseaux,famille)
    cpt=0
    for oiseaux1 in liste_observations:
         if oiseaux1[0] in res:
             cpt+=oiseaux1[1]
    return cpt

def construire_liste_observations(liste_oiseaux,liste_comptage):
    res=[]
    for i in range(len(liste_oiseaux)):
        res.append((liste_oiseaux[i][0],liste_comptage[i]))
    return res

def construire_liste_observations_selon_utilisateur(liste_oiseaux):
    res = []
    for i in range(len(liste_oiseaux)):
        observation = input("Combien a tu observé de "+liste_oiseaux[i][0]+" ? ")
        if int(observation) > 0:
            res.append((liste_oiseaux[i][0],int(observation)))
    return res

# print(construire_liste_observations_selon_utilisateur(oiseaux))

# Exercice 5
def afficher_observation(liste_oiseaux, liste_observations):
    res = ""
    for observ in liste_observations:
        res += "\nNom: "+observ[0].ljust(15)+"Famille: "+recherche_oiseau(liste_oiseaux,observ[0])[1].ljust(15)+"Nb observés: "+str(observ[1])
    return res

# print(afficher_observation(oiseaux,observations1))

def graphiques(liste_observations,seuil):
    res = ""
    for obs in liste_observations:
        if obs[1]>=seuil:
            res+="**  "
        else:
            res+="    "
    return res

# print(graphiques(observations1,6))
# print(graphiques(observations1,5))
# print(graphiques(observations1,4))
# print(graphiques(observations1,3))
# print(graphiques(observations1,2))
# print(graphiques(observations1,1))

def total_graphiques(liste_observations,seuil):
    res = ""
    while seuil>0:
        res += "\n"+graphiques(liste_observations,seuil)
        seuil-=1
    return res 

# print(total_graphiques(observations1,max_observations(observations1)))

def trois_prem_lettres(liste_observations):
    res = ""
    for oiseau in liste_observations:
        res+=oiseau[0][:3]+" "
    return res

# print(trois_prem_lettres(observations1))

#--------------------------------------
# PROGRAMME PRINCIPAL
#--------------------------------------

def afficher_graphique_observation(liste_observations):
    return total_graphiques(liste_observations,max_observations(liste_observations))+"\n"+trois_prem_lettres(liste_observations)+"\n"

print(afficher_graphique_observation(observations1))
