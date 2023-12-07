week_end_mai = {"Pierre": [70, 10, 12], "Paul":[100], "Marie":[15], "Anna":[]}
week_end_juin = {"Pierre": [15, 12, 8,3], "Béatrice": [8], "Sacha":[], "Anna":[52], "Marie": [20, 34]}


def depense_dune_personne(depenses:list):
    """renvoit la somme des dépenses qu'une personne a dépenser

    Args:
        depenses (list): une liste des dépenses d'une personne

    Returns:
        int: la somme des dépenses
    """    
    somme = 0
    for depense in depenses:
        somme += depense
    return somme

def somme_depense(weekend:dict):
    """renvoit la somme de toutes les dépenses de toutes les personnes

    Args:
        weekend (dict): un doctionnaire Nom personne : liste des dépenses

    Returns:
        int: la somme de toutes les dépenses
    """    
    somme = 0
    for depenses in weekend.values():
        somme += depense_dune_personne(depenses)
    return somme

def get_nb_personne(weekend:dict):
    """renvoit le nombre de participant d'un week end

    Args:
        weekend (dict): un doctionnaire Nom personne : liste des dépenses

    Returns:
        int: le nombre de participant
    """    
    return len(weekend)

def moyenne_depense_par_personne(weekend:dict):
    """renvoit la moyenne des dépenses de tout les participant d'un week end

    Args:
        weekend (dict): un doctionnaire Nom personne : liste des dépenses

    Returns:
        int: la moyenne des dépenses
    """    
    return somme_depense(weekend)/get_nb_personne(weekend)

def combien_doit_payer(moyenne:int, depense:int):
    """renvoit combien d'argent une personne doit payer/recevoir

    Args:
        moyenne (int): la moyenne des dépenses
        depense (int): combien la personne a dépenser

    Returns:
        int: combien d'argent une personne doit payer/recevoir
    """    
    return moyenne - depense

def affiche_bilan_financier(weekend):
    """affiche le bilan financier du weekend

    Args:
        weekend (dict): un doctionnaire Nom personne : liste des dépenses
    """    
    moyenne = moyenne_depense_par_personne(weekend)
    for personne, depenses in weekend.items():
        rembourse = combien_doit_payer(moyenne, depense_dune_personne(depenses))
        if rembourse == 0:
            print(personne + "est ne doit rien verser ni recevoir !")
        elif rembourse > 0:
            print(personne + "doit verser " + str(round(rembourse, 2)) + " euros")
        else:
            print(personne + "doit recevoir " + str(round(rembourse*-1, 2)) + " euros")

affiche_bilan_financier(week_end_juin)