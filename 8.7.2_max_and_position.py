"""
Ejercicio 8.7.2. Escribir una función que reciba una lista de números no ordenada, que:
a) Devuelva el valor máximo.
b) Devuelva una tupla que incluya el valor máximo y su posición.
"""

def max_and_position(unordered_list: list):
    maximum = 0
    position = -1
    count = 0

    for number in unordered_list:
        if number > maximum:
            maximum = number 
            count = 0
        else:
            count += 1

        position += 1 

    position -= count

    return(maximum,position)

print(max_and_position([99,1,4,140,3,70,-54,40]))

def easy_max_and_position(unordered_list: list):
    maximum = 0
    final_position = 0   

    for position, number in enumerate(unordered_list):
        if number > maximum:
            maximum = number 
            final_position = position

    return maximum, final_position

print(easy_max_and_position([99,1,4,140,3,70,-54,40]))

def very_easy_max_and_position(unordered_list: list):
    return max(unordered_list), unordered_list.index(max(unordered_list))

print(very_easy_max_and_position([99,1,4,140,3,70,-54,40]))

