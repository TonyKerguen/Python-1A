import exo3 as matrice

matrice1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

matrice2 = [[1,  2,  3,  4],
            [5,  6,  7,  8],
            [9,  10, 11, 12],
            [13, 14, 15, 16]]

def test_get_ligne():
    assert matrice.get_ligne(matrice1,0) == [1, 2, 3]
    assert matrice.get_ligne(matrice2,1) == [5, 6, 7, 8]

def test_bloc():
    assert matrice.sm(matrice1, 0, 0, 2, 2) == [[1, 2], [4, 5]]
    assert matrice.sm(matrice2, 1, 1, 2, 2) == [[6, 7], [10, 11]]
    assert matrice.sm(matrice2, 1, 1, 5, 5) is None

def test_colle_sous_matrice():
    assert matrice.colle_sous_matrice([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[67, 42], [43, 17]], 0, 0) == [[67, 42, 3], [43, 17, 6], [7, 8, 9]]
    assert matrice.colle_sous_matrice([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[67, 42], [43, 17]], 1, 1) == [[1, 2, 3], [4, 67, 42], [7, 43, 17]]