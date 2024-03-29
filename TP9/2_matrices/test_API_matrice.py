""" tests pour les API matrices 
    Remarques : tous les tests de ce fichier doivent passer quelle que soit l'API utilisée
    """
import API_matrice1 as API
import utilitaires_matrice as APIut

def matrice1():
    m1 = API.construit_matrice(3, 4, None)
    API.set_val(m1, 0, 0, 10)
    API.set_val(m1, 0, 1, 11)    
    API.set_val(m1, 0, 2, 12)
    API.set_val(m1, 0, 3, 13)
    API.set_val(m1, 1, 0, 14)
    API.set_val(m1, 1, 1, 15)
    API.set_val(m1, 1, 2, 16)
    API.set_val(m1, 1, 3, 17)
    API.set_val(m1, 2, 0, 18)
    API.set_val(m1, 2, 1, 19)
    API.set_val(m1, 2, 2, 20)
    API.set_val(m1, 2, 3, 21)
    return m1

print(matrice1())

def matrice2():
    m2 = API.construit_matrice(2, 3, None)
    print(m2)
    API.set_val(m2, 0, 0, 'A')
    API.set_val(m2, 0, 1, 'B')    
    API.set_val(m2, 0, 2, 'C')
    API.set_val(m2, 1, 0, 'D')
    API.set_val(m2, 1, 1, 'E')
    API.set_val(m2, 1, 2, 'F')
    return m2

print(matrice2())

def matrice3():
    m3 = API.construit_matrice(3, 3, None)
    API.set_val(m3, 0, 0, 2)
    API.set_val(m3, 0, 1, 7)    
    API.set_val(m3, 0, 2, 6)
    API.set_val(m3, 1, 0, 9)
    API.set_val(m3, 1, 1, 5)
    API.set_val(m3, 1, 2, 1)
    API.set_val(m3, 2, 0, 4)
    API.set_val(m3, 2, 1, 3)
    API.set_val(m3, 2, 2, 8)
    return m3

def test_get_nb_lignes():
    m1 = matrice1()
    m2 = matrice2()
    m3 = matrice3()
    assert API.get_nb_lignes(m1) == 3
    assert API.get_nb_lignes(m2) == 2
    assert API.get_nb_lignes(m3) == 3
        
def test_get_nb_colonnes():
    m1 = matrice1()
    m2 = matrice2()
    m3 = matrice3()
    assert API.get_nb_colonnes(m1) == 4
    assert API.get_nb_colonnes(m2) == 3
    assert API.get_nb_colonnes(m3) == 3

def test_get_val():
    m1 = matrice1()
    m2 = matrice2()
    m3 = matrice3()
    assert API.get_val(m1, 0, 1) == 11
    assert API.get_val(m1, 2, 1) == 19
    assert API.get_val(m2, 1, 1) == 'E'
    assert API.get_val(m2, 0, 2) == 'C'
    assert API.get_val(m3, 2, 0) == 4
    assert API.get_val(m3, 1, 0) == 9

def test_sauve_charge_matrice():
    matrice = matrice2()
    API.sauve_matrice(matrice, "matrice.csv")
    matrice_bis = API.charge_matrice_str("matrice.csv")
    assert matrice == matrice_bis

def test_get_ligne():
    m1 = matrice1()
    m3 = matrice3()
    assert API.get_ligne(m1,1) == [14, 15, 16, 17]
    assert API.get_ligne(m3,2) == [4, 3, 8]

def test_get_colonne():
    m1 = matrice1()
    m3 = matrice3()
    assert API.get_colonne(m1,1) == [11, 15, 19]
    assert API.get_colonne(m3,2) == [6, 1, 8]

def test_get_diagonale_principale():
    m3 = matrice3()
    assert APIut.get_diagonale_principale(m3) == [2,5,8]

def test_get_diagonale_secondaire():
    m3 = matrice3()
    assert APIut.get_diagonale_secondaire(m3) == [6,5,4]

def test_transposee():
    m3 = matrice3()
    assert APIut.transpose(m3) == (3, 3, [2,9,4,7,5,3,6,1,8])

def test_is_triangulaire_inf():
    m3 = matrice3()
    assert not APIut.is_triangulaire_inf(m3)
    assert APIut.is_triangulaire_inf((3, 3, [1, 0, 0, 2, 2, 0, 3, 3, 3]))

def test_bloc():
    m3 = matrice3()
    assert APIut.bloc(m3, 0, 0, 2, 2) == (2, 2, [2, 7, 9, 5])
    assert APIut.bloc(m3, 1, 1, 2, 2) == (2, 2, [5, 1, 3, 8])