"""
Ejercicio 7.6.8. Inversión de listas
a) Realizar una función que, dada una lista, devuelva una nueva lista cuyo contenido sea
igual a la original pero invertida. Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'],
deberá devolver ['papa', 'a', 'día', 'buen', 'Di'].
b) Realizar otra función que invierta la lista, pero en lugar de devolver una nueva, 
modifique la lista dada para invertirla, sin usar listas auxiliares.
"""

phrase = ["di","buen","dia","a","papá"]

def reverse_list(phrase: list):
    i = len(phrase) -1
    new_list = []
    while i >= 0:
        new_list.append(phrase[i])
        i -= 1
    return new_list

print(reverse_list(phrase))

def pro_reverse_list(phrase: list):
    phrase = phrase.copy()
    lenght_phrase = len(phrase) - 1 
    while lenght_phrase >= 0: 
        phrase.insert(len(phrase),phrase[lenght_phrase])
        lenght_phrase -= 1
    for word in range(len(phrase) // 2):
        phrase.remove(phrase[word])
    return phrase

print(pro_reverse_list(phrase))

def easy_reverse_list(phrase: list):
    phrase = phrase.copy()
    phrase = phrase[::-1]
    return phrase

print(easy_reverse_list(phrase))
