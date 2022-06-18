"""
Ejercicio 7.6.9. Escribir una función empaquetar para una lista, donde epaquetar significa indi-
car la repetición de valores consecutivos mediante una tupla (valor, cantidad de repeticiones).
Por ejemplo, empaquetar([1, 1, 1, 3, 5, 1, 1, 3, 3]) debe devolver [(1, 3), (3, 1), (5,
1), (1, 2), (3, 2)].
"""

def package(numbers: list):
    count = 1
    new_list = []
    for i in range(len(numbers) - 1 ): 
        if numbers[i] == numbers[i + 1]: 
            count += 1
        else:
            new_value = (numbers[i], count)
            new_list.append(new_value) 
            count = 1
    return new_list

print(package([1, 1, 1, 3, 5, 1, 1, 3, 3]))
