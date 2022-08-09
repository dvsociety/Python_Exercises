"""
Ejercicio 7.6.6. Dada una lista de números enteros y un entero k, escribir una función que:
a) Devuelva tres listas, una con los menores, otra con los mayores y otra con los iguales a
k.
b) Devuelva una lista con aquellos que son múltiplos de k.
"""

def max_and_min_in_lists(numbers: list, k: int):
    positives = []
    negatives = []
    k_list = []
    k_multiples = []
    for number in numbers: 
        if number > 0: 
            positives.append(number)
        elif number < 0: 
            negatives.append(number)
        else: 
            raise Exception("El numero no puede ser 0")
        if number == k:
            k_list.append(number)
        if number % k == 0:
            k_multiples.append(number)

    return f"Los numeros positivos son: {positives}\nLos numeros negativos son: {negatives}\nLos numeros iguales a {k} son: {k_list}\nLos numeros multiplos de {k} son {k_multiples}"

print(max_and_min_in_lists([-2,-53,4,5,2],2))
