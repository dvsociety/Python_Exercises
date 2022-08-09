"""
Ejercicio 6.8.1. Escribir funciones que dada una cadena de caracteres:
"""

# a) Imprima los dos primeros caracteres.
def first_two(sentence):
    return sentence[:2]


# b) Imprima los tres últimos caracteres.
def last_tree(sentence):
    return sentence[-3:]


# c) Imprima dicha cadena cada dos caracteres. Ej.: 'recta' debería imprimir 'rca'
def jumping_characters(sentence):
    return sentence[::2]


# d) Dicha cadena en sentido inverso. Ej.: 'hola mundo!' debe imprimir '!odnum aloh'
def reverse_direction(sentence):
    return sentence[::-1]


# e) Imprima la cadena en un sentido y en sentido inverso. Ej: 'reflejo' imprime 'reflejoojelfer'.
def normal_and_inverse(sentence):
    return sentence[:] + sentence[::-1]


print(first_two("hola mundo"))
