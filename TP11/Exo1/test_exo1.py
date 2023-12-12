import tp11 as ff

week_end_mai = {"Pierre": [70, 10, 12], "Paul":[100], "Marie":[15], "Anna":[]}
week_end_juin = {"Pierre": [15, 12, 8, 3], "Béatrice": [8], "Sacha":[], "Anna":[52], "Marie": [20, 34]}


def test_depense_dune_personne():
    assert ff.depense_dune_personne([70, 10, 12]) == 92
    assert ff.depense_dune_personne([100]) == 100
    assert ff.depense_dune_personne([]) == 0

def test_somme_depense():
    assert ff.somme_depense(week_end_mai) == 207
    assert ff.somme_depense(week_end_juin) == 152

def test_test_somme_depense():
    assert ff.get_nb_personne(week_end_mai) == 4
    assert ff.get_nb_personne(week_end_juin) == 5

def test_moyenne_depense_par_personne():
    assert ff.moyenne_depense_par_personne(week_end_mai) ==  51.75
    assert ff.moyenne_depense_par_personne(week_end_juin) == 30.40

def test_combien_doit_payer():
    assert ff.combien_doit_payer(30.40, 0) == 30.40
    assert ff.combien_doit_payer(30.40, 54) == -23.6
    assert ff.combien_doit_payer(30.40, 8) == 22.40