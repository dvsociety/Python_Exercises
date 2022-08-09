"""
Ejercicio 5.7.6. Potencias de dos.
"""

# a) Escribir una función es_potencia_de_dos que reciba como parámetro un número na-
# tural, y devuelva True si el número es una potencia de 2, y False en caso contrario.
def is_potency_of_two(number): 
    x = 1 
    potencyOfTwo = 1
    while potencyOfTwo < number:
        potencyOfTwo = 2 ** x 
        x += 1
        if potencyOfTwo == number:
            return True
    return False 
# print (is_potency_of_two(2))

# b) Escribir una función que, dados dos números naturales pasados como parámetros, de-
# vuelva la suma de todas las potencias de 2 que hay en el rango formado por esos números
# (0 si no hay ninguna potencia de 2 entre los dos). Utilizar la función es_potencia_de_dos,
# descripta en el punto anterior.

def range_potency_of_two(numberOne,NumberTwo):
    sum = 0 
    if numberOne >= NumberTwo:
        max = numberOne
        min = NumberTwo
    else:
        max = NumberTwo
        min = numberOne
    for x in range (min, max+1):
        if is_potency_of_two(x) == True:
            sum += x 
            print (x)
        else: 
            continue
    return sum 

print (range_potency_of_two(2,16))

