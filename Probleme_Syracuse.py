"""On étudie la suite de Syracuse"""

from ast import Index
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

# tempsdarret() ver2

def tempsdarret(c :int) -> int:
    Un = c
    n = 0   # Indice n du terme de Un < c
    while Un >= c:
        if Un % 2 == 0:
            Un /= 2
            n =+ 1
        else:
            Un = Un * 3 + 1
            n += 1
    
    return n

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

# Question 6

def vol_max() -> tuple:
    """Renvoie un tuple contenant respectivement l'index puis la 
    valeur du max des qltitudes des 10**6 premiers entiers"""
    values = []                          # C'est là qu'on stoquera les altitudes maximales

    for i in range(1, 1_000_001):
        values.append(altitude(i))
    
    index_ = values.index(max(values))
    maximum = max(values)
    return (index_, maximum)

# Question 7

def tps_max(m) -> tuple:
    """Renvoie un tuple ... des tps d'arrêt des m - 1 premiers entiers allant de 1 à m"""
    values = []

    for i in range(1, m + 1):
        values.append(tempsdevol(i))
    
    index_ = values.index(max(values))  # Recyclage de code
    maximum = max(values)               # Recyclage de code
    return(index_, maximum)             # Recyclage de code

# Question 8
