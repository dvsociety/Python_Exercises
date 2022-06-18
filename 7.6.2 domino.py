"""
Ejercicio 7.6.2. Dominó.
a) Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son
recibidas en dos tuplas, por ejemplo: (3,4) y (5,4)
b) Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son
recibidas en una cadena, por ejemplo: 3-4 2-5. Nota: utilizar la función split de las
"""

def domino(dominoes1: tuple, dominoes2: tuple): 
    """Dadas dos tuplas con fichas de dominó, devuelve si encajan o no

    Args:
        dominoes1(tuple): Primera tupla de fichas
        dominoes2(tuple): Segunda tupla de fichas

    Returns:
        boolean: Verdadero si encajan o Falso si no
    """
    for i in range(len(dominoes1)):
        for y in range(len(dominoes2)):
            if dominoes1[i] == dominoes2[y]:
                return True 
    return False 

print(domino((1,3),(2,3)))

def string_domino(dominoes1: str, dominoes2: str):
    sdominoes1 = dominoes1.split("-")
    sdominoes2 = dominoes2.split("-")
    for i in range(len(sdominoes1)):
        for y in range(len(sdominoes2)):
            if sdominoes1[i] == sdominoes2[y]:
                return True
    return False 

print(string_domino("1-2","1-4"))
