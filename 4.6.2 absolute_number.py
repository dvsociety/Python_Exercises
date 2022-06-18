"""
Ejercicio 4.6.2. Escribir una implementación propia de la función abs, que devuelva el valor
absoluto de cualquier valor que reciba.
"""

def absolute_number(number):
    if number >= 0: 
        return number
    else:
        return number * -1

print(absolute_number(0))

        
