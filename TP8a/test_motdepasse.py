import motdepasse

# --------------------------------------
# FONCTIONS
# --------------------------------------

def test_longueur_ok():
    assert motdepasse.longueur_ok("choubouilli") # longueur ok
    assert not motdepasse.longueur_ok("chou") # longueur pas ok
    assert not motdepasse.longueur_ok("") # chaine vide


def test_chiffre_ok():
    assert not motdepasse.chiffre_ok("chou9bouilli")  # chiffre au milieu
    assert not motdepasse.chiffre_ok("7choubouilli")  # chiffre au début
    assert not motdepasse.chiffre_ok("choubouilli5")  # chiffre à la fin
    assert not motdepasse.chiffre_ok("chou3boui8lli")  # deux chiffres    
    assert not motdepasse.chiffre_ok("chou")       # pas de chiffres
    assert not motdepasse.chiffre_ok("un deux trois") # pas de chiffres
    assert motdepasse.chiffre_ok("chou3boui8lli4")  # trois chiffres   


def test_sans_espace():
    assert motdepasse.sans_espace("choubouilli") # sans espace ok
    assert not motdepasse.sans_espace("chou bouilli") # espace au milieu
    assert not motdepasse.sans_espace(" choubouilli") # espace au début
    assert not motdepasse.sans_espace("choubouilli ") # espace à la fin
    assert motdepasse.sans_espace("") # chaine vide


def test_sans_deux_chiffre_consecutif():
    assert not motdepasse.sans_deux_chiffre_consecutif("a")
    assert motdepasse.sans_deux_chiffre_consecutif("aa")
    assert not motdepasse.sans_deux_chiffre_consecutif("a11")
    assert motdepasse.sans_deux_chiffre_consecutif("1a1")

def test_plus_petit_chiffre_apparait_une_seul_fois():
    assert not motdepasse.plus_petit_chiffre_apparait_une_seul_fois("aaa")
    assert not motdepasse.plus_petit_chiffre_apparait_une_seul_fois("1a2a3a1")
    assert motdepasse.plus_petit_chiffre_apparait_une_seul_fois("1a2a3a3")
    assert motdepasse.plus_petit_chiffre_apparait_une_seul_fois("1a2202a3a3")