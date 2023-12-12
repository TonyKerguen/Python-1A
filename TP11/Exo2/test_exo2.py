import exo2 as couple

ATM = {'Armand':'Beatrice','Beatrice':'Cesar','Cesar':'Dalida',
     'Dalida':'Cesar','Etienne':'Beatrice','Firmin':'Henri',
     'Gaston':'Beatrice','Henri':'Firmin'}

def test_trouver_couple_reciproque():
    assert couple.trouver_couple_reciproque(ATM) == {('Dalida', 'Cesar'), ('Henri', 'Firmin')}

def test_soupirants():
    assert couple.soupirants(ATM, 'Beatrice') == {'Armand', 'Etienne', 'Gaston'}
    assert couple.soupirants(ATM, 'Armant') == {}