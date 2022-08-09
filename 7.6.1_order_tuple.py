"""
Ejercicio 7.6.1. Escribir una función que reciba una tupla de elementos e indique si se encuen-
tran ordenados de menor a mayor o no.
"""

def ordered_items(items: tuple): 
    """Dada una tupla de elementos, informa si se encuentran ordenados

    Args:
        items(tuple): Elementos a comparar

    Returns: 
        boolean: Verdadero o falso
    """

    list_of_items = list(items)
    orderer_list = sorted(items)

    if list_of_items == orderer_list:
        return True
    else:
        return False 

print(ordered_items((1,4,3)))
