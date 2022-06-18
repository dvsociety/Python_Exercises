"""
Ejercicio 4.6.1. Escribir dos funciones que resuelvan los siguientes problemas:
a) Dado un número entero n, indicar si es par o no.
b) Dado un número entero n, indicar si es primo o no.
"""

def even_and_odd_number(number):
    if number % 2 == 0:
        return "par"
    else:
        return "impar"

# print (even_and_odd_number(-1))

def prime_number(number):
    for i in range (2,number):
        if number % i == 0:
            return "no primo"
    return "primo"

print (prime_number(45))
