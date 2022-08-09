"""
Ejercicio 8.7.5. Escribir una función que reciba una lista ordenada y un elemento. Si el elemento
se encuentra en la lista, debe encontrar su posición mediante búsqueda binaria y devolverlo. Si
no se encuentra, debe agregarlo a la lista en la posición correcta y devolver esa nueva posición.
(No utilizar lista.sort().)
"""

def search_and_put(ordered_list: list, number: int):
    left = 0
    right = len(ordered_list)-1
    center = 0

    while left <= right:
        center = (left + right) // 2 
        print(f"[DEBUG] izquierda: {left} derecha: {right} centro: {center}")

        if number == ordered_list[center]:
            return center
        elif number > ordered_list[center]:
            left = center + 1
        else:
            right = center -1 

    ordered_list.insert(center,number) 
    return center
    

print(search_and_put([1,2,3,4,5,7,8,9,10],6))
