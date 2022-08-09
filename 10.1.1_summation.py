"""
Ejercicio 10.1.1. Realizar la implementación correspondiente a la función sumatoria.

Tanto inicial como final deben ser números enteros, y dependiendo de la implementación
a realizar o de la especificación previa, puede ser necesario que final deba ser mayor o igual a
inicial.
Con respecto a f, se trata de una función que será llamada con un parámetro en cada paso
y se requiere poder sumar el resultado, por lo que debe ser una función que reciba un número
y devuelva un número.
"""

def function(number: int):
    return 3*number-1

def summation(initial: int, final: int, f: int):
    """Dado tres numeros, devuelve la sumatoria dada entre el rango inicial, el rango final y la funcion (f)

    Args:
        initial (int): Rango inicial de la sumatoria
        final (int): Rango final de la sumatoria
        f (int): Funcion de la sumatoria

    Returns:
        int: Resultado final de la suma de la sumatoria 
    """
    sum = 0
    for i in range(initial, final+1):
        f = function(i)
        sum += f
    return sum

print(summation(1,5,3))

