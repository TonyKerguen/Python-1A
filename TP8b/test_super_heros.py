import super_heros

avengers = {' Spiderman ': (5 , 5 , ' araign ée a quatre pattes ') ,
            ' Hulk ': (7 , 4 , " Grand homme vert " ) ,
            ' Agent 13 ': (2 , 3 , ' agent 13 ') ,
            'M Melin ': (2 , 6, ' expert en archi ')}
exemple2 = { 'a ':(1 , 1, 'a ') , 'b ':(3 , 9, 'b ') , 'c ':(7 , 2, 'c ')}
exemple3 = { 'a ':(1 , 1, 'a ') , 'b ':(3 , 9, 'b ') , 'd ':(4 , 4, 'd ')}

def test_intelligence_moyenne():
    assert super_heros.intelligence_moyenne ( avengers ) == 4.5
    assert super_heros.intelligence_moyenne ( exemple2 ) == 4
    assert abs ( super_heros.intelligence_moyenne ( exemple3 ) -14/3) <= 0.01


def test_kikelplusfort():
    assert super_heros.kikelplusfort(avengers) == ' Hulk '
    assert super_heros.kikelplusfort(exemple2) == 'c '
    assert super_heros.kikelplusfort(exemple3) == 'd '


def test_combienDeCretins():
    assert super_heros.combienDeCretins(avengers) == 2
    assert super_heros.combienDeCretins(exemple2) == 2
    assert super_heros.combienDeCretins(exemple3) == 2