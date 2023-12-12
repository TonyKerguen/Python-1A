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

print(syracuse(5))

def temps_de_vol(n:int):
    return len(syracuse(n))
    

print(temps_de_vol(-1))