import time


temps_connus = {10: 6, 124: 108}

def syracuse(n:int):
    """renvoie la suite de Syracuse sous la forme d'une liste

    Args:
        n (int): le nombre dont on cherche sa suite de Syracuse

    Returns:
        liste: la suite de Syracuse
    """    
    res = [n]
    if n < 1:
        return "Il me faut un nombre supérieur à 0"
    while res[-1] != 1:
        if res[-1]%2 == 0:
            res.append(round(res[-1]/2))
        else:
            res.append(round(3*res[-1]+1))
    return res

# print(syracuse(1))

def temps_de_vol(n:int):
    """renvoie le temps de vol de l'entier n

    Args:
        n (int): un entier

    Returns:
        int: le temps de vol de l'entier n
    """    
    return len(syracuse(n))-1
    
print(temps_de_vol(45644))

def temps_de_vol_avec_precalcul(n:int, temps_connus:dict):
    if n in temps_connus.keys():
        return temps_connus[n]
    else:
        temps_vol = 0
        while n != 1 and n not in temps_connus.keys():
            if n%2 == 0:
                n = n // 2
            else:
                n = n*3 + 1
            temps_vol += 1
        if n in temps_connus.keys():
            return temps_connus[n] + temps_vol
        else:
            return temps_vol

print(temps_de_vol_avec_precalcul(45644, {}))

def champion(n:int):
    start_time = time.time()
    champion = n
    temps_champion = temps_de_vol(n)
    for nombre in range(1,n-1):
        temps_nombre = temps_de_vol(nombre)
        if temps_nombre > temps_champion:
            temps_champion = temps_nombre
            champion = nombre
    end_time = time.time()
    return champion, f'Time elapsed: {end_time - start_time} seconds', 

def champion_v2(n:int, temps_connus:dict):
    start_time = time.time()
    champion = n
    temps_champion = temps_de_vol_avec_precalcul(n, temps_connus)
    for nombre in range(1,n-1):
        temps_nombre = temps_de_vol_avec_precalcul(nombre, temps_connus)
        if temps_nombre > temps_champion:
            temps_champion = temps_nombre
            champion = nombre
    end_time = time.time()
    return champion, f'Time elapsed: {end_time - start_time} seconds'

print(champion(124))
print(champion_v2(124, temps_connus))

# print(champion(124))
# 45644