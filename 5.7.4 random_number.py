"""
Ejercicio 5.7.4. Utilizando la función randrange del módulo random, escribir un programa que
obtenga un número aleatorio secreto, y luego permita al usuario ingresar números y le indique
si son menores o mayores que el número a adivinar, hasta que el usuario ingrese el número
correcto.
"""

import random 

def random_number():
    number = int(input("Elija su numero del 1 al 100 - escriba '-1' para rendirse "))
    secret = random.randrange(100)
    while number != secret and number != -1: 
        if number < secret:
            print ("El numero es mayor")
        elif number > secret:
            print ("el numero es menor")
        number = int(input("Elija nuevamente un numero "))
    print( f"El numero secreto era: {secret}")

random_number()
