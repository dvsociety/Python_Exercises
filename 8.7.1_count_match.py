"""
Ejercicio 8.7.1. Escribir una función que reciba una lista desordenada y un elemento, que:
a) Busque todos los elementos coincidan con el pasado por parámetro y devuelva la can-
tidad de coincidencias encontradas.
b) Busque la primera coincidencia del elemento en la lista y devuelva su posición.
c) Utilizando la función anterior, busque todos los elementos que coincidan con el pasado
por parámetro y devuelva una lista con las posiciones.
"""

def count_elements(unordered_list: list, number_to_search: int):
    count = 0 

    for number in unordered_list:
        if number_to_search == number:
            count += 1
    return count   

# print(count_elements([3,4,5,756,32,-4,3,-532,3,3],3))

def fist_match(unordered_list: list, number_to_search: int):
    position = 0

    for number in unordered_list:
        if number_to_search == number:
            return position
        else:
            position += 1

# print(fist_match([4,5,756,32,-4,3,-532,3,3],3))

def count_and_matchs(unordered_list: list, number_to_search: int):
    unordered_list = unordered_list.copy()
    new_list = []
    count = 0
    
    while number_to_search in unordered_list:
        new_list.append(fist_match(unordered_list, number_to_search) + count) 
        unordered_list.remove(number_to_search)  
        count += 1
    return(new_list)

print(count_and_matchs([3,4,5,756,32,-4,3,-532,3,3],3))
