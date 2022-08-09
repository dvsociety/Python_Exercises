"""
Ejercicio 9.5.2. Diccionarios usados para contar.
a) Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad
de apariciones de cada palabra en la cadena. Por ejemplo, si recibe ”Qué lindo día que
hace hoy” debe devolver: { 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1}.
b) Escribir una función que cuente la cantidad de apariciones de cada caracter en una ca-
dena de texto, y los devuelva en un diccionario.
c) Escribir una función que reciba una cantidad de iteraciones de una tirada de 2 dados a
realizar y devuelva la cantidad de veces que se observa cada valor de la suma de los dos
dados.
Nota: utilizar el módulo random para obtener tiradas aleatorias.
"""

def word_counter(phrase: str):
    list_phrase = phrase.split() 
    count_dict = {}
    for word in list_phrase:
        if word not in count_dict:
            count_dict[word.lower()] = 1
        else:
            count_dict[word.lower()] += 1 
    return count_dict

print(word_counter("Que lindo día que hace hoy"))


def character_counter(phrase: str):
    count_dict = {}
    for word in phrase:
        for character in word:
            if character not in count_dict:
                count_dict[character.lower()] = 1
            else:
                count_dict[character.lower()] += 1
    return count_dict

print(character_counter("Contando los caracteres de este texto"))

import random

def sum_die(throws: int):
    sum = 0
    count_dict = {}
    for shoots in range(throws):
        die_one = random.randrange(1,7)
        die_two = random.randrange(1,7)
        sum = die_one + die_two 
        if sum not in count_dict:
            count_dict[sum] = 1
        else:
            count_dict[sum] += 1

    return count_dict

print(sum_die(30))
