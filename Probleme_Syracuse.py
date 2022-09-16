"""On étudie la suite de Syracuse"""

from time import time

def tempsdevol(num :int) -> int:
    n = 0
    
    while num != 1:
        n += 1
        if num % 2 == 0:
            num /= 2
        else:
            num *= 3
            num += 1
            
    return n

def altitude(num :int) -> float:
    l = []
    
    while num != 1:
        if num % 2 == 0:
            num /= 2
            l.append(num)
        else:
            num *= 3
            num += 1
            l.append(num)
            
    return(max(l))

# tempsdarret() ver1

# def tempsdarret(c):
#     for i in range(1, 1_000_001):
#         if altitude(i) > c:
#             
#             return altitude(i)

# tempsdarret() ver2

def tempsdarret(c :int) -> int:
    Un = c
    n = 0  # Indice n du terme de Un < c
    while Un >= c:
        if Un % 2 == 0:
            Un /= 2
            n =+ 1
        else:
            Un = Un * 3 + 1
            n += 1
    
    return n

# Probablement inutile

# def f(c):
#     """tempsdarret mais avec une boucle while"""
#     
#     i = 1
#     
#     while i < 1_000_001 and altitude(i) <= c:
#         i += 1
#     return altitude(i)

def verification(m :int):
    temps = time()
    
    for i in range(2, m + 1):
        tempsdarret(i)
    temps2 = time()
    
    return temps2 - temps

def verif(m):
    """On vérifie qu'il existe bien un temps d'arrêt pour les entiers allant de 7 à m"""
    temps = time()
    i = 1

    while i * 4 + 3 < m:
        tempsdarret(i * 4 + 3)
    temps2 = time()

    return temps2 - temps
