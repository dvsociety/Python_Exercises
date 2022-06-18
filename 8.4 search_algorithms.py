"""
Algoritmos de busqueda lineal y busqueda binaria
"""

def lineal_search(list: list,number_to_search: int):
    position = 0
    for number in list:
        if number == number_to_search:
            return position
        else: 
            position += 1
    return -1

# print(lineal_search([-3,9,424,5,2,-1],9))

def binary_search(list: list,number_to_search: int):
    list.sort()
    left = 0
    right = len(list) - 1

    while left <= right:
        center = (left + right) // 2
        print("[DEBUG]", "left:", left, "right:", right, "center:", center)

        if list[center] == number_to_search:
            return center 

        elif list[center] > number_to_search:
            right = center - 1
        else:
            left = center + 1

    return -1

print(binary_search([-3,9,424,5,2,-1],9))

